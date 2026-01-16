import datetime

from pywin.framework.editor.configui import paletteVGA
from datetime import datetime, date as DateClass
from conn import *
from tkcalendar import DateEntry

from tkinter import *
import tkinter.messagebox as mb
import tkinter.ttk as ttk
from color_palette import *
from datetime import *

class Expenses:
    def __init__(self,root):

        self.cursor = con.cursor()


        # Initializing the GUI window
        palette = Color_Palette()
        palette.apply_to_window(root)
        root.title('Expense Tracker')
        root.geometry("1350x700+110+80")
        Label(root, text='EXPENSE TRACKER').pack(side="top", fill="x")


        # StringVar and DoubleVar variables
        self.desc = StringVar()
        self.amnt = DoubleVar()
        self.payee = StringVar()
        self.MoP = StringVar(value='Cash')

        # Frames
        self.data_entry_frame = Frame(root)
        palette.apply_to_window(self.data_entry_frame)
        self.data_entry_frame.place(x=0, y=30, relheight=0.95, relwidth=0.25)
        buttons_frame = Frame(root)
        palette.apply_to_window(buttons_frame)
        buttons_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.21)
        tree_frame = Frame(root)
        tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)
        palette.apply_to_window(tree_frame)

        # Data Entry Frame

        self.L0 = Label(self.data_entry_frame, text="Expenses", font=("times new roman", 15, "bold"), bg="Indigo", fg="white")
        self.L0.pack(side="top", fill="x")
       # palette.apply_to_label(self.L0)
        self.L1=Label(self.data_entry_frame, text='Date (M/DD/YY) :', )
        self.L1.place(x=10, y=50)
        self.date_ent = DateEntry(self.data_entry_frame, date=datetime.now().date())
        self.date_ent.place(x=160, y=50)

        self.cat_l=Label(self.data_entry_frame, text="Category:        ")
        self.cat_l.place(x=10, y=100)
        palette.apply_to_label(self.cat_l)

        cursor = con.cursor()
        cursor.execute("SELECT CategoryName FROM ExpenseCategories")
        self.all_categories = [row[0] for row in cursor.fetchall()]
        cursor.close()
        self.combo_cat = ttk.Combobox(self.data_entry_frame, state="normal", values=self.all_categories, style="Custom.TCombobox")
        self.combo_cat.place(x=120, y=100, width=200, height=28)

        self.expen_l=Label(self.data_entry_frame, text="Expenses:        ")
        self.expen_l.place(x=10, y=150)
        palette.apply_to_label(self.expen_l)

        self.combo_expen = ttk.Combobox(self.data_entry_frame, state="normal",style="Custom.TCombobox")
        self.combo_expen.place(x=120, y=150, width=200, height=28)


        def update_expenses(event=None):
            selected_category = self.combo_cat.get()

            cursor = con.cursor()
            cursor.execute(
                "SELECT ExpenseID, ExpenseName, Description FROM expenses WHERE categoryName = %s",
                (selected_category,)
            )
            expenses = cursor.fetchall()
            cursor.close()
            self.all_expenses = []
            self.product_dict = {}

            for ex_id, ex_name, desc in expenses:
                self.all_expenses.append({'ex_id': ex_id,'ex_name':ex_name, 'desc': desc})
                self.product_dict[ex_id] = {'ex_name':desc,'desc': desc}
            all_product_names = [ex_name['ex_name'] for ex_name in self.all_expenses]
            self.combo_expen['values'] = all_product_names

            self.selected_product = self.combo_expen.get()
            if all_product_names:
                self.combo_expen['values'] = all_product_names
            else:
                self.combo_expen.set('')

        self.combo_cat.bind('<<ComboboxSelected>>', update_expenses)

        self.L3=Label(self.data_entry_frame, text='Description           :' )
        self.L3.place(x=10,y=225)
        self.ent_desc=Entry(self.data_entry_frame, width=31, textvariable=self.desc)
        self.ent_desc.place(x=10, y=250)

        self.L4=Label(self.data_entry_frame, text='Amount\t             :',)
        self.L4.place(x=10, y=300)
        self.ent_amnt=Entry(self.data_entry_frame, width=14, textvariable=self.amnt)
        self.ent_amnt.place(x=170, y=305)


        self.L5=Label(self.data_entry_frame, text='Mode of Payment:')
        self.L5.place(x=10,y=250)
        self.L5.place(x=10, y=430)
        palette.apply_to_label(self.L1, 'active')
        palette.apply_to_label(self.L3, 'active')
        palette.apply_to_label(self.L4, 'active')
        palette.apply_to_label(self.L5, 'active')


        self.dd1 = OptionMenu(self.data_entry_frame, self.MoP,*['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay'])
        self.dd1.place(x=170, y=425)
        self.dd1.configure(width=10)
        self.B7=Button(self.data_entry_frame, text='Add expense', command=self.add_another_expense, width=30)
        self.B7.place(x=10, y=515)
        self.B8=(Button(self.data_entry_frame, text='Convert to words before adding'))
        self.B8.place(x=10, y=570)
        # Buttons' Frame
        self.B1=Button(buttons_frame, text='Delete Expense', width=25,command=self.remove_expense)
        self.B1.place(x=30, y=5)
        self.B2=(Button(buttons_frame, text='Clear Fields in DataEntry Frame', width=25,command=self.clear_fields))
        self.B2.place(x=335, y=5)
        self.B3=Button(buttons_frame, text='Delete All Expenses', width=25,command=self.remove_all_expenses)
        self.B3.place(x=640, y=5)
        self.B4=Button(buttons_frame, text='View Selected Expense\'s Details', width=25,command=self.view_expense_details)
        self.B4.place(x=30, y=65)
        self.B5=Button(buttons_frame, text='Edit Selected Expense', command=self.edit_expense,width=25,)
        self.B5.place(x=335, y=65)
        self.B6=Button(buttons_frame, text='Convert Expense to a sentence',width=25,command=self.selected_expense_to_words)
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
                             columns=('ID', 'Date', 'categories','expenses','Description', 'Amount', 'Mode of Payment','Created At'))
        X_Scroller = Scrollbar(self.table, orient="horizontal", command=self.table.xview)
        Y_Scroller = Scrollbar(self.table, orient="vertical", command=self.table.yview)
        X_Scroller.pack(side="bottom", fill="x")
        Y_Scroller.pack(side="right", fill="y")
        self.table.config(yscrollcommand=Y_Scroller.set, xscrollcommand=X_Scroller.set)
        self.table.heading('ID', text='S No.', anchor="center")
        self.table.heading('Date', text='Date', anchor="center")
        self.table.heading('categories', text='Category', anchor="center")
        self.table.heading('expenses', text='Expense', anchor="center")
        self.table.heading('Description', text='Description', anchor="center")
        self.table.heading('Amount', text='Amount', anchor="center")
        self.table.heading('Mode of Payment', text='Mode of Payment', anchor="center")
        self.table.heading('Created At', text='Created At', anchor="center")
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', width=50, stretch=NO)
        self.table.column('#2', width=95, stretch=NO)  # Date column
        self.table.column('#3', width=160, stretch=NO)  # category column
        self.table.column('#4', width=160, stretch=NO)  # description column
        self.table.column('#5', width=125, stretch=NO)  #amount col
        self.table.column('#6', width=105, stretch=NO)# Mode of Payment column
        self.table.column('#7', width=105, stretch=NO)
        self.table.place(relx=0, y=0, relheight=1, relwidth=1)
        palette.apply_to_treeview(self.table)
        self.list_all_expenses()
        # Functions
    def list_all_expenses(self):
      self.table.delete(*self.table.get_children())
      self.cursor=con.cursor()
      self.cursor.execute('SELECT * FROM ExpenseTracker')
      rows = self.cursor.fetchall()
      for idx, row in enumerate(rows,start=1):
          row_v=(idx,)+row[1:]
          self.table.insert('', "end", values=row_v)

    def view_expense_details(self):
        if not self.table.selection():
            mb.showerror('No expense selected', 'Please select an expense from the table to view its details')
            return

        current_selected_expense = self.table.item(self.table.focus())
        values = current_selected_expense['values']

        raw_date = values[1]

        if raw_date is None:
            mb.showerror('Invalid data', 'Selected expense has no valid date stored')
            return

        # If raw_date is already datetime or date object
        if isinstance(raw_date, (datetime, DateClass)):
            expenditure_date = raw_date.date() if isinstance(raw_date, datetime) else raw_date
        else:
            # Assume string, parse using known format
            try:
                expenditure_date = datetime.strptime(raw_date, '%Y-%m-%d %H:%M:%S').date()
            except ValueError:
                try:
                    # Try alternate format if time portion missing
                    expenditure_date = datetime.strptime(raw_date, '%Y-%m-%d').date()
                except Exception as e:
                    mb.showerror('Date parsing error', f"Could not parse date: {raw_date}\n{e}")
                    return

        self.date_ent.set_date(expenditure_date)
        self.combo_cat.set(values[2])
        self.combo_expen.set(values[3])
        
        self.desc.set(values[4])
        self.amnt.set(values[6])
        self.MoP.set(values[7])

    def clear_fields(self):
      global desc,  amnt, MoP, date
      today_date = datetime.now().date()
      self.desc.set('')  ; self.amnt.set(0.0) ; self.MoP.set('Cash'), self.date_ent.set_date(today_date)
      self.table.selection_remove(self.table.selection())
      self.combo_cat.set('')
      self.combo_expen.set('')


    def remove_expense(self):
      if not self.table.selection():
         mb.showerror('No record selected!', 'Please select a record to delete!')
         return
      current_selected_expense = self.table.item(self.table.focus())
      values_selected = current_selected_expense['values']
      expense_id = int(values_selected[0])
      surety = mb.askyesno('Are you sure?', f'Are you sure that you want to delete the record of {values_selected[2]}')
      if surety:

          self.cursor.execute('DELETE FROM ExpenseTracker WHERE ID=%s', (expense_id,))
          con.commit()
          self.list_all_expenses()
          mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')
      self.list_all_expenses()

    def remove_all_expenses(self):
      surety = mb.askyesno('Are you sure?', 'Are you sure that you want to delete all the expense items from the database?', icon='warning')

      if surety:
         self.table.delete(*self.table.get_children())
         self.cursor.execute('DELETE FROM ExpenseTracker')
         con.commit()

         self.clear_fields()
         self.list_all_expenses()
         mb.showinfo('All Expenses deleted', 'All the expenses were successfully deleted')
      else:
         mb.showinfo('Ok then', 'The task was aborted and no expense was deleted!')


    def add_another_expense(self):
          date=self.date_ent.get_date()
          category=self.combo_cat.get()
          expense=self.combo_expen.get()
          desc=self.desc.get()
          amnt=self.amnt.get()
          MoP=self.MoP.get()
          self.cursor.execute('SELECT COUNT(*) FROM ExpenseTracker')
          row_count = self.cursor.fetchone()[0]
          if row_count == 0:
              # Reset autoincrement
              # For MySQL:
              try:
                  self.cursor.execute('ALTER TABLE ExpenseTracker AUTO_INCREMENT = 1')
              except Exception as ex:
                  print(f"Autoincrement reset failed: {ex}")
          if all([category,expense,desc,amnt,MoP]):
              cursor = con.cursor()
              cursor.execute(
                  'INSERT INTO ExpenseTracker (Date,category,expense,Description, Amount, ModeOfPayment,created_at ) VALUES (%s,%s,%s, %s, %s, %s,NOW())',
                  (date, category,expense,  desc, amnt, MoP)
              )
              con.commit()
              self.clear_fields()
              self.list_all_expenses()
              mb.showinfo('Expense added', 'The expense whose details you just entered has been added to the database')
          else:
              messagebox.showwarning('Fields empty!', "Please fill all the missing fields before pressing the add button!")
              self.list_all_expenses()

    def edit_expense(self):
        def edit_existing_expense():
            current_selected_expense = self.table.item(self.table.focus())
            if not current_selected_expense:
                mb.showerror('Error', 'No expense selected for editing')
                return

            contents = current_selected_expense['values']

            self.cursor.execute('''
                UPDATE ExpenseTracker 
                SET Date=%s, category=%s, expense=%s, Payee=%s, Description=%s, Amount=%s, ModeOfPayment=%s
                WHERE ID=%s
            ''', (
                self.date_ent.get_date(),
                self.combo_cat.get(),
                self.combo_expen.get(),
                self.payee.get(),
                self.desc.get(),
                self.amnt.get(),
                self.MoP.get(),
                contents[0]  # ID
            ))

            con.commit()  # ✅ FIXED (use global con instead of self.con)
            self.clear_fields()
            self.list_all_expenses()
            mb.showinfo('Data edited', 'The expense was updated successfully')
            # remove the extra button after saving
            edit_btn.destroy()

        if not self.table.selection():
            mb.showerror('No expense selected!', 'Please select an expense to edit first.')
            return

        # Populate the entry fields with the selected row
        self.view_expense_details()

        # Add the "Edit expense" button dynamically
        edit_btn = Button(self.data_entry_frame, text='Save Changes', width=30, command=edit_existing_expense)
        edit_btn.place(x=10, y=475)

    def selected_expense_to_words(self):


      if not self.table.selection():
         mb.showerror('No expense selected!', 'Please select an expense from the self.table for us to read')
         return

      current_selected_expense = self.table.item(self.table.focus())
      values = current_selected_expense['values']

      message = f'Your expense can be read like: \n"You paid {values[6]} to {values[4]} for {values[3]} on {values[1]} via {values[7]}"'

      mb.showinfo('Here\'s how to read your expense', message)


    def expense_to_words_before_adding(self):
      global date, desc, amnt,   MoP

      if not date or not desc or not amnt or not  MoP:
         mb.showerror('Incomplete data', 'The data is incomplete, meaning fill all the fields first!')

      message = f'Your expense can be read like: \n"You paid {amnt.get()}  for {desc.get()} on {date.get_date()} via {MoP.get()}"'

      add_question = mb.askyesno('Read your record like: ', f'{message}\n\nShould I add it to the database?')

      if add_question:
         self.add_another_expense()
      else:
         mb.showinfo('Ok', 'Please take your time to add this record')
    # Backgrounds and Fonts


    # Finalizing the GUI window
if __name__=="__main__":
    root=Tk()
    obj=Expenses(root)
    root.mainloop()
