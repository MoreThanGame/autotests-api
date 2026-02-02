import httpx
from clients.api_client import APIClient
from typing import TypedDict

class CreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserDict) -> httpx.Response:
        """ Метод выполняет создание пользователя
        :param request: Словарь с email, password и данными пользователя
        :return: Ответ от сервера в виду объекта httpx.Response """
        return self.post("/api/v1/users", json=request)