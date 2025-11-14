__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A window that displays a searchable table of all clients.

    This class extends LookupWindow and provides:
    - Loading client & account data from CSV files (using load_data)
    - Displaying each client in a table
      (client number, first name, last name, email)
    - Allowing the user to search using the lookup bar inherited
      from LookupWindow
    - Opening AccountDetailsWindow when a client row is double-clicked

    The window does not modify client or account data directly;
    updates are handled in AccountDetailsWindow and written to file
    through update_data().
    """

    def __init__(self):
        """Initialize the lookup window and load all client data."""
        super().__init__()
        self.clients, self.accounts = load_data()
        self.populate_table()

    # ------------------------------------------------------------
    def populate_table(self):
        """
        Populate the table with all loaded client records.

        Each row displays: client number, first name, last name, email.
        The table only displays data; it does not modify it.
        """
        self.account_table.setRowCount(len(self.clients))

        for row_index, client in enumerate(self.clients.values()):

            # Client Number
            self.account_table.setItem(
                row_index, 0, QTableWidgetItem(str(client.client_number))
            )

            # First Name
            self.account_table.setItem(
                row_index, 1, QTableWidgetItem(client.first_name)
            )

            # Last Name
            self.account_table.setItem(
                row_index, 2, QTableWidgetItem(client.last_name)
            )

            # Email
            self.account_table.setItem(
                row_index, 3, QTableWidgetItem(client.email_address)
            )

        self.account_table.resizeColumnsToContents()

    # ------------------------------------------------------------
    def handle_row_selected(self, row: int):
        """
        Triggered when the user double-clicks a row.

        Retrieves the client_number from the row and opens
        AccountDetailsWindow for the selected client.
        """
        item = self.account_table.item(row, 0)

        if item is None:
            QMessageBox.warning(self, "Selection Error", "No client selected.")
            return

        client_number = int(item.text())
        client = self.clients.get(client_number)

        if not client:
            QMessageBox.warning(self, "Error", "Client not found.")
            return

        # Open the account details window
        window = AccountDetailsWindow(client, self.accounts, update_data)
        window.exec()
