from vk_api.keyboard import VkKeyboard, VkKeyboardColor

start = VkKeyboard(one_time=False, inline=False)
start.add_button(label='Начать', color=VkKeyboardColor.POSITIVE)

keyboard_city_aprove = VkKeyboard(one_time=False, inline=True)
keyboard_city_aprove.add_button(label='Да', color=VkKeyboardColor.PRIMARY)
keyboard_city_aprove.add_button(label='Нет', color=VkKeyboardColor.PRIMARY)


main_menu = VkKeyboard(one_time=False, inline=False)
main_menu.add_button(label='Погода', color=VkKeyboardColor.PRIMARY)
main_menu.add_button(label='Пробка', color=VkKeyboardColor.PRIMARY)
main_menu.add_line()
main_menu.add_button(label='Афиша', color=VkKeyboardColor.PRIMARY)
main_menu.add_button(label='Валюта', color=VkKeyboardColor.PRIMARY)
main_menu.add_line()
main_menu.add_button(label='Изменить город', color=VkKeyboardColor.SECONDARY)



weather = VkKeyboard(one_time=False, inline=True)
weather.add_button(label='Погода на сегодня', color=VkKeyboardColor.PRIMARY)
weather.add_line()
weather.add_button(label='Погода на завтра', color=VkKeyboardColor.PRIMARY)


afisha = VkKeyboard(one_time=False, inline=True)
afisha.add_button(label='Афиша на сегодня', color=VkKeyboardColor.PRIMARY)
afisha.add_line()
afisha.add_button(label='Афиша на завтра', color=VkKeyboardColor.PRIMARY)







# # №1. Клавиатура с 3 кнопками: "показать всплывающее сообщение", "открыть URL" и изменить меню (свой собственный тип)
# keyboard_1 = VkKeyboard(one_time=False, inline=True)
# # pop-up кнопка
# keyboard_1.add_callback_button(label='Покажи pop-up сообщение', color=VkKeyboardColor.SECONDARY, payload={"type": "show_snackbar", "text": "Это исчезающее сообщение"})
# keyboard_1.add_line()
# # кнопка с URL
# keyboard_1.add_callback_button(label='Откртыть Url', color=VkKeyboardColor.POSITIVE, payload={"type": "open_link", "link": "https://vk.com/dev/bots_docs_5"})
# keyboard_1.add_line()
# # кнопка по открытию ВК-приложения
# keyboard_1.add_callback_button(label='Открыть приложение', color=VkKeyboardColor.NEGATIVE, payload={"type": "open_app", "app_id": 'APP_ID', "owner_id": 'OWNER_ID', "hash": "anything_data_100500"})
# keyboard_1.add_line()
# # кнопка переключения на 2ое меню
# keyboard_1.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY, payload={"type": "my_own_100500_type_edit"})

# # №2. Клавиатура с одной красной callback-кнопкой. Нажатие изменяет меню на предыдущее.
# keyboard_2 = VkKeyboard(one_time=False, inline=True)
# # кнопка переключения назад, на 1ое меню.
# keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"})

