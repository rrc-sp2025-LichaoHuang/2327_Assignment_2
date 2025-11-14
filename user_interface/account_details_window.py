__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Signal
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    Dialog window that shows a single bank account and allows
    deposit/withdraw actions.
    """

    # Signal to ClientLookupWindow
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount):
        """
        Initialize the transaction window for a specific account.
        """
        super().__init__()

        # Original reference (actual account stored in dictionary)
        self.account = account

        # Working copy (all transactions modify this until Exit)
        self.working_account = copy.deepcopy(account)

        # Load UI display values
        self.load_account_details()

        # Connect buttons
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)

    # ------------------------------------------------------------
    def load_account_details(self):
        """Display account number and balance in the UI."""

        # account_number_label is a QLabel
        self.account_number_label.setText(str(self.working_account.account_number))

        # balance_label is a QLabel
        self.balance_label.setText(f"${self.working_account.balance:,.2f}")

        # Clear the transaction field every time window opens
        self.transaction_amount_edit.clear()

    # ------------------------------------------------------------
    def on_apply_transaction(self):
        """
        Handles both Deposit and Withdraw buttons.
        """

        sender = self.sender()

        # Read amount
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.information(self, "Invalid Input", "Amount must be numeric.")
            return

        if amount <= 0:
            QMessageBox.information(self, "Invalid Input", "Amount must be positive.")
            return

        # Apply deposit or withdraw on the working copy
        try:
            if sender == self.deposit_button:
                self.working_account.deposit(amount)
            elif sender == self.withdraw_button:
                self.working_account.withdraw(amount)
        except Exception as e:
            QMessageBox.information(self, "Transaction Error", str(e))
            return

        # Update displayed balance
        self.balance_label.setText(f"${self.working_account.balance:,.2f}")

        # Clear amount entry after transaction
        self.transaction_amount_edit.clear()

    # ------------------------------------------------------------
    def on_exit(self):
        """
        Save working balance back to the original BankAccount and close dialog.
        """

        # Calculate balance difference
        difference = self.working_account.balance - self.account.balance

        # Apply this change to the real account
        self.account.update_balance(difference)

        # Notify parent window
        self.balance_updated.emit(self.account)

        # Close the window
        self.close()