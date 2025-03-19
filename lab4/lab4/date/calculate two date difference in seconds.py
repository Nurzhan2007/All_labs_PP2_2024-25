from datetime import datetime, timedelta

def difference_in_seconds(date1, date2):
    return abs((date2 - date1).total_seconds())

try:
    date1_str = input("Введите первую дату (YYYY-MM-DD HH:MM:SS): ")
    date2_str = input("Введите вторую дату (YYYY-MM-DD HH:MM:SS): ")

    date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

    print("Разница в секундах:", difference_in_seconds(date1, date2))
except ValueError:
    print("Ошибка: формат даты должен быть YYYY-MM-DD HH:MM:SS")
