import json

# Чтение файла и удаление комментариев
with open("testing_data.txt", "r", encoding="utf-8") as file:
    result = file.readlines()

# Удаление строк, содержащих ```json и ```
nice_result = result[1:-1]


# Объединение строк в одну строку
topics_data = json.loads("".join(nice_result))

# Проверка корректности JSON
try:
    data = json.loads(topics_data)
    print("JSON is valid")
except json.JSONDecodeError as e:
    print(f"JSON is invalid: {e}")