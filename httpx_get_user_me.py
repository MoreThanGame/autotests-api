import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login = {
    "email": "morethangame@example.com",
    "password": "string123"
}

# Выполняем запрос на аутентификацию
response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login)
response_data = response.json()

# Выводим полученные токены и получаем статус-код
print("Login response:", response_data)
print("Status Code:", response.status_code)

# Из полученных токенов забираем accessToken и создаем заголовки
access_payload = response_data["token"]["accessToken"]
headers = {
    "Authorization": f"Bearer {access_payload}"
}

# Передаем accessToken и получаем данные о пользователе и статус код ответа
user_data = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
access_response = user_data.json()

print(access_response)
print(user_data.status_code)