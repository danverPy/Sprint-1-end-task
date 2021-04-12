import datetime as dt


class Records():
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()


class Calculator():
    def __init__(self, limit):
        self.limit = limit
        