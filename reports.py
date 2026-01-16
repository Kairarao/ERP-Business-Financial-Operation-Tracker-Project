from color_palette import Color_Palette
import tkinter
from tkinter import *
import time
import os
from tkinter import messagebox
from conn import *
from ProfitLoss import ProfitLoss
from BalanceSheet import BalanceSheet

class reportsClass:
    def __init__(self, root):
        self.root = root
        palette = Color_Palette()
        palette.apply_to_window(root)
        self.root = root
        self.root.geometry("1236x600+280+150")
        self.root.title("Reporting")
        self.workspace = Frame(self.root, bd=0, relief="solid")
        self.workspace.place(x=0, y=0, width=1236, height=600)
        palette.apply_to_window(self.workspace)
        self.lbl_expense = Label(self.workspace, text="Total Expenses\n{ 0 }", bd=5, relief="ridge", bg="#33bbf9",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_expense.place(x=100, y=50, height=150, width=300)
        palette.apply_to_label(self.lbl_expense, 'active')

        self.lbl_sales = Label(self.workspace, text="Total Sales\n{ 0 }", bd=5, relief="ridge", bg="#ff5722",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=450, y=50, height=150, width=300)
        palette.apply_to_label(self.lbl_sales, 'active')

        self.lbl_revenue = Label(self.workspace, text="Total Revenue\n{ 0 }", bd=5, relief="ridge", bg="#009688",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_revenue.place(x=800, y=50, height=150, width=300)
        palette.apply_to_label(self.lbl_revenue, 'active')

        self.lbl_asset = Label(self.workspace, text="Total Assets\n{ 0 }", bd=5, relief="ridge", bg="#607d8b",
                                 fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_asset.place(x=300, y=250, height=150, width=300)
        palette.apply_to_label(self.lbl_asset, 'active')

        self.lbl_liability = Label(self.workspace, text="Total Liabilities\n{ 0 }", bd=5, relief="ridge", bg="#ffc107",
                               fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_liability.place(x=650, y=250, height=150, width=300)
        palette.apply_to_label(self.lbl_liability, 'active')
        self.update_content()

        #buttons
        buttomMenu = Frame(self.workspace, bd=0, relief="ridge")
        buttomMenu.place(x=5, y=450, width=1200, height=250)
        palette.apply_to_window(buttomMenu)
        btn_PandL = Button(buttomMenu, text="Profit & Loss Statement", command=self.PandL, compound="left", padx=20, anchor="center",
                             font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_PandL.pack(side="top", fill="x")
        palette.apply_to_button(btn_PandL)
        btn_BS = Button(buttomMenu, text="Balance Sheet", command=self.BS,  compound="left", padx=20,
                              anchor="center", font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_BS.pack(side="top", fill="x")
        palette.apply_to_button(btn_BS)
    
    def update_content(self):

        cur = con.cursor()
        try:
            cur.execute("select * from asset")
            product = cur.fetchall()
            self.lbl_asset.config(text=f"Total Asset\n[ {str(len(product))} ]")

            cur.execute("select * from revenue_tracker")
            category = cur.fetchall()
            self.lbl_revenue.config(text=f"Total Revenue\n[ {str(len(category))} ]")

            cur.execute("select * from expensetracker")
            employee = cur.fetchall()
            self.lbl_expense.config(text=f"Total Expenses\n[ {str(len(employee))} ]")

            cur.execute("select * from capital_liability")
            supplier = cur.fetchall()
            self.lbl_liability.config(text=f"Total Liabilities\n[ {str(len(supplier))} ]")

            bill = len(os.listdir("K://IMP_2025//Inventory-Management-System-main//Inventory-Management-System/bill"))
            self.lbl_sales.config(text=f"Total Sales\n[ {str(bill)} ]")


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    def PandL(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProfitLoss(self.new_win)
    def BS(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BalanceSheet(self.new_win)


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = reportsClass(root)
    root.mainloop()