class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Date: {self.date}, Description: {self.description}, Amount: ${self.amount:.2f}"
    

    def to_csv_row(self):
        """
        Convert an Expense object into a list of values for CSV storage.
        """
        return [self.date, self.description, str(self.amount)]
    

    @classmethod
    def from_csv_row(cls, row):
        """
        Create an Expense object from a CSV row.
        Expected row format: [date, description, amount]
        """
        date, description, amount = row
        return cls(date, description, float(amount))