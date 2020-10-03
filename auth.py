import vk_api
from vk_api.longpoll import VkLongPoll

login, password = "LOGIN", "PASSWORD"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)  # данные входа
vk_session.auth(token_only=True)  # аутентификация
session_api = vk_session.get_api()
long_poll = VkLongPoll(vk_session)