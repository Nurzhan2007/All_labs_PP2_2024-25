from datetime import datetime, timedelta

def subtract_five_days():
    return datetime.now() - timedelta(days=5)

print("Дата 5 дней назад:", subtract_five_days())
