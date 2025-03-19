from datetime import datetime, timedelta
def remove_microseconds():
    return datetime.now().replace(microsecond=0)

print("Текущая дата без микросекунд:", remove_microseconds())
