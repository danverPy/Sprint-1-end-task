import datetime as dt


class Records():
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()


class Calculator():
    def __init__(self, limit):
        self.limit = limit
        self.record = []

    def add_record(self, record):
        self.records.append(record)
    
    def get_today_stats(self):
        today = dt.date.today()
        total = sum(
            [
                record.amount for record in self.records
                if record.date == today
            ]
        )
        return total
    
    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=7)

        total = sum(
            [
                record.amount for record in self.records
                if week_ago <= record.date <= today
            ]
        )
        return total
    
    def today_remind(self)
        return self.limit - self.get_today_stats()
        
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.today_remind <= 0:
            return ('Хватит есть!')
        else:
            return (f'Сегодня можно съесть что-нибудь ещё,' 
                    'но с общей калорийностью не более {self.today_remind} кКал')


        