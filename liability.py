from tkinter import *

from PIL.Image import Palette
from matplotlib.pyplot import close
from numpy.random import geometric

from color_palette import *
from conn import *
import datetime
from tkcalendar import DateEntry
from datetime import *
import tkinter.messagebox as mb


class liabilityClass:
    def __init__(self, root):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ims_P25'
        )
        self.cursor = self.con.cursor()
        self.root = root
        self.palette=Color_Palette()
        palette = Color_Palette()
        self.root = root
        self.root.geometry("1350x700+110+80")
        self.root.title("liability Management System")
        palette.apply_to_window(root)

        # StringVar and DoubleVar variables
        self.desc = StringVar()
        self.amnt = DoubleVar()
        self.creditor = StringVar()
        self.MoP = StringVar(value='Cash')
        self.amount = DoubleVar()
        self.resale_value = DoubleVar()
        self.life = IntVar()
        self.desc = StringVar()
        self.amount = DoubleVar()
        self.creditor_name = StringVar()
        self.status = StringVar()
        self.interest_rate = DoubleVar()
        self.due_date = StringVar()  # Use string to receive date from Entry widget
        self.entry_date = datetime.now()

        # Define StringVars for subwin inputs
        self.serial_number_var = StringVar()
        self.manufacturer_var = StringVar()
        self.description_var = StringVar()
        self.location_var = StringVar()
        self.status_var = StringVar()
        self.owner_var = StringVar()
        self.warranty_expiry_var = StringVar()
        self.maintenance_schedule_var = StringVar()

        # Frames
        self.data_entry_frame = Frame(root)
        palette.apply_to_window(self.data_entry_frame)
        self.data_entry_frame.place(relx=0, rely=0, relwidth=1.0, relheight=0.30)
        self.L0 = Label(self.data_entry_frame, text="Liabilities", font=("Arial", 18, "bold"), bg="Indigo",
                        fg="white")
        self.L0.place(x=50, y=5)
        buttons_frame = Frame(root)
        palette.apply_to_window(buttons_frame)
        buttons_frame.place(relx=0, rely=0.30, relheight=0.95, relwidth=0.25)
        tree_frame = Frame(root)
        tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)
        palette.apply_to_window(tree_frame)

        # Data Entry Frame
        self.L1 = Label(self.data_entry_frame, text='Date (M/DD/YY) :', )
        self.L1.place(x=200, y=5)
        self.date_ent = DateEntry(self.data_entry_frame, date=datetime.now().date())
        self.date_ent.place(x=380, y=10)
        palette.apply_to_label(self.L1)

        self.cat_l = Label(self.data_entry_frame, text="Liability:        ")
        self.cat_l.place(x=50, y=50)
        palette.apply_to_label(self.cat_l)

        self.cursor = con.cursor()
        self.cursor.execute("SELECT lia_name FROM liabilit_cat")
        self.all_liability= [row[0] for row in self.cursor.fetchall()]
        self.cursor.close()
        self.combo_rev = ttk.Combobox(self.data_entry_frame, state="normal", values=self.all_liability,
                                      style="Custom.TCombobox")
        self.combo_rev.place(x=120, y=50, width=200, height=28)

        """self.expen_l = Label(self.data_entry_frame, text="liabilitys:        ")
        self.expen_l.place(x=10, y=150)
        palette.apply_to_label(self.expen_l)

        self.combo_expen = ttk.Combobox(self.data_entry_frame, state="normal", style="Custom.TCombobox")
        self.combo_expen.place(x=120, y=150, width=200, height=28)"""

        self.L3 = Label(self.data_entry_frame, text='Description :')
        self.L3.place(x=350, y=50)
        self.ent_desc = Entry(self.data_entry_frame, width=31, textvariable=self.desc)
        self.ent_desc.place(x=480, y=55)

        self.L4 = Label(self.data_entry_frame, text='Amount :', )
        self.L4.place(x=50, y=100)
        self.ent_amnt = Entry(self.data_entry_frame, width=14, textvariable=self.amount)
        self.ent_amnt.place(x=150, y=105)

        self.L2 = Label(self.data_entry_frame, text='Creditor Name  :', )
        self.L2.place(x=700, y=50)
        self.ent_creditor = Entry(self.data_entry_frame, width=31, textvariable=self.creditor)
        self.ent_creditor.place(x=850, y=55)
        L5=Label(self.data_entry_frame, text="Status:")
        L5.place(x=300, y=100)
        self.status_entry = Entry(self.data_entry_frame, textvariable=self.status)
        self.status_entry.place(x=380, y=105)
        L6=Label(self.data_entry_frame, text="Interest Rate (%):")
        L6.place(x=550, y=100)
        self.interest_entry = Entry(self.data_entry_frame, textvariable=self.interest_rate)
        self.interest_entry.place(x=730, y=105)
        L7=Label(self.data_entry_frame, text="Due Date (YYYY-MM-DD):")
        L7.place(x=890, y=105)
        self.due_date_entry = Entry(self.data_entry_frame, textvariable=self.due_date)
        self.due_date_entry.place(x=1120, y=110)
        """self.L5 = Label(self.data_entry_frame, text='Mode of Payment:')
        self.L5.place(x=1000, y=50)
        

        self.dd1 = OptionMenu(self.data_entry_frame, self.MoP,
                              *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay'])
        self.dd1.place(x=1180, y=50)
        self.dd1.configure(width=10)"""
        palette.apply_to_label(self.L1, 'active')
        palette.apply_to_label(self.L2, 'active')
        palette.apply_to_label(self.L3, 'active')
        palette.apply_to_label(self.L4, 'active')
        palette.apply_to_label(L5, 'active')
        palette.apply_to_label(L6, 'active')
        palette.apply_to_label(L7, 'active')


        #palette.apply_to_label(self.L5, 'active')







        b9=Button(buttons_frame, text='Calculate Depreciation', command=self.on_calc_dep,width=25)

        palette.apply_to_button(b9,'active')

        # Buttons' Frame
        self.B7 = Button(buttons_frame, text='Add liability', command=self.add_another_liability, width=20)
        self.B7.place(x=30, y=0)
        self.B8 = (Button(buttons_frame, text='Convert to words before adding'))
        self.B8.place(x=30, y=50)
        self.B5 = Button(buttons_frame, text='Edit Selected liability', command=self.edit_liability, width=25, )
        self.B5.place(x=30, y=100)

        self.B2 = (Button(buttons_frame, text='Clear Fields in DataEntry Frame', width=25, command=self.clear_fields))
        self.B2.place(x=30, y=150)
        b9.place(x=30, y=200)
        self.B1 = Button(buttons_frame, text='Delete liability', width=25, command=self.remove_liability)
        self.B1.place(x=30, y=250)

        self.B3 = Button(buttons_frame, text='Delete All liability', width=25, command=self.remove_all_liabilitys)
        self.B3.place(x=30, y=300)
        self.B4 = Button(buttons_frame, text='View Selected liability\'s Details', width=25,
                         command=self.view_liability_details)
        self.B4.place(x=30, y=350)

        self.B6 = Button(buttons_frame, text='Convert liabilityto a sentence', width=25,
                         command=self.selected_liability_to_words)
        self.B6.place(x=30, y=400)

        palette.apply_to_button(self.B1, 'active')
        palette.apply_to_button(self.B2, 'active')
        palette.apply_to_button(self.B3, 'active')
        palette.apply_to_button(self.B4, 'active')
        palette.apply_to_button(self.B5, 'active')
        palette.apply_to_button(self.B6, 'active')
        palette.apply_to_button(self.B7, 'active')
        palette.apply_to_button(self.B8, 'active')

        # Treeview Frame
        # Treeview Frame Setup - inside __init__
        self.table = ttk.Treeview(tree_frame, selectmode="browse",
                                  columns=(
                                      'ID', 'name', 'liability_type', 'serial_number', 'manufacturer', 'description',
                                      'location', 'status', 'owner', 'amount', 'date_of_purchase',
                                      'resale_value', 'depreciation', 'warranty_expiry', 'maintenance_schedule'),
                                  show="headings")

        # Scrollbars
        X_Scroller = Scrollbar(tree_frame, orient="horizontal", command=self.table.xview)
        Y_Scroller = Scrollbar(tree_frame, orient="vertical", command=self.table.yview)
        X_Scroller.pack(side="bottom", fill="x")
        Y_Scroller.pack(side="right", fill="y")
        self.table.config(xscrollcommand=X_Scroller.set, yscrollcommand=Y_Scroller.set)

        # Set column headings with user-friendly labels
        self.table.heading('ID', text='S No.', anchor="center")
        self.table.heading('name', text='Name', anchor="center")
        self.table.heading('liability_type', text='Liability Type', anchor="center")
        self.table.heading('serial_number', text='Serial Number', anchor="center")
        self.table.heading('manufacturer', text='Manufacturer', anchor="center")
        self.table.heading('description', text='Description', anchor="center")
        self.table.heading('location', text='Location', anchor="center")
        self.table.heading('status', text='Status', anchor="center")
        self.table.heading('owner', text='Owner', anchor="center")
        self.table.heading('amount', text='Purchase Price', anchor="center")
        self.table.heading('date_of_purchase', text='Date of Purchase', anchor="center")
        self.table.heading('resale_value', text='Resale Value', anchor="center")
        self.table.heading('depreciation', text='Depreciation', anchor="center")
        self.table.heading('warranty_expiry', text='Warranty Expiry', anchor="center")
        self.table.heading('maintenance_schedule', text='Maintenance Schedule', anchor="center")

        # Set column widths (fixed for clarity)
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('ID', width=50, stretch=NO)
        self.table.column('name', width=120, stretch=NO)
        self.table.column('liability_type', width=100, stretch=NO)
        self.table.column('serial_number', width=100, stretch=NO)
        self.table.column('manufacturer', width=100, stretch=NO)
        self.table.column('description', width=150, stretch=NO)
        self.table.column('location', width=100, stretch=NO)
        self.table.column('status', width=80, stretch=NO)
        self.table.column('owner', width=100, stretch=NO)
        self.table.column('amount', width=100, stretch=NO)
        self.table.column('date_of_purchase', width=120, stretch=NO)
        self.table.column('resale_value', width=100, stretch=NO)
        self.table.column('depreciation', width=100, stretch=NO)
        self.table.column('warranty_expiry', width=120, stretch=NO)
        self.table.column('maintenance_schedule', width=140, stretch=NO)

        self.table.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.palette.apply_to_treeview(self.table)

        self.list_all_liabilitys()
        # Functions
    def calculate_depreciation(self,amount, resale_value, useful_life):
        if useful_life <= 0 or amount <= 0 or resale_value < 0 or resale_value >= amount:
            return 0
        return round((amount - resale_value) / useful_life, 2)

    def on_calc_dep(self):
        pp = self.amount.get()
        rv = self.resale_value.get()
        lf = self.life.get()
        dep = self.calculate_depreciation(pp, rv, lf)
        self.depreciation.set(dep)

    def get_depreciation_schedule(self,amount, resale_value, useful_life):
        schedule = []
        start_value = amount
        depreciation = self.calculate_depreciation(amount, resale_value, useful_life)
        for year in range(1, useful_life + 1):
            end_value = start_value - depreciation
            if end_value < resale_value:
                end_value = resale_value
            schedule.append((year, start_value, depreciation, end_value))
            start_value = end_value
        return schedule

    def list_all_liabilitys(self):
        self.table.delete(*self.table.get_children())
        self.cursor = con.cursor()
        self.cursor.execute("SELECT * FROM capital_liability")
        rows=self.cursor.fetchall()
        self.cursor.execute("SELECT COUNT(*) FROM capital_liability")
        row_count = self.cursor.fetchone()[0]

        if row_count == 0:
            # Reset autoincrement
            # For MySQL:
            try:
                self.cursor.execute('ALTER TABLE capital_liability AUTO_INCREMENT = 1')
            except Exception as ex:
                print(f"Autoincrement reset failed: {ex}")
        for idx, row in enumerate(rows, start=1):
            # row assumed to be all columns starting from ID at row[0]
            # Insert row with idx as S No., then actual DB fields from row
            self.table.insert('', 'end', values=(idx,) + row[1:])
        self.cursor.close()
    def view_liability_details(self):
        global date_ent, creditor, desc, amnt, MoP
        if not self.table.selection():
            mb.showerror('No liabilityselected', 'Please select an liabilityfrom the self.table to view its details')
        current_selected_liability= self.table.item(self.table.focus())
        values = current_selected_liability['values']
        expenditure_date = datetime.strptime(values[1], '%Y-%m-%d %H:%M:%S').date()
        self.date_ent.set_date(expenditure_date)
        self.combo_rev.set(values[2])
        self.creditor.set(values[3])
        self.amnt.set(values[5])
        self.desc.set(values[4])
        self.MoP.set(values[6])

    def clear_fields(self):
        global desc, creditor, amnt, MoP, date
        today_date = datetime.now().date()
        self.desc.set('')
        self.creditor.set('')
        self.amnt.set(0.0)
        self.MoP.set('Cash'), self.date_ent.set_date(today_date)
        self.table.selection_remove(self.table.selection())
        self.combo_rev.set('')

    def remove_liability(self):
        if not self.table.selection():
            mb.showerror('No record selected!', 'Please select a record to delete!')
            return
        current_selected_liability= self.table.item(self.table.focus())
        values_selected = current_selected_liability['values']
        liability_id = int(values_selected[0])
        surety = mb.askyesno('Are you sure?',
                             f'Are you sure that you want to delete the record of {values_selected[2]}')
        if surety:
            cursor = con.cursor()
            cursor.execute('DELETE FROM capital_liability WHERE ID=%s', (liability_id,))
            con.commit()
            self.list_all_liabilitys()
            mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')
        self.list_all_liabilitys()

    def remove_all_liabilitys(self):
        surety = mb.askyesno('Are you sure?',
                             'Are you sure that you want to delete all the liabilityitems from the database?',
                             icon='warning')

        if surety:
            self.table.delete(*self.table.get_children())
            cursor = con.cursor()
            cursor.execute('DELETE FROM capital_liability')
            con.commit()

            self.clear_fields()
            self.list_all_liabilitys()
            mb.showinfo('All liabilitys deleted', 'All the liabilitys were successfully deleted')
        else:
            mb.showinfo('Ok then', 'The task was aborted and no liabilitywas deleted!')

    def add_another_liability(self):
        subwin = Toplevel(self.root)  # ✅ Child window
        subwin.geometry("600x600")
        subwin.resizable(0, 0)
        subwin.title("Additional details")
        palette = Color_Palette()
        palette.apply_to_window(subwin)

        # Serial Number
        serial_number_label = Label(subwin, text="Serial Number:")
        serial_number_label.place(x=50, y=60)
        palette.apply_to_label(serial_number_label, 'active')

        serial_number_entry = Entry(subwin, textvariable=self.serial_number_var, width=30)
        serial_number_entry.place(x=400, y=60)
        palette.apply_to_entry(serial_number_entry, 'active')

        # Manufacturer
        manufacturer_label = Label(subwin, text="Manufacturer:")
        manufacturer_label.place(x=50, y=100)
        palette.apply_to_label(manufacturer_label, 'active')

        manufacturer_entry = Entry(subwin, textvariable=self.manufacturer_var, width=30)
        manufacturer_entry.place(x=400, y=100)
        palette.apply_to_entry(manufacturer_entry, 'active')

        # Description
        description_label = Label(subwin, text="Description:")
        description_label.place(x=50, y=140)
        palette.apply_to_label(description_label, 'active')

        description_entry = Entry(subwin, textvariable=self.description_var, width=30)
        description_entry.place(x=400, y=140)
        palette.apply_to_entry(description_entry, 'active')

        # Location
        location_label = Label(subwin, text="Location:")
        location_label.place(x=50, y=180)
        palette.apply_to_label(location_label, 'active')

        location_entry = Entry(subwin, textvariable=self.location_var, width=30)
        location_entry.place(x=400, y=180)
        palette.apply_to_entry(location_entry, 'active')

        # Status
        status_label = Label(subwin, text="Status:")
        status_label.place(x=50, y=220)
        palette.apply_to_label(status_label, 'active')

        status_entry = Entry(subwin, textvariable=self.status_var, width=30)
        status_entry.place(x=400, y=220)
        palette.apply_to_entry(status_entry, 'active')

        # Owner
        owner_label = Label(subwin, text="Owner:")
        owner_label.place(x=50, y=260)
        palette.apply_to_label(owner_label, 'active')

        owner_entry = Entry(subwin, textvariable=self.owner_var, width=30)
        owner_entry.place(x=400, y=260)
        palette.apply_to_entry(owner_entry, 'active')

        # Warranty Expiry
        warranty_expiry_label = Label(subwin, text="Warranty Expiry (YYYY-MM-DD):")
        warranty_expiry_label.place(x=50, y=300)
        palette.apply_to_label(warranty_expiry_label, 'active')

        warranty_expiry_entry = Entry(subwin, textvariable=self.warranty_expiry_var, width=30)
        warranty_expiry_entry.place(x=400, y=300)
        palette.apply_to_entry(warranty_expiry_entry, 'active')

        # Maintenance Schedule
        maintenance_schedule_label = Label(subwin, text="Maintenance Schedule (YYYY-MM-DD):")
        maintenance_schedule_label.place(x=50, y=340)
        palette.apply_to_label(maintenance_schedule_label, 'active')

        maintenance_schedule_entry = Entry(subwin, textvariable=self.maintenance_schedule_var, width=30)
        maintenance_schedule_entry.place(x=400, y=340)
        palette.apply_to_entry(maintenance_schedule_entry, 'active')

        # -------------------- SUBMIT BUTTON --------------------
        def submit_additional_details():
            # Collect values from entry widgets
            serial_number = serial_number_entry.get()
            manufacturer = manufacturer_entry.get()
            description = description_entry.get()
            location = location_entry.get()
            status = status_entry.get()
            owner = owner_entry.get()
            warranty_expiry = warranty_expiry_entry.get()
            maintenance_schedule = maintenance_schedule_entry.get()

            # Main form values
            name = self.combo_rev.get()
            liability_type = self.combo_rev.get()
            amount = self.amount.get()
            resale_value = self.resale_value.get() or 0.0
            date_of_purchase = self.date_ent.get_date()
            useful_life = self.life.get()

            if not all([name, liability_type, amount, date_of_purchase, useful_life]):
                mb.showwarning('Fields empty!', "Please fill all the required fields.")
                return

            depreciation = self.calculate_depreciation(amount, resale_value, useful_life)

            try:
                cursor = con.cursor()
                cursor.execute('''
                    INSERT INTO liability (
                        name, liability_type, serial_number, manufacturer, description,
                        location, status, owner, amount, date_of_purchase,
                        resale_value, depreciation, warranty_expiry, maintenance_schedule
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    name, liability_type, serial_number, manufacturer, description,
                    location, status, owner, amount, date_of_purchase,
                    resale_value, depreciation, warranty_expiry, maintenance_schedule
                ))
                con.commit()
                self.clear_fields()
                self.list_all_liabilitys()
                mb.showinfo('liability added', 'The liability details have been saved!')
                subwin.destroy()
            except Exception as ex:
                mb.showerror('Database error', f'Could not add liability: {ex}')

        submit_button = Button(subwin, text="Submit", command=submit_additional_details)
        submit_button.place(x=300, y=550)
        palette.apply_to_window(subwin)  # optional if you want styling for button too

        self.list_all_liabilitys()

    def edit_liability(self):
        def edit_existing_liability():
            global date, amnt, desc, creditor, MoP
            current_selected_liability= self.table.item(self.table.focus())
            contents = current_selected_liability['values']
            cursor = con.cursor()
            cursor.execute(
                'UPDATE liability_tracker SET Date = %s, category=%s,liability=%s,creditor =%s, Description = %s, Amount = %s, ModeOfPayment = %s WHERE ID = %s',
                (self.date_ent.get_date(), self.combo_rev.get(), self.creditor.get(),
                 self.desc.get(), self.amnt.get(), self.MoP.get(), contents[0]))
            con.commit()
            self.clear_fields()
            self.list_all_liabilitys()

            mb.showinfo('Data edited', 'We have updated the data and stored in the database as you wanted')
            edit_btn.destroy()
            return

        if not self.table.selection():
            mb.showerror('No liabilityselected!',
                         'You have not selected any liabilityin the self.table for us to edit; please do that!')
            return

        self.view_liability_details()
        edit_btn = Button(self.data_entry_frame, text='Edit liability', width=30, command=edit_existing_liability)
        edit_btn.place(x=10, y=475)

    def selected_liability_to_words(self):

        if not self.table.selection():
            mb.showerror('No liabilityselected!', 'Please select an liabilityfrom the self.table for us to read')
            return
        current_selected_liability= self.table.item(self.table.focus())
        values = current_selected_liability['values']
        message = f'Your liabilitycan be read like: \n"You received {values[4]} from {values[3]} for {values[2]} on {values[1]} via {values[6]}"'
        mb.showinfo('Here\'s how to read your liability', message)

    def liability_to_words_before_adding(self):
        global date, desc, amnt, creditor, MoP

        if not date or not desc or not amnt or not creditor or not MoP:
            mb.showerror('Incomplete data', 'The data is incomplete, meaning fill all the fields first!')

        message = f'Your liabilitycan be read like: \n"You received {amnt.get()} from {creditor.get()} for {desc.get()} on {date.get_date()} via {MoP.get()}"'

        add_question = mb.askyesno('Read your record like: ', f'{message}\n\nShould I add it to the database?')

        if add_question:
            self.add_another_liability()
        else:
            mb.showinfo('Ok', 'Please take your time to add this record')
    # Backgrounds and Fonts


if __name__ == "__main__":
    root = Tk()
    obj = liabilityClass(root)
    root.mainloop()