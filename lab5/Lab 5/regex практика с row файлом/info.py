import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

receipt_info = {
    "Филиал": re.search(r"Филиал\s+(.*?)\n", text).group(1),
    "БИН": re.search(r"БИН\s+(\d+)", text).group(1),
    "Касса": re.search(r"Касса\s+([\d-]+)", text).group(1),
    "Смена": re.search(r"Смена\s+(\d+)", text).group(1),
    "Порядковый номер чека": re.search(r"Порядковый номер чека №(\d+)", text).group(1),
    "Чек №": re.search(r"Чек №(\d+)", text).group(1),
    "Кассир": re.search(r"Кассир\s+(.*?)\n", text).group(1),
    "ИТОГО": re.search(r"ИТОГО:\s+([\d\s,]+)", text).group(1).replace(" ", ""),
    "Дата и время": re.search(r"Время:\s+([\d:. ]+)", text).group(1),
    "Адрес": re.search(r"г\.\s*[\w-]+,.*", text).group(0),
}

items_pattern = re.findall(
    r"(\d+)\.\n([\w\s\(\)%,-]+)\n(\d+,\d{2}) x ([\d\s,]+)\n([\d\s,]+)",
    text
)

receipt_info["Товары"] = [
    {
        "№": item[0],
        "Название": item[1].strip(),
        "Количество": item[2].replace(",", "."),
        "Цена за шт": item[3].replace(" ", "").replace(",", "."),
        "Сумма": item[4].replace(" ", "").replace(",", "."),
    }
    for item in items_pattern
]

print("\nИнформация о чеке:")
for key, value in receipt_info.items():
    if key == "Товары":
        print("\nТовары:")
        for product in value:
            print(f"{product['№']}. {product['Название']} - {product['Количество']} шт. x {product['Цена за шт']} = {product['Сумма']}")
    else:
        print(f"{key}: {value}")
