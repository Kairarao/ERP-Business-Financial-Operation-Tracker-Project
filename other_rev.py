from tkinter import *
from color_palette import *
from conn import *
import datetime
from tkcalendar import DateEntry
from datetime import *
import tkinter.messagebox as mb


class other_rev_class:
    def __init__(self, root):

        self.root = root
        palette = Color_Palette()
        self.root = root
        self.root.geometry("1350x700+110+80")
        self.root.title("Other Revenue")
        palette.apply_to_window(root)



        # StringVar and DoubleVar variables
        self.desc = StringVar()
        self.amnt = DoubleVar()
        self.payer = StringVar()
        self.MoP = StringVar(value='Cash')

        # Frames
        self.data_entry_frame = Frame(root)
        palette.apply_to_window(self.data_entry_frame)
        self.data_entry_frame.place(x=0, y=30, relheight=0.95, relwidth=0.25)
        self.L0 = Label(self.data_entry_frame, text="Other Revenue", font=("Arial", 18, "bold"), bg="Indigo",
                        fg="white")
        self.L0.place(x=50, y=5)
        buttons_frame = Frame(root)
        palette.apply_to_window(buttons_frame)
        buttons_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.21)
        tree_frame = Frame(root)
        tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)
        palette.apply_to_window(tree_frame)

        # Data Entry Frame
        self.L1 = Label(self.data_entry_frame, text='Date (M/DD/YY) :', )
        self.L1.place(x=10, y=50)
        self.date_ent = DateEntry(self.data_entry_frame, date=datetime.now().date())
        self.date_ent.place(x=160, y=50)

        self.cat_l = Label(self.data_entry_frame, text="Revenue Type:        ")
        self.cat_l.place(x=10, y=100)
        palette.apply_to_label(self.cat_l)

        self.cursor=con.cursor()
        self.cursor.execute("SELECT revenue_type FROM revenue")
        self.all_revenue = [row[0] for row in self.cursor.fetchall()]
        self.cursor.close()
        self.combo_rev = ttk.Combobox(self.data_entry_frame, state="normal", values=self.all_revenue,
                                      style="Custom.TCombobox")
        self.combo_rev.place(x=10, y=130, width=200, height=28)

        """self.expen_l = Label(self.data_entry_frame, text="revenues:        ")
        self.expen_l.place(x=10, y=150)
        palette.apply_to_label(self.expen_l)

        self.combo_expen = ttk.Combobox(self.data_entry_frame, state="normal", style="Custom.TCombobox")
        self.combo_expen.place(x=120, y=150, width=200, height=28)"""

        self.cat = Label(self.data_entry_frame, text="Trading A/C(1) or Profit A/C(2):        ")
        self.cat.place(x=10, y=150)
        palette.apply_to_label(self.cat)
        values=[1,2]
        self.category = ttk.Combobox(self.data_entry_frame, state="normal", values=values,
                                      style="Custom.TCombobox")
        self.category.place(x=10, y=180, width=200, height=28)

        self.L3 = Label(self.data_entry_frame, text='Description           :')
        self.L3.place(x=10, y=225)
        self.ent_desc = Entry(self.data_entry_frame, width=31, textvariable=self.desc)
        self.ent_desc.place(x=10, y=250)

        self.L4 = Label(self.data_entry_frame, text='Amount\t             :', )
        self.L4.place(x=10, y=300)
        self.ent_amnt = Entry(self.data_entry_frame, width=14, textvariable=self.amnt)
        self.ent_amnt.place(x=170, y=305)

        self.L2 = Label(self.data_entry_frame, text='Payer\t             :', )
        self.L2.place(x=10, y=345)
        self.ent_payer = Entry(self.data_entry_frame, width=31, textvariable=self.payer)
        self.ent_payer.place(x=10, y=370)
        self.L5 = Label(self.data_entry_frame, text='Mode of Payment:')
        self.L5.place(x=10, y=250)
        self.L5.place(x=10, y=430)
        palette.apply_to_label(self.L1, 'active')
        palette.apply_to_label(self.L2, 'active')
        palette.apply_to_label(self.L3, 'active')
        palette.apply_to_label(self.L4, 'active')
        palette.apply_to_label(self.L5, 'active')

        self.dd1 = OptionMenu(self.data_entry_frame, self.MoP,
                              *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay'])
        self.dd1.place(x=170, y=425)
        self.dd1.configure(width=10)
        self.B7 = Button(self.data_entry_frame, text='Add Revenue', command=self.add_another_revenue, width=30)
        self.B7.place(x=10, y=515)
        self.B8 = (Button(self.data_entry_frame, text='Convert to words before adding'))
        self.B8.place(x=10, y=570)
        # Buttons' Frame
        self.B1 = Button(buttons_frame, text='Delete Revenue', width=25, command=self.remove_revenue)
        self.B1.place(x=30, y=5)
        self.B2 = (Button(buttons_frame, text='Clear Fields in DataEntry Frame', width=25, command=self.clear_fields))
        self.B2.place(x=335, y=5)
        self.B3 = Button(buttons_frame, text='Delete All Revenue', width=25, command=self.remove_all_revenues)
        self.B3.place(x=640, y=5)
        self.B4 = Button(buttons_frame, text='View Selected Revenue\'s Details', width=25,
                         command=self.view_revenue_details)
        self.B4.place(x=30, y=65)
        self.B5 = Button(buttons_frame, text='Edit Selected Revenue', command=self.edit_revenue, width=25, )
        self.B5.place(x=335, y=65)
        self.B6 = Button(buttons_frame, text='Convert Revenue to a sentence', width=25,
                         command=self.selected_revenue_to_words)
        self.B6.place(x=640, y=65)

        palette.apply_to_button(self.B1, 'active')
        palette.apply_to_button(self.B2, 'active')
        palette.apply_to_button(self.B3, 'active')
        palette.apply_to_button(self.B4, 'active')
        palette.apply_to_button(self.B5, 'active')
        palette.apply_to_button(self.B6, 'active')
        palette.apply_to_button(self.B7, 'active')
        palette.apply_to_button(self.B8, 'active')

        # Treeview Frame
        self.table = ttk.Treeview(tree_frame, selectmode="browse",
                                  columns=('ID', 'Date', 'Revenue', 'Payer','Amount', 'Description',
                                           'Mode of Payment','created_at'), show="headings")
        X_Scroller = Scrollbar(self.table, orient="horizontal", command=self.table.xview)
        Y_Scroller = Scrollbar(self.table, orient="vertical", command=self.table.yview)
        X_Scroller.pack(side="bottom", fill="x")
        Y_Scroller.pack(side="right", fill="y")
        self.table.config(yscrollcommand=Y_Scroller.set, xscrollcommand=X_Scroller.set)
        self.table.heading('ID', text='S No.', anchor="center")
        self.table.heading('Date', text='Date', anchor="center")
        self.table.heading('Revenue', text='Revenue', anchor="center")
        self.table.heading('Payer', text='Payer', anchor="center")
        self.table.heading('Amount', text='Amount', anchor="center")
        self.table.heading('Description', text='Description', anchor="center")
        self.table.heading('Mode of Payment', text='Mode of Payment', anchor="center")
        self.table.heading('created_at', text='Created At', anchor="center")
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', width=50, stretch=NO)
        self.table.column('#2', width=95, stretch=NO)  # Date column
        self.table.column('#3', width=160, stretch=NO)  # category column
        self.table.column('#4', width=160, stretch=NO)  # description column
        self.table.column('#5', width=135, stretch=NO)  # payer column
        self.table.column('#6', width=125, stretch=NO)  # amount col
        self.table.column('#7', width=105, stretch=NO)  # Mode of Payment column
        self.table.place(relx=0, y=0, relheight=1, relwidth=1)
        palette.apply_to_treeview(self.table)
        self.list_all_revenues()
        # Functions

    def list_all_revenues(self):
        self.table.delete(*self.table.get_children())
        cursor = con.cursor()

        cursor.execute('SELECT * FROM revenue_tracker')
        rows = cursor.fetchall()

        cursor.execute('SELECT COUNT(*) FROM revenue_tracker')
        row_count = cursor.fetchone()[0]

        if row_count == 0:
            try:
                cursor.execute('ALTER TABLE revenue_tracker AUTO_INCREMENT = 1')
            except Exception as ex:
                print(f"Autoincrement reset failed: {ex}")

        for idx, row in enumerate(rows, start=1):
            row_v = (idx,) + row[1:]
            self.table.insert('', "end", values=row_v)

        cursor.close()

    def view_revenue_details(self):
        global date_ent, payer, desc, amnt, MoP
        if not self.table.selection():
            mb.showerror('No revenue selected', 'Please select an revenue from the self.table to view its details')
        current_selected_revenue = self.table.item(self.table.focus())
        values = current_selected_revenue['values']
        #expenditure_date = datetime.strptime(values[1], '%Y-%m-%d %H:%M:%S').date()
        #self.date_ent.set_date(expenditure_date)
        self.combo_rev.set(values[2])
        self.payer.set(values[3])
        self.amnt.set(values[4])
        self.desc.set(values[5])
        self.MoP.set(values[6])

    def clear_fields(self):
        global desc, payer, amnt, MoP, date
        today_date = datetime.now().date()
        self.desc.set('')
        self.payer.set('')
        self.amnt.set(0.0)
        self.MoP.set('Cash'), self.date_ent.set_date(today_date)
        self.table.selection_remove(self.table.selection())
        self.combo_rev.set('')
        

    def remove_revenue(self):
        if not self.table.selection():
            mb.showerror('No record selected!', 'Please select a record to delete!')
            return
        current_selected_revenue = self.table.item(self.table.focus())
        values_selected = current_selected_revenue['values']
        revenue_id = int(values_selected[0])
        surety = mb.askyesno('Are you sure?',f'Are you sure that you want to delete the record of {values_selected[2]}')
        if surety:
            cursor = con.cursor()
            cursor.execute('DELETE FROM revenue_tracker WHERE ID=%s', (revenue_id,))
            con.commit()
            self.list_all_revenues()
            mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')
        self.list_all_revenues()

    def remove_all_revenues(self):
        surety = mb.askyesno('Are you sure?',
                             'Are you sure that you want to delete all the revenue items from the database?',
                             icon='warning')

        if surety:
            self.table.delete(*self.table.get_children())
            self.cursor.execute('DELETE FROM revenue_tracker')
            con.commit()

            self.clear_fields()
            self.list_all_revenues()
            mb.showinfo('All revenues deleted', 'All the revenues were successfully deleted')
        else:
            mb.showinfo('Ok then', 'The task was aborted and no revenue was deleted!')

    def add_another_revenue(self):
        date = self.date_ent.get_date()
        revenue = self.combo_rev.get()
        payer = self.payer.get()
        desc = self.desc.get()
        amnt = self.amnt.get()
        MoP = self.MoP.get()
        category=self.category.get()

        if all([date, revenue, payer, desc, amnt, MoP]):
            cursor = con.cursor()
            cursor.execute(
                'INSERT INTO revenue_tracker(date, revenue_type, payer, amount, description, mop, created_at, category) VALUES (%s,%s,%s,%s,%s,%s,NOW(),%s)',
                (date, revenue, payer, amnt, desc, MoP,category))
            con.commit()
            cursor.close()

            self.clear_fields()
            self.list_all_revenues()
            mb.showinfo('Revenue added', 'The revenue details have been added to the database.')
        else:
            mb.showwarning('Fields empty!', "Please fill all missing fields before adding revenue!")

    def edit_revenue(self):
        def edit_existing_revenue():
            global date, amnt, desc, payer, MoP
            current_selected_revenue = self.table.item(self.table.focus())
            contents = current_selected_revenue['values']
            cursor = con.cursor()
            cursor.execute(
                'UPDATE revenue_tracker SET Date = %s, category=%s,payer =%s, Description = %s, Amount = %s, mop = %s WHERE ID = %s',
                (self.date_ent.get_date(), self.combo_rev.get(), self.payer.get(),
                 self.desc.get(), self.amnt.get(), self.MoP.get(), contents[0]))
            con.commit()
            self.clear_fields()
            self.list_all_revenues()

            mb.showinfo('Data edited', 'We have updated the data and stored in the database as you wanted')
            edit_btn.destroy()
            return

        if not self.table.selection():
            mb.showerror('No revenue selected!',
                         'You have not selected any revenue in the self.table for us to edit; please do that!')
            return

        self.view_revenue_details()
        edit_btn = Button(self.data_entry_frame, text='Edit revenue', width=30, command=edit_existing_revenue)
        edit_btn.place(x=10, y=475)


    def selected_revenue_to_words(self):

        if not self.table.selection():
            mb.showerror('No revenue selected!', 'Please select an revenue from the self.table for us to read')
            return
        current_selected_revenue = self.table.item(self.table.focus())
        values = current_selected_revenue['values']
        message = f'Your revenue can be read like: \n"You received {values[4]} from {values[3]} for {values[2]} on {values[1]} via {values[6]}"'
        mb.showinfo('Here\'s how to read your revenue', message)

    def revenue_to_words_before_adding(self):
        global date, desc, amnt, payer, MoP

        if not date or not desc or not amnt or not payer or not MoP:
            mb.showerror('Incomplete data', 'The data is incomplete, meaning fill all the fields first!')

        message = f'Your revenue can be read like: \n"You received {amnt.get()} from {payer.get()} for {desc.get()} on {date.get_date()} via {MoP.get()}"'

        add_question = mb.askyesno('Read your record like: ', f'{message}\n\nShould I add it to the database?')

        if add_question:
            self.add_another_revenue()
        else:
            mb.showinfo('Ok', 'Please take your time to add this record')
    # Backgrounds and Fonts


if __name__=="__main__":
    root=Tk()
    obj=other_rev_class(root)
    root.mainloop()