import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'vk1.a.zL396WXTDTTqyJmxoLrhQybrfdQdrJVPNsrOmHaz0Hy8K2DkXZzFRQShp_eSEuAf9UpTdikRUccktE18Y7p7PxIuW2OY6a4e5OO2zSiYmzmajiDzTZwJm_y1Bi3vUEGpoZg7OXPaLdnTI4oZr4nQw5TsLa0gAhZh20VHbkDoXn1EC075i8eTNsFQf3VwqO4UOPbSc6nzmnF6JTMkypYSTw'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # print('user_id: ', event.user_id)
        # print('msg_text: ', event.text)
        # print('date: ', event.datetime)
        msg = event.text
        user_id = event.user_id
        message_id = event.message_id

        if msg == 'Привет':
            vk.messages.send(user_id=user_id,random_id=message_id,message='Привет!')

