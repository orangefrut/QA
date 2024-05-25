import unittest

from BankAccount import BankAccount

# py -m unittest .\Tests.py
# py -m coverage report -m

class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.initial_balance = 2000
        self.account = BankAccount("Bank account 2024", self.initial_balance)

    def test_bank_account_initialization(self):
        # Arrange & Act
        account_name = self.account.name
        account_balance = self.account.balance
        # Assert
        self.assertEqual("Bank account 2024", account_name, 'error name')
        self.assertEqual(self.initial_balance, account_balance, 'error balance')

    def test_deposit_positive_amount_should_increase_balance(self):
        # Arrange
        deposit_amount = 500
        # Act
        self.account.deposit(deposit_amount)
        # Assert
        self.assertEqual(self.initial_balance + deposit_amount, self.account.balance, 'error right add')

    def test_deposit_negative_amount_should_raise_value_error(self):
        # Arrange
        deposit_amount = -100
        # Act & Assert
        with self.assertRaises(ValueError, msg='Сумма для депозита должна быть больше нуля'):
            self.account.deposit(deposit_amount)

    def test_withdraw_positive_amount_less_than_balance_should_decrease_balance(self):
        # Arrange
        withdraw_amount = 500
        # Act
        self.account.withdraw(withdraw_amount)
        # Assert
        self.assertEqual(self.initial_balance - withdraw_amount, self.account.balance, 'error incorrect amount after withdrawal')

    def test_withdraw_amount_more_than_balance_should_raise_value_error(self):
        # Arrange
        withdraw_amount = self.initial_balance + 500
        # Act & Assert
        with self.assertRaises(ValueError, msg='Недостаточно средств на счете'):
            self.account.withdraw(withdraw_amount)

    def test_withdraw_negative_amount_should_raise_value_error(self):
        # Arrange
        withdraw_amount = -500
        # Act & Assert
        with self.assertRaises(ValueError, msg='Сумма снятия должна быть >0'):
            self.account.withdraw(withdraw_amount)

    def test_transfer_valid_amount_should_decrease_sender_balance_and_increase_recipient_balance(self):
        # Arrange
        recipient = BankAccount("RecipientAccount")
        transfer_amount = 500
        # Act
        self.account.transfer(recipient, transfer_amount)
        # Assert
        self.assertEqual(self.initial_balance - transfer_amount, self.account.balance, "The sender's amount is incorrect")
        self.assertEqual(transfer_amount, recipient.balance, 'Recipient')

    def test_transfer_amount_more_than_balance_should_raise_value_error(self):
        # Arrange
        recipient = BankAccount("RecipientAccount")
        transfer_amount = self.initial_balance + 500
        # Act & Assert
        with self.assertRaises(ValueError, msg='Недостаточно средств на счете для перевода'):
            self.account.transfer(recipient, transfer_amount)

    def test_transfer_negative_amount_should_raise_value_error(self):
        # Arrange
        recipient = BankAccount("RecipientAccount")
        transfer_amount = -500
        # Act & Assert
        with self.assertRaises(ValueError, msg='Сумма перевода должна быть положительная'):
            self.account.transfer(recipient, transfer_amount)

    def test_add_interest_valid_rate_should_increase_balance(self):
        # Arrange
        interest_rate = 5
        # Act
        self.account.add_interest(interest_rate)
        expected_interest = self.initial_balance * interest_rate / 100
        # Assert
        self.assertEqual(self.initial_balance + expected_interest, self.account.balance, 'Incorrect accrual percent')

    def test_add_interest_negative_rate_should_raise_value_error(self):
        # Arrange
        interest_rate = -5
        # Act & Assert
        with self.assertRaises(ValueError, msg='Процент не может быть отрицательным'):
            self.account.add_interest(interest_rate)


    def test_history_should_record_all_transactions(self):
        # Arrange & Act
        self.account.deposit(500)
        self.account.withdraw(200)
        self.account.add_interest(5)
        # Assert
        self.assertEqual(3, len(self.account.history), 'error history')

