import requests

# URL вашого сервера
url = "http://127.0.0.1:8000/files/upload_file/"

# Шлях до файлу, який потрібно завантажити
file_path = "download.jfif"

# Параметри запиту
params = {
    "filename": "downloaded_image.jfif",  # Ім'я файлу на сервері
    "id_": 123  # Унікальний ідентифікатор запису
}

# Відкриття файлу та відправка POST-запиту
with open(file_path, "rb") as file:
    files = {"file": file}  # Передаємо файл
    response = requests.post(url, files=files, params=params)  # Параметри передаються через `params`

# Перевірка відповіді від сервера
if response.status_code == 200:
    print("Файл успішно завантажено:", response.json())
else:
    print("Помилка:", response.status_code, response.text)
