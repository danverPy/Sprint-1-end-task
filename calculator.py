import datetime as dt


class Record():
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
        self.records = []

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
    
    def today_remind(self):
        return self.limit - self.get_today_stats()
        
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.today_remind <= 0:
            return ('Хватит есть!')
        return ('Сегодня можно съесть что-нибудь ещё,' 
                f'но с общей калорийностью не более {self.today_remind} кКал')

class CashCalculator(Calculator):

    USD_RATE = 77.23
    EURO_RATE = 90.74

    def get_today_cash_remained(self, currency):
        cash_remained = self.today_remind()
        if cash_remained == 0:
            return 'Денег нет, держись'
        all_currencies ={
            'usd':(self.USD_RATE, 'USD'),
            'eur':(self.EURO_RATE, 'EUR'),
            'rub':(1.0, 'руб')
        }
        needed_currency = round(abs(cash_remained)/all_currencies[currency][0],2)
        name_needed_currency = all_currencies[currency][1]

        if cash_remained < 0:
            return f'Денег нет, держись: твой долг - {needed_currency}{name_needed_currency}'
        
        return f'На сегодня осталось {needed_currency}{name_needed_currency}'

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб
        