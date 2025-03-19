from datetime import datetime, timedelta
def yesterday_today_tomorrow():
    today = datetime.now()
    return today - timedelta(days=1), today, today + timedelta(days=1)

yesterday, today, tomorrow = yesterday_today_tomorrow()
print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)
