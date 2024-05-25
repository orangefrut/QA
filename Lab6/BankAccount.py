class BankAccount:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = balance
        self._history = []

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        return self._history

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Нельзя внести сумму меньше нуля")
        self._balance += amount
        self._history.append(f"Счет: +{amount}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительная")
        self._balance -= amount
        self._history.append(f"Счет: -{amount}")

    def transfer(self, recipient, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительная")
        self._balance -= amount
        recipient.deposit(amount)
        self._history.append(f"Перевод: -{amount} -> {recipient.name}")

    def add_interest(self, rate):
        if rate <= 0:
            raise ValueError("Процент не может быть отрицательным")
        interest = self._balance * rate / 100
        self._balance += interest
        self._history.append(f"Начисление процентов: +{interest}")
