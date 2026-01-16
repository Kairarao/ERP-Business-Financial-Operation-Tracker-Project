import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import os
import mysql.connector
import mysql.connector
import color_palette
import employee as emp
from conn import *

from color_palette import *
from visualize import FinancialDashboard
from demo_gui import Notes
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from Invoice import Invoice
from expenses import Expenses
from asset import assetClass
from liability import liabilityClass
from reports import reportsClass


class IMS:
    def __init__(self, root):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="", database="ims_p25")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred due to {ex}")
        palette = Color_Palette()
        palette.apply_to_window(root)
        self.root = root
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}+0+0")
        root.state('zoomed')
        # self.root.geometry("1350x700+110+80")
        self.root.title("Inventory Management System")
        # self.root.resizable(False,False)
        # self.root.config(bg="white")

        # ---------------- Top Frame ---------------
        TopMenu = Frame(self.root, bd=2, relief="raised")
        TopMenu.place(x=260, y=0, width=width - 260, height=100)
        palette.apply_to_window(TopMenu)

        # ----------------  Menu Bar ---------------
        Menu_bar = Frame(self.root, bd=2, relief="raised")
        Menu_bar.place(x=260, y=80, width=width - 260, height=40)
        palette.apply_to_window(Menu_bar)

        # ---------------- left menu ---------------
        self.MenuLogo = Image.open("K:\\IMP_2025\\Inventory-Management-System-main\\images\\menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        L_Menu = Frame(self.root, bd=0.5, relief="solid")
        L_Menu.place(x=0, y=0, width=260, height=780)
        LeftMenu = Frame(L_Menu, bd=0, relief="ridge")
        LeftMenu.place(x=5, y=25, width=250, height=780)
        palette.apply_to_window(LeftMenu)
        palette.apply_to_window(L_Menu)

        # ------------- title --------------
        self.icon_title = PhotoImage(file="K:\\IMP_2025\\Inventory-Management-System-main\\images\\logo1.png")
        title = Label(TopMenu, text="Inventory Management System", image=self.icon_title, compound="left",
                      font=("times new roman", 40, "bold"), anchor="w", padx=20)
        title.place(x=130, y=0, relwidth=1, height=70)
        palette.apply_to_label(title, 'active')

        # ------------ logout button -----------
        btn_logout = Button(TopMenu, text="Logout", font=("times new roman", 15, "bold"), cursor="hand2", command=self.destroy)
        btn_logout.place(x=width - 450, y=15, height=50, width=150)
        # btn_logout.pack(side="right")
        palette.apply_to_button(btn_logout, 'active')

        # ------------ clock -----------------
        self.lbl_clock = Label(Menu_bar, text="Date:DD:MM:YYYY Time:HH:MM:SS", font=("times new roman", 15))
        palette.apply_to_label(self.lbl_clock, 'active')
        self.lbl_clock.place(width=width - 260, height=30)
        self.lbl_clock.pack(side="right")

        # ---------------- left Frame_deco ---------------
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side="top", fill="y")

        lbl_menu = (Label(LeftMenu, text="Menu", font=("times new roman", 20)))
        lbl_menu.pack(side="top", fill="x")
        palette.apply_to_label(lbl_menu, 'active')
        self.icon_side = PhotoImage(file="K:\\IMP_2025\\Inventory-Management-System-main\\images\\side.png")

        btn_billing = Button(LeftMenu, text="Revenue", command=self.billing, compound="left", padx=20,pady=10, anchor="center",font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_billing.pack(side="top", fill="x")
        btn_expenses = Button(LeftMenu, text="Expenses", command=self.expenses, compound="left", padx=20,pady=10, anchor="center",font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_expenses.pack(side="top", fill="x")

        btn_asset = Button(LeftMenu, text="Asset", command=self.asset, compound="left", padx=20,pady=10,
                              anchor="center", font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_asset.pack(side="top", fill="x")
        btn_lia = Button(LeftMenu, text="Liability", command=self.liability, compound="left", padx=20,pady=10,
                           anchor="center", font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_lia.pack(side="top", fill="x")
        palette.apply_to_button(btn_lia, 'active')
        btn_report = Button(LeftMenu, text="Reports", command=self.reports, compound="left", padx=20,pady=10,
                         anchor="center", font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_report.pack(side="top", fill="x")
        palette.apply_to_button(btn_report, 'active')
        btn_vis = Button(LeftMenu, text="Visuals", command=self.vis, compound="left", padx=20,pady=10,
                           anchor="center", font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_vis.pack(side="top", fill="x")
        palette.apply_to_button(btn_vis, 'active')

        btn_notes = Button(LeftMenu, text="Take Notes", command=self.notes, compound="left", padx=20,pady=10,
                            anchor="center", font=("times new roman", 20, "bold"), bd=8, cursor="hand2")
        btn_notes.pack(side="top", fill="x")
        palette.apply_to_button(btn_notes, 'active')

        # ---------------- Menu Bar Compo ---------------
        btn_employee = Button(Menu_bar, text="Employee", command=self.employee, image=self.icon_side, compound="left",
                              padx=20, anchor="center", font=("times new roman", 14, "bold"), bd=0, cursor="hand2")
        btn_employee.pack(side="left")
        btn_supplier = Button(Menu_bar, text="Supplier", command=self.supplier, image=self.icon_side, compound="left",
                              padx=20, anchor="center", font=("times new roman", 14, "bold"), bd=0, cursor="hand2")
        btn_supplier.pack(side="left")
        btn_category = Button(Menu_bar, text="Category", command=self.category, image=self.icon_side, compound="left",
                              padx=20, anchor="center", font=("times new roman", 14, "bold"), bd=0, cursor="hand2")
        btn_category.pack(side="left")
        btn_product = Button(Menu_bar, text="Products", command=self.product, image=self.icon_side, compound="left",
                             padx=20, anchor="center", font=("times new roman", 14, "bold"), bd=0, cursor="hand2")
        btn_product.pack(side="left")
        btn_sales = Button(Menu_bar, text="Sales", command=self.sales, image=self.icon_side, compound="left", padx=20,
                           anchor="center", font=("times new roman", 14, "bold"), bd=0, cursor="hand2")
        btn_sales.pack(side="left")

        # btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound="left",padx=20,anchor="center",font=("times new roman",14,"bold"),bd=0,cursor="hand2")
        # btn_exit.pack(side="top",fill="x")

        # ---------------- Palette application ---------------
        palette.apply_to_button(btn_employee, 'active')
        palette.apply_to_button(btn_supplier, 'active')
        palette.apply_to_button(btn_category, 'active')
        palette.apply_to_button(btn_product, 'active')
        palette.apply_to_button(btn_sales, 'active')
        palette.apply_to_button(btn_billing, 'active')

        palette.apply_to_button(btn_expenses, 'active')
        palette.apply_to_button(btn_asset, 'active')

        # ---------------- WorkSpace Frame ---------------
        self.workspace = Frame(self.root, bd=0, relief="solid")
        self.workspace.place(x=280, y=150, width=width - 300, height=600)
        palette.apply_to_window(self.workspace)

        # ----------- content of Workspace----------------
        self.lbl_employee = Label(self.workspace, text="Total Employee\n{ 0 }", bd=5, relief="ridge", bg="#33bbf9",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=100, y=100, height=150, width=300)
        palette.apply_to_label(self.lbl_employee, 'active')

        self.lbl_supplier = Label(self.workspace, text="Total Supplier\n{ 0 }", bd=5, relief="ridge", bg="#ff5722",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=450, y=100, height=150, width=300)
        palette.apply_to_label(self.lbl_supplier, 'active')

        self.lbl_category = Label(self.workspace, text="Total Category\n{ 0 }", bd=5, relief="ridge", bg="#009688",
                                  fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=800, y=100, height=150, width=300)
        palette.apply_to_label(self.lbl_category, 'active')

        self.lbl_product = Label(self.workspace, text="Total Product\n{ 0 }", bd=5, relief="ridge", bg="#607d8b",
                                 fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)
        palette.apply_to_label(self.lbl_product, 'active')

        self.lbl_sales = Label(self.workspace, text="Total Sales\n{ 0 }", bd=5, relief="ridge", bg="#ffc107",
                               fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        palette.apply_to_label(self.lbl_sales, 'active')

        # ------------ footer -----------------
        lbl_footer = (Label(self.workspace, text="_______", font=("times new roman", 12), bg="#4d636d", fg="white"))
        lbl_footer.pack(side="bottom", fill="x")
        palette.apply_to_label(lbl_footer, 'active')
        self.update_content()

    # -------------- functions ----------------
    def destroy(self):
        root.destroy()
    def vis(self):
        self.new_win=Toplevel(self.root)
        self.new_obj= FinancialDashboard(self.new_win)




    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
    def notes(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Notes(self.new_win)
    def asset(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = assetClass(self.new_win)
    def liability(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = liabilityClass(self.new_win)
    def reports(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportsClass(self.new_win)
    def expenses(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Expenses(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Invoice(self.new_win)

    def update_content(self):

        cur = self.con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n[ {str(len(supplier))} ]")

            bill = len(os.listdir("K:/IMP_2025/Inventory-Management-System-main/Inventory-Management-System/bill"))
            self.lbl_sales.config(text=f"Total Sales\n[ {str(bill)} ]")

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f" Date: {str(date_)} Time: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = tkinter.Tk()
    obj = IMS(root)
    root.mainloop()

    """
        #other revenue page
        Return inwards and outwards record page
        balance recording 
        asset management system
        capital/liability management system
        profit and loss statement
        balance sheet 
        adjustments
        """