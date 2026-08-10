# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Саша', color="#070707")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
image s normal = "images/sasha.png"
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene home

    show s normal

    s "Здравствуйте!"

    return
