import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine

# --- Styling & theme ---
plt.style.use("dark_background")
sns.set_theme(style="dark")

POWER_COLORS = {
    "revenue": "#4CAF50",
    "expense": "#E53935",
    "accent": "#1E88E5",
    "card_bg": "#222233",
    "card_border": "#2e2e3f",
    "text": "#EAEAF2",
    "muted": "#9AA0B4"
}

class FinancialDashboard:
    def __init__(self, root, year=2025):
        self.root = root
        self.year = year
        root.title("REPORTS")
        root.geometry("1260x600+270+150")
        root.configure(bg="#151520")

        # DB engine
        self.engine = create_engine("mysql+mysqlconnector://root:@localhost/ims_p25")

        # Scrollable canvas
        container = tk.Frame(root, bg=root["bg"])
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg=root["bg"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Inner cards frame
        self.cards_frame = tk.Frame(self.canvas, bg=root["bg"])
        self.canvas.create_window((0, 0), window=self.cards_frame, anchor="nw")
        self.cards_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.cards_frame.columnconfigure(0, weight=1)
        self.cards_frame.columnconfigure(1, weight=1)

        self._load_data()
        self._create_charts()

    def fetch(self, query):
        return pd.read_sql(query, self.engine)

    def _load_data(self):
        try:
            self.revenue = self.fetch("SELECT date, category, amount FROM revenue_tracker")
            self.revenue["date"] = pd.to_datetime(self.revenue["date"])
        except:
            self.revenue = pd.DataFrame(columns=["date", "category", "amount"])

        try:
            self.expense = self.fetch("SELECT Date AS date, category, Amount AS amount FROM expensetracker")
            self.expense["date"] = pd.to_datetime(self.expense["date"])
        except:
            self.expense = pd.DataFrame(columns=["date", "category", "amount"])

        try:
            self.asset = self.fetch("SELECT asset_type, purchase_price FROM asset")
        except:
            self.asset = pd.DataFrame(columns=["asset_type", "purchase_price"])

        try:
            self.capital_liability = self.fetch("SELECT type, amount FROM capital_liability")
        except:
            self.capital_liability = pd.DataFrame(columns=["type", "amount"])

    # ---------- Card frame ----------
    def _card_frame(self, parent, title, row, col, colspan=1):
        card = tk.Frame(parent, bg=POWER_COLORS["card_bg"])
        card.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

        title_bar = tk.Frame(card, bg=POWER_COLORS["card_border"], height=36)
        title_bar.pack(fill="x")

        lbl = tk.Label(title_bar, text=title, bg=POWER_COLORS["card_border"],
                       fg=POWER_COLORS["text"], font=("Segoe UI", 11, "bold"), padx=10)
        lbl.pack(side="left", pady=6)

        return card

    # ---------- PLOT FUNCTIONS ----------
    def _fig_revenue_vs_expense(self):
        fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
        rev_y = self.revenue.groupby(self.revenue["date"].dt.year)["amount"].sum() if not self.revenue.empty else pd.Series()
        exp_y = self.expense.groupby(self.expense["date"].dt.year)["amount"].sum() if not self.expense.empty else pd.Series()

        years = sorted(set(rev_y.index.tolist() + exp_y.index.tolist()))
        rev_vals = [rev_y.get(y, 0) for y in years]
        exp_vals = [exp_y.get(y, 0) for y in years]

        ax.bar([y - 0.2 for y in years], rev_vals, width=0.35, color=POWER_COLORS["revenue"], label="Revenue")
        ax.bar([y + 0.2 for y in years], exp_vals, width=0.35, color=POWER_COLORS["expense"], label="Expense")

        ax.set_title("Revenue vs Expense (Yearly)", color=POWER_COLORS["text"])
        ax.legend(facecolor="#2a2a3a", edgecolor="#444")
        ax.set_facecolor("#151520")
        return fig

    def _fig_monthly_trend(self, which):
        fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
        df = self.revenue if which == "revenue" else self.expense

        if df.empty:
            ax.text(0.5, 0.5, f"No {which} data", ha="center", va="center", color="white")
            return fig

        s = df[df["date"].dt.year == self.year].groupby(df["date"].dt.month)["amount"].sum().reindex(range(1, 13), fill_value=0)
        color = POWER_COLORS["revenue"] if which == "revenue" else POWER_COLORS["expense"]

        ax.plot(s.index, s.values, marker="o", linewidth=2.2, color=color)
        ax.set_title(f"Monthly {which.capitalize()} Trend — {self.year}", color=POWER_COLORS["text"])
        ax.set_facecolor("#151520")
        return fig

    def _fig_pie(self, which):
        fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
        df = self.revenue if which == "revenue" else self.expense

        if df.empty:
            ax.text(0.5, 0.5, "No data", ha="center", color="white")
            return fig

        s = df[df["date"].dt.year == self.year].groupby("category")["amount"].sum()
        ax.pie(s.values, labels=s.index, autopct="%1.1f%%", textprops={"color": "white"})
        ax.set_title(f"{which.capitalize()} Breakdown — {self.year}", color=POWER_COLORS["text"])
        return fig

    def _fig_asset(self):
        fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
        if self.asset.empty:
            ax.text(0.5, 0.5, "No assets", ha="center", color="white")
            return fig
        s = self.asset.groupby("asset_type")["purchase_price"].sum()
        ax.bar(s.index, s.values, color="#8be9fd")
        ax.set_title("Asset Distribution", color=POWER_COLORS["text"])
        return fig

    def _fig_cl(self):
        fig, ax = plt.subplots(figsize=(3, 3), dpi=100)
        if self.capital_liability.empty:
            ax.text(0.5, 0.5, "No data", ha="center", color="white")
            return fig
        s = self.capital_liability.groupby("type")["amount"].sum()
        ax.bar(s.index, s.values, color=[POWER_COLORS["revenue"], POWER_COLORS["expense"]])
        ax.set_title("Capital vs Liability", color=POWER_COLORS["text"])
        return fig

    # ---------- BUILD DASHBOARD ----------
    def _create_charts(self):
        tiles = [
            (f"Revenue Breakdown — {self.year}", lambda: self._fig_pie("revenue")),
            ("Revenue vs Expense (Yearly)", self._fig_revenue_vs_expense),
            ("Asset Distribution", self._fig_asset),# This one spans 2 columns
            (f"Expense Breakdown — {self.year}", lambda: self._fig_pie("expense")),
            ("Capital vs Liability", self._fig_cl),
            (f"Monthly Revenue — {self.year}", lambda: self._fig_monthly_trend("revenue")),
            (f"Monthly Expense — {self.year}", lambda: self._fig_monthly_trend("expense")),

        ]
        row = 0
        col = 0
        for title, fig_fn in tiles:
            if title == "Asset Distribution":
                card = self._card_frame(self.cards_frame, title, row, 2, colspan=2)
                col += 1
            else:
                card = self._card_frame(self.cards_frame, title, row, col)
            fig = fig_fn()
            fig.patch.set_facecolor(POWER_COLORS["card_bg"])
            for ax in fig.axes:
                ax.patch.set_facecolor(POWER_COLORS["card_bg"])
                for spine in ax.spines.values():
                    spine.set_color("#2f2f3f")
                ax.tick_params(colors=POWER_COLORS["muted"])
                ax.title.set_color(POWER_COLORS["text"])

            canvas = FigureCanvasTkAgg(fig, master=card)
            canvas.get_tk_widget().pack(fill="both", expand=True, padx=8, pady=8)

            col=col+1
            if col == 4:
                col=0
                row=row+1

if __name__ == "__main__":
    root = tk.Tk()
    FinancialDashboard(root, year=2025)
    root.mainloop()
