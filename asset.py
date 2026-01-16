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


class assetClass:
    def __init__(self, root):

        self.root = root
        self.palette=Color_Palette()
        palette = Color_Palette()
        self.root = root

        self.root.geometry("1350x700+110+80")
        self.root.title("Asset Management System")
        palette.apply_to_window(root)

        # StringVar and DoubleVar variables
        self.desc = StringVar()
        self.amnt = DoubleVar()
        self.debtor = StringVar()
        self.MoP = StringVar(value='Cash')
        self.purchase_price = DoubleVar()
        self.resale_value = DoubleVar()
        self.life = IntVar()

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
        self.L0 = Label(self.data_entry_frame, text="Assets", font=("Arial", 18, "bold"), bg="Indigo",
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

        self.cat_l = Label(self.data_entry_frame, text="Asset:        ")
        self.cat_l.place(x=50, y=50)
        palette.apply_to_label(self.cat_l,'active')

        self.cursor = con.cursor()
        self.cursor.execute("SELECT asset_name FROM asset_cat")
        self.all_asset= [row[0] for row in self.cursor.fetchall()]
        self.cursor.close()
        self.combo_rev = ttk.Combobox(self.data_entry_frame, state="normal", values=self.all_asset,
                                      style="Custom.TCombobox")
        self.combo_rev.place(x=120, y=50, width=200, height=28)

        """self.expen_l = Label(self.data_entry_frame, text="assets:        ")
        self.expen_l.place(x=10, y=150)
        palette.apply_to_label(self.expen_l)

        self.combo_expen = ttk.Combobox(self.data_entry_frame, state="normal", style="Custom.TCombobox")
        self.combo_expen.place(x=120, y=150, width=200, height=28)"""

        self.L3 = Label(self.data_entry_frame, text='Description :')
        self.L3.place(x=350, y=50)
        self.ent_desc = Entry(self.data_entry_frame, width=31, textvariable=self.desc)
        self.ent_desc.place(x=480, y=55)

        self.L4 = Label(self.data_entry_frame, text='Purchase Price :', )
        self.L4.place(x=50, y=100)
        self.ent_amnt = Entry(self.data_entry_frame, width=14, textvariable=self.purchase_price)
        self.ent_amnt.place(x=200, y=105)

        self.L2 = Label(self.data_entry_frame, text='Debtor  :', )
        self.L2.place(x=700, y=50)
        self.ent_debtor = Entry(self.data_entry_frame, width=31, textvariable=self.debtor)
        self.ent_debtor.place(x=780, y=55)
        self.L5 = Label(self.data_entry_frame, text='Mode of Payment:')
        self.L5.place(x=1000, y=50)
        palette.apply_to_label(self.L1, 'active')
        palette.apply_to_label(self.L2, 'active')
        palette.apply_to_label(self.L3, 'active')
        palette.apply_to_label(self.L4, 'active')
        palette.apply_to_label(self.L5, 'active')

        self.dd1 = OptionMenu(self.data_entry_frame, self.MoP,
                              *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay'])
        self.dd1.place(x=1180, y=50)
        self.dd1.configure(width=10)






        Lr=Label(self.data_entry_frame, text='Resale Value:')
        Lr.place(x=310, y=100)
        palette.apply_to_label(Lr, 'active')
        Er=Entry(self.data_entry_frame, textvariable=self.resale_value)
        Er.place(x=440, y=105)
        palette.apply_to_entry(Er,'active')

        Lu=Label(self.data_entry_frame, text='Useful Life (years):')
        Lu.place(x=580, y=100)
        palette.apply_to_label(Lu, 'active')
        Eu=Entry(self.data_entry_frame, textvariable=self.life)
        Eu.place(x=750, y=105)
        palette.apply_to_entry(Eu,'active')


        self.depreciation = DoubleVar()
        Ld=Label(self.data_entry_frame, text='Annual Depreciation:')
        Ld.place(x=880, y=100)
        palette.apply_to_label(Ld, 'active')
        Ed=Entry(self.data_entry_frame, textvariable=self.depreciation, state='normal')
        Ed.place(x=1070, y=105)
        palette.apply_to_entry(Ed,'active')

        b9=Button(buttons_frame, text='Calculate Depreciation', command=self.on_calc_dep,width=25)

        palette.apply_to_button(b9,'active')

        # Buttons' Frame
        self.B7 = Button(buttons_frame, text='Add asset', command=self.add_another_asset, width=20)
        self.B7.place(x=30, y=0)
        self.B8 = (Button(buttons_frame, text='Convert to words before adding'))
        self.B8.place(x=30, y=50)
        self.B5 = Button(buttons_frame, text='Edit Selected asset', command=self.edit_asset, width=25, )
        self.B5.place(x=30, y=100)

        self.B2 = (Button(buttons_frame, text='Clear Fields in DataEntry Frame', width=25, command=self.clear_fields))
        self.B2.place(x=30, y=150)
        b9.place(x=30, y=200)
        self.B1 = Button(buttons_frame, text='Delete asset', width=25, command=self.remove_asset)
        self.B1.place(x=30, y=250)

        self.B3 = Button(buttons_frame, text='Delete All asset', width=25, command=self.remove_all_assets)
        self.B3.place(x=30, y=300)
        self.B4 = Button(buttons_frame, text='View Selected asset\'s Details', width=25,
                         command=self.view_asset_details)
        self.B4.place(x=30, y=350)

        self.B6 = Button(buttons_frame, text='Convert assetto a sentence', width=25,
                         command=self.selected_asset_to_words)
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
                                  columns=('ID', 'name', 'asset_type', 'serial_number', 'manufacturer', 'description',
                                           'location', 'status', 'owner', 'purchase_price', 'date_of_purchase',
                                           'resale_value', 'depreciation', 'warranty_expiry', 'maintenance_schedule'),
                                  show="headings")

        # Scrollbars as children of tree_frame
        X_Scroller = Scrollbar(tree_frame, orient="horizontal", command=self.table.xview)
        Y_Scroller = Scrollbar(tree_frame, orient="vertical", command=self.table.yview)
        X_Scroller.pack(side="bottom", fill="x")
        Y_Scroller.pack(side="right", fill="y")

        self.table.config(xscrollcommand=X_Scroller.set, yscrollcommand=Y_Scroller.set)

        # Define headings with user-friendly column names
        self.table.heading('ID', text='S No.', anchor="center")
        self.table.heading('name', text='Name', anchor="center")
        self.table.heading('asset_type', text='Asset Type', anchor="center")
        self.table.heading('serial_number', text='Serial Number', anchor="center")
        self.table.heading('manufacturer', text='Manufacturer', anchor="center")
        self.table.heading('description', text='Description', anchor="center")
        self.table.heading('location', text='Location', anchor="center")
        self.table.heading('status', text='Status', anchor="center")
        self.table.heading('owner', text='Owner', anchor="center")
        self.table.heading('purchase_price', text='Purchase Price', anchor="center")
        self.table.heading('date_of_purchase', text='Date of Purchase', anchor="center")
        self.table.heading('resale_value', text='Resale Value', anchor="center")
        self.table.heading('depreciation', text='Depreciation', anchor="center")
        self.table.heading('warranty_expiry', text='Warranty Expiry', anchor="center")
        self.table.heading('maintenance_schedule', text='Maintenance Schedule', anchor="center")

        # Set columns width and stretch options
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('ID', width=50, stretch=NO)
        self.table.column('name', width=120, stretch=NO)
        self.table.column('asset_type', width=100, stretch=NO)
        self.table.column('serial_number', width=100, stretch=NO)
        self.table.column('manufacturer', width=100, stretch=NO)
        self.table.column('description', width=150, stretch=NO)
        self.table.column('location', width=100, stretch=NO)
        self.table.column('status', width=80, stretch=NO)
        self.table.column('owner', width=100, stretch=NO)
        self.table.column('purchase_price', width=100, stretch=NO)
        self.table.column('date_of_purchase', width=120, stretch=NO)
        self.table.column('resale_value', width=100, stretch=NO)
        self.table.column('depreciation', width=100, stretch=NO)
        self.table.column('warranty_expiry', width=120, stretch=NO)
        self.table.column('maintenance_schedule', width=140, stretch=NO)

        self.table.place(relx=0, rely=0, relheight=1, relwidth=1)
        palette.apply_to_treeview(self.table)
        # Update the list_all_assets method to query and load these columns properly:


        self.list_all_assets()
        # Functions
    def calculate_depreciation(self,purchase_price, resale_value, useful_life):
        if useful_life <= 0 or purchase_price <= 0 or resale_value < 0 or resale_value >= purchase_price:
            return 0
        return round((purchase_price - resale_value) / useful_life, 2)

    def on_calc_dep(self):
        pp = self.purchase_price.get()
        rv = self.resale_value.get()
        lf = self.life.get()
        dep = self.calculate_depreciation(pp, rv, lf)
        self.depreciation.set(dep)

    def get_depreciation_schedule(self,purchase_price, resale_value, useful_life):
        schedule = []
        start_value = purchase_price
        depreciation = self.calculate_depreciation(purchase_price, resale_value, useful_life)
        for year in range(1, useful_life + 1):
            end_value = start_value - depreciation
            if end_value < resale_value:
                end_value = resale_value
            schedule.append((year, start_value, depreciation, end_value))
            start_value = end_value
        return schedule

    def list_all_assets(self):
        self.table.delete(*self.table.get_children())
        cursor = con.cursor()
        cursor.execute(
            'SELECT ID, name, asset_type, serial_number, manufacturer, description, location, status, owner, purchase_price, date_of_purchase, resale_value, depreciation, warranty_expiry, maintenance_schedule FROM asset'
        )
        rows = cursor.fetchall()
        print(f"Rows fetched: {len(rows)}")

        # Get row count with a proper query
        cursor.execute('SELECT COUNT(*) FROM asset')
        row_count = cursor.fetchone()[0]

        if row_count == 0:
            try:
                cursor.execute('ALTER TABLE asset AUTO_INCREMENT = 1')
                con.commit()
            except Exception as ex:
                print(f"Autoincrement reset failed: {ex}")

        for idx, row in enumerate(rows, start=1):
            self.table.insert('', 'end', values=(idx,) + row[1:])

        cursor.close()

    def view_asset_details(self):
        global date_ent, debtor, desc, amnt, MoP
        if not self.table.selection():
            mb.showerror('No assetselected', 'Please select an assetfrom the self.table to view its details')
        current_selected_asset= self.table.item(self.table.focus())
        values = current_selected_asset['values']
        expenditure_date = datetime.strptime(values[1], '%Y-%m-%d %H:%M:%S').date()
        self.date_ent.set_date(expenditure_date)
        self.combo_rev.set(values[2])
        self.debtor.set(values[3])
        self.amnt.set(values[5])
        self.desc.set(values[4])
        self.MoP.set(values[6])

    def clear_fields(self):
        global desc, debtor, amnt, MoP, date
        today_date = datetime.now().date()
        self.desc.set('')
        self.debtor.set('')
        self.amnt.set(0.0)
        self.MoP.set('Cash'), self.date_ent.set_date(today_date)
        self.table.selection_remove(self.table.selection())
        self.combo_rev.set('')

    def remove_asset(self):
        if not self.table.selection():
            mb.showerror('No record selected!', 'Please select a record to delete!')
            return
        current_selected_asset= self.table.item(self.table.focus())
        values_selected = current_selected_asset['values']
        asset_id = int(values_selected[0])
        surety = mb.askyesno('Are you sure?',
                             f'Are you sure that you want to delete the record of {values_selected[2]}')
        if surety:
            cursor = con.cursor()
            cursor.execute('DELETE FROM asset WHERE ID=%s', (asset_id,))
            con.commit()
            self.list_all_assets()
            mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')
        self.list_all_assets()

    def remove_all_assets(self):
        surety = mb.askyesno('Are you sure?',
                             'Are you sure that you want to delete all the assetitems from the database?',
                             icon='warning')

        if surety:
            self.table.delete(*self.table.get_children())
            cursor = con.cursor()
            cursor.execute('DELETE FROM asset')
            con.commit()

            self.clear_fields()
            self.list_all_assets()
            mb.showinfo('All assets deleted', 'All the assets were successfully deleted')
        else:
            mb.showinfo('Ok then', 'The task was aborted and no assetwas deleted!')

    def add_another_asset(self):
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
            asset_type = self.combo_rev.get()
            purchase_price = self.purchase_price.get()
            resale_value = self.resale_value.get() or 0.0
            date_of_purchase = self.date_ent.get_date()
            useful_life = self.life.get()

            if not all([name, asset_type, purchase_price, date_of_purchase, useful_life]):
                mb.showwarning('Fields empty!', "Please fill all the required fields.")
                return

            depreciation = self.calculate_depreciation(purchase_price, resale_value, useful_life)

            try:
                cursor = con.cursor()
                cursor.execute('''
                    INSERT INTO asset (
                        name, asset_type, serial_number, manufacturer, description,
                        location, status, owner, purchase_price, date_of_purchase,
                        resale_value, depreciation, warranty_expiry, maintenance_schedule
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    name, asset_type, serial_number, manufacturer, description,
                    location, status, owner, purchase_price, date_of_purchase,
                    resale_value, depreciation, warranty_expiry, maintenance_schedule
                ))
                con.commit()
                self.clear_fields()
                self.list_all_assets()
                mb.showinfo('Asset added', 'The asset details have been saved!')
                subwin.destroy()
            except Exception as ex:
                mb.showerror('Database error', f'Could not add asset: {ex}')

        submit_button = Button(subwin, text="Submit", command=submit_additional_details)
        submit_button.place(x=300, y=550)
        palette.apply_to_window(subwin)  # optional if you want styling for button too

        self.list_all_assets()

    def edit_asset(self):
        def edit_existing_asset():
            global date, amnt, desc, debtor, MoP
            current_selected_asset= self.table.item(self.table.focus())
            contents = current_selected_asset['values']
            cursor = con.cursor()
            cursor.execute(
                'UPDATE asset_tracker SET Date = %s, category=%s,asset=%s,debtor =%s, Description = %s, Amount = %s, ModeOfPayment = %s WHERE ID = %s',
                (self.date_ent.get_date(), self.combo_rev.get(), self.debtor.get(),
                 self.desc.get(), self.amnt.get(), self.MoP.get(), contents[0]))
            con.commit()
            self.clear_fields()
            self.list_all_assets()

            mb.showinfo('Data edited', 'We have updated the data and stored in the database as you wanted')
            edit_btn.destroy()
            return

        if not self.table.selection():
            mb.showerror('No assetselected!',
                         'You have not selected any assetin the self.table for us to edit; please do that!')
            return

        self.view_asset_details()
        edit_btn = Button(self.data_entry_frame, text='Edit asset', width=30, command=edit_existing_asset)
        edit_btn.place(x=10, y=475)

    def selected_asset_to_words(self):

        if not self.table.selection():
            mb.showerror('No assetselected!', 'Please select an assetfrom the self.table for us to read')
            return
        current_selected_asset= self.table.item(self.table.focus())
        values = current_selected_asset['values']
        message = f'Your assetcan be read like: \n"You received {values[4]} from {values[3]} for {values[2]} on {values[1]} via {values[6]}"'
        mb.showinfo('Here\'s how to read your asset', message)

    def asset_to_words_before_adding(self):
        global date, desc, amnt, debtor, MoP

        if not date or not desc or not amnt or not debtor or not MoP:
            mb.showerror('Incomplete data', 'The data is incomplete, meaning fill all the fields first!')

        message = f'Your assetcan be read like: \n"You received {amnt.get()} from {debtor.get()} for {desc.get()} on {date.get_date()} via {MoP.get()}"'

        add_question = mb.askyesno('Read your record like: ', f'{message}\n\nShould I add it to the database?')

        if add_question:
            self.add_another_asset()
        else:
            mb.showinfo('Ok', 'Please take your time to add this record')
    # Backgrounds and Fonts


if __name__ == "__main__":
    root = Tk()
    obj = assetClass(root)
    root.mainloop()