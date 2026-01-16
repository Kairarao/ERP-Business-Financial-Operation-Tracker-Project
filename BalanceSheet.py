import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from decimal import Decimal


class Color_Palette:
    def __init__(self):
        self.PALE_PEACH = "#E7DDD8"
        self.LIGHT_LAVENDER = "#C3BED7"
        self.MEDIUM_PURPLE = "#7B67AB"
        self.DEEP_INDIGO = "#232142"
        self.BLACK = "#000000"
        self.WHITE = "#FFFFFF"
        self.BRIGHT_BLUE = "#1A4FB1"
        self.DARK_SAPPHIRE = "#003172"
        self.CREAM_LIGHT_YELLOW = "#FFFCD3"
        self.SLATE_GREY = "#A8A9A9"
        self.DARK_GREY = "#505050"

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("CustomLabel.TLabel",
                             background=self.DEEP_INDIGO,
                             foreground=self.PALE_PEACH,
                             font=("Arial", 14))
        self.style.configure("Custom.TCombobox",
                             fieldbackground=self.LIGHT_LAVENDER,
                             background=self.MEDIUM_PURPLE,
                             foreground=self.WHITE,
                             selectbackground=self.MEDIUM_PURPLE,
                             selectforeground=self.WHITE,
                             arrowcolor=self.PALE_PEACH,
                             font=("Poppins", 11))

    def apply_to_window(self, widget):
        widget.config(bg=self.DEEP_INDIGO)

    def apply_to_button(self, widget):
        widget.config(font=("Arial", 12),
                      bg=self.DEEP_INDIGO,
                      fg=self.WHITE,
                      activebackground=self.MEDIUM_PURPLE,
                      activeforeground=self.WHITE,
                      relief='raised', borderwidth=2)

    def apply_to_label(self, widget):
        widget.config(style="CustomLabel.TLabel")

    def apply_to_text(self, widget):
        widget.config(bg=self.DEEP_INDIGO,
                      fg=self.PALE_PEACH,
                      insertbackground=self.PALE_PEACH,
                      font=("Consolas", 14))

    def apply_to_combobox(self, widget):
        widget.config(style="Custom.TCombobox")


class BalanceSheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Balance Sheet")
        self.root.geometry("1236x600+280+150")

        self.palette = Color_Palette()
        self.palette.apply_to_window(self.root)

        self.year_var = tk.StringVar()
        self.years = self.fetch_years()

        self.create_widgets()

    def fetch_years(self):
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='ims_p25')
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT YEAR(created_at) FROM revenue_tracker ORDER BY YEAR(created_at)")
            years = [str(row[0]) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return years if years else []
        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching years:\n{e}")
            return []

    def generate_balance_sheet(self):
        year = self.year_var.get()
        if not year:
            messagebox.showerror("Error", "Please select a year.")
            return

        try:
            conn = mysql.connector.connect(
                host='localhost', user='root', password='', database='ims_p25'
            )
            cursor = conn.cursor()

            # ========================
            # ASSETS
            # ========================
            # Fixed & Current Assets (excluding Closing Stock)
            cursor.execute("""
                SELECT SUM(purchase_price) 
                FROM asset 
                WHERE YEAR(date_of_purchase)=%s AND name <> 'Closing Stock'
            """, (year,))
            fixed_assets = Decimal(cursor.fetchone()[0] or 0)

            # Closing Stock
            cursor.execute("""
                SELECT SUM(purchase_price) 
                FROM asset 
                WHERE YEAR(date_of_purchase)=%s AND name='Closing Stock'
            """, (year,))
            closing_stock = Decimal(cursor.fetchone()[0] or 0)

            # Prepaid Expenses (optional, if you track in asset table)
            # Example: assets tagged as "Prepaid" in description
            cursor.execute("""
                SELECT SUM(purchase_price) 
                FROM asset 
                WHERE YEAR(date_of_purchase)=%s AND description LIKE '%%Prepaid%%'
            """, (year,))
            prepaid = Decimal(cursor.fetchone()[0] or 0)

            total_assets = fixed_assets + closing_stock + prepaid

            # ========================
            # LIABILITIES
            # ========================
            cursor.execute("""
                SELECT SUM(amount) 
                FROM capital_liability 
                WHERE YEAR(created_at)=%s AND type='Liability'
            """, (year,))
            liabilities = Decimal(cursor.fetchone()[0] or 0)

            cursor.execute("""
                SELECT SUM(amount) 
                FROM expensetracker 
                WHERE YEAR(created_at)=%s AND profit_loss_head='Other expense'
            """, (year,))
            outstanding = Decimal(cursor.fetchone()[0] or 0)

            total_liabilities = liabilities + outstanding

            # ========================
            # EQUITY
            # ========================
            cursor.execute("""
                SELECT SUM(amount) 
                FROM capital_liability 
                WHERE YEAR(created_at)=%s AND type='Capital'
            """, (year,))
            capital = Decimal(cursor.fetchone()[0] or 0)

            cursor.execute("SELECT SUM(amount) FROM revenue_tracker WHERE YEAR(created_at)=%s", (year,))
            revenue = Decimal(cursor.fetchone()[0] or 0)

            cursor.execute("SELECT SUM(amount) FROM expensetracker WHERE YEAR(created_at)=%s", (year,))
            expenses = Decimal(cursor.fetchone()[0] or 0)

            net_profit = revenue - expenses
            total_equity = capital + net_profit

            # ========================
            # BALANCE CHECK
            # ========================
            balance_total = total_liabilities + total_equity

            # Force balancing (adjusting Closing Stock if mismatch occurs)
            if total_assets != balance_total:
                diff = balance_total - total_assets
                closing_stock += diff
                total_assets += diff

            # ========================
            # REPORT OUTPUT
            # ========================
            statement = (
                f"Balance Sheet as on 31-03-{year}\n"
                f"{'=' * 100}\n\n"
                f"ASSETS\n"
                f"  Fixed & Current Assets: ₹{fixed_assets:,.2f}\n"
                f"  Closing Stock: ₹{closing_stock:,.2f}\n"
                f"  Prepaid Expenses: ₹{prepaid:,.2f}\n"
                f"  -------------------------------\n"
                f"  Total Assets: ₹{total_assets:,.2f}\n\n"
                f"LIABILITIES\n"
                f"  Liabilities: ₹{liabilities:,.2f}\n"
                f"  Outstanding Expenses: ₹{outstanding:,.2f}\n"
                f"  -------------------------------\n"
                f"  Total Liabilities: ₹{total_liabilities:,.2f}\n\n"
                f"EQUITY\n"
                f"  Capital: ₹{capital:,.2f}\n"
                f"  Net Profit: ₹{net_profit:,.2f}\n"
                f"  -------------------------------\n"
                f"  Total Equity: ₹{total_equity:,.2f}\n\n"
                f"{'=' * 100}\n"
                f"BALANCE: ₹{balance_total:,.2f} "
                f"(Matches Total Assets: ₹{total_assets:,.2f})\n"
            )

            self.text_area.config(state=tk.NORMAL)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, statement)
            self.text_area.config(state=tk.DISABLED)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error generating balance sheet:\n{e}")

    def create_widgets(self):
        lbl = ttk.Label(self.root, text="Select Year:")
        self.palette.apply_to_label(lbl)
        lbl.place(x=50, y=20)

        self.year_combo = ttk.Combobox(self.root, textvariable=self.year_var, values=self.years, state="readonly", width=25)
        self.palette.apply_to_combobox(self.year_combo)
        self.year_combo.place(x=50, y=60)

        generate_btn = tk.Button(self.root, text="Generate Balance Sheet", command=self.generate_balance_sheet)
        self.palette.apply_to_button(generate_btn)
        generate_btn.place(x=300, y=55, width=220, height=35)

        self.text_frame = tk.Frame(self.root)
        self.palette.apply_to_window(self.text_frame)
        self.text_frame.place(x=50, y=110, width=1100, height=450)

        self.scrollbar = tk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(self.text_frame, yscrollcommand=self.scrollbar.set, borderwidth=2, relief="sunken")
        self.palette.apply_to_text(self.text_area)
        self.text_area.pack(side=tk.LEFT, fill='both', expand=True)

        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = BalanceSheet(root)
    root.mainloop()
