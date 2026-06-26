# ui/main_window.py
"""
Simple and clean GUI for Personal Finance Manager.
"""

import FreeSimpleGUI as sg
from datetime import datetime
from services.finance_manager import FinanceManager


class MainWindow:
    """Main GUI Window"""

    def __init__(self):
        self.manager = FinanceManager()
        sg.theme('DarkAmber')
        self.window = None
        self.create_main_window()

    def create_main_window(self):
        layout = [
            [sg.Text("Personal Finance Manager", 
                    font=("Helvetica", 20, "bold"), 
                    justification="center", 
                    expand_x=True)],

            # Summary
            [sg.Frame("Financial Summary", [
                [sg.Text("Balance:", font=("Helvetica", 12))],
                [sg.Text("$0.00", key="-BALANCE-", font=("Helvetica", 18, "bold"), text_color="#4CAF50")],
                [sg.Text("Income: $0.00", key="-INCOME-", text_color="#4CAF50", font=("Helvetica", 11))],
                [sg.Text("Expense: $0.00", key="-EXPENSE-", text_color="#F44336", font=("Helvetica", 11))],
            ], expand_x=True)],

            [sg.HorizontalSeparator()],

            # Transactions Table
            [sg.Table(
                values=[],
                headings=["Date", "Type", "Title", "Category", "Amount"],
                key="-TABLE-",
                justification="left",
                auto_size_columns=True,
                num_rows=12,
                row_height=35,
                header_background_color="#37474F",
                background_color="#1E1E1E",
                text_color="white",
                enable_events=True,
                expand_x=True,
                expand_y=True
            )],

            [sg.HorizontalSeparator()],

            # Action Buttons
            [sg.Button("Add Category", key="-ADD_CATEGORY-", size=(15, 2), button_color="#2196F3"),
            sg.Button("Add Income", key="-ADD_INCOME-", size=(15, 2), button_color="#4CAF50"),
            sg.Button("Add Expense", key="-ADD_EXPENSE-", size=(15, 2), button_color="#F44336")],

            [sg.Button("Export to CSV", key="-EXPORT-", size=(15, 2), button_color="#FF9800"),
            sg.Button("Refresh", key="-REFRESH-", size=(15, 2)),
            sg.Button("Exit", key="-EXIT-", size=(15, 2), button_color="#9E9E9E")]
        ]

        self.window = sg.Window("Personal Finance Manager", 
                            layout, 
                            finalize=True, 
                            resizable=True,
                            element_justification="center")

        self.refresh_table()
        self.update_summary()

    def update_summary(self):
        balance = self.manager.get_balance()
        income = self.manager.get_total_income()
        expense = self.manager.get_total_expense()

        color = "#4CAF50" if balance >= 0 else "#F44336"
        self.window["-BALANCE-"].update(f"${balance:,.2f}", text_color=color)
        self.window["-INCOME-"].update(f"${income:,.2f}")
        self.window["-EXPENSE-"].update(f"${expense:,.2f}")

    def refresh_table(self):
        transactions = self.manager.get_all_transactions()
        table_data = [[t.date, t.type, t.title, t.category.name, t.get_display_amount()] for t in transactions]
        self.window["-TABLE-"].update(values=table_data)

    def add_category_window(self):
        layout = [
            [sg.Text("Add New Category", font=("Helvetica", 14, "bold"))],
            [sg.Text("Category Name:"), sg.Input(key="-CAT_NAME-", size=(30, 1))],
            [sg.Button("Add", key="-ADD_CAT-"), sg.Button("Cancel")]
        ]

        win = sg.Window("New Category", layout, modal=True)

        while True:
            event, values = win.read()
            if event in (sg.WIN_CLOSED, "Cancel"):
                break
            if event == "-ADD_CAT-":
                name = values["-CAT_NAME-"].strip()
                if name:
                    try:
                        self.manager.add_category(name)
                        sg.popup("Category added successfully!", title="Success")
                        break
                    except ValueError as e:
                        sg.popup_error(str(e))
                else:
                    sg.popup_error("Please enter a category name.")

        win.close()
        self.refresh_table()

    def add_transaction_window(self, trans_type):
        categories = self.manager.get_category_names()
        if not categories:
            sg.popup_error("No categories found!\nPlease add a category first.")
            return

        layout = [
            [sg.Text(f"Add New {trans_type}", font=("Helvetica", 14, "bold"))],
            [sg.Text("Date (dd/mm/yyyy):"), sg.Input(datetime.now().strftime("%d/%m/%Y"), key="-DATE-")],
            [sg.Text("Title:"), sg.Input(key="-TITLE-", size=(40, 1))],
            [sg.Text("Amount:"), sg.Input(key="-AMOUNT-", size=(15, 1))],
            [sg.Text("Category:"), sg.Combo(categories, key="-CATEGORY-", size=(35, 1), readonly=True)],
            [sg.Button(f"Add {trans_type}", key="-ADD-"), sg.Button("Cancel")]
        ]

        win = sg.Window(f"New {trans_type}", layout, modal=True)

        while True:
            event, values = win.read()
            if event in (sg.WIN_CLOSED, "Cancel"):
                break
            if event == "-ADD-":
                try:
                    self.manager.add_transaction(
                        title=values["-TITLE-"],
                        amount=values["-AMOUNT-"],
                        category_name=values["-CATEGORY-"],
                        trans_type=trans_type,
                        date_str=values["-DATE-"]
                    )
                    sg.popup(f"{trans_type} added successfully!", title="Success")
                    break
                except ValueError as e:
                    sg.popup_error(str(e))

        win.close()
        self.refresh_table()
        self.update_summary()

    def run(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "-EXIT-"):
                break

            if event == "-ADD_CATEGORY-":
                self.add_category_window()
            elif event == "-ADD_INCOME-":
                self.add_transaction_window("Income")
            elif event == "-ADD_EXPENSE-":
                self.add_transaction_window("Expense")
            elif event == "-EXPORT-":
                try:
                    path = self.manager.export_to_csv()
                    sg.popup(f"Export completed!\nFile saved in:\n{path}")
                except Exception as e:
                    sg.popup_error(f"Export failed: {e}")
            elif event == "-REFRESH-":
                self.refresh_table()
                self.update_summary()

        self.window.close()


# ====================== START ======================
if __name__ == "__main__":
    app = MainWindow()
    app.run()