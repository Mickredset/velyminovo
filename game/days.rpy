# days.rpy
# day2
label day2:
    scene 5

    "Вы легли спать"

    $ t = 2

    "Холодно"

    "Сейчас полночь"

    "Вы слышите за окном звуки Сарайки"

    show s normal at center

    s "Сарайка пришла!"

    scene

    show homed2 at fullscreen_shake

    stop music

    play music "audio/horror.mp3"

    $ renpy.pause(12)

    "Сарайка придёт"

    scene black

    "Вы захотели поесть солёные огурчики"

    "Вы спустились в погреб"

    stop music

    play sound "audio/shagi.ogg"

    $ renpy.pause(9)

    scene 0 at fullscreen_shake

    "git: Ошибка слияния"

    "Вы в чужом погребе"

    scene black

    "Вы проснулись. Это был сон"

    scene root

    show s normal at center

    show d normal at left

    s "Сегодня ночью Сарайка не приходила"

    d "Подождите..."

    d "Сарайка приходила к нам"

    $ renpy.open_url("https://velyminovo-game.vercel.app/tools/game.html")

    $ renpy.force_autosave()

    s "Я пошёл в огород"

    s "Я видел САРАЙКУ!"

    hide s normal

    d "Я тоже"

    "Вы пошли в погреб"

    python:
        print("Это кто то читает?")

    scene 6

    "В погребе соленья"

    if cellar_light == True:
        # свет включён
        scene 6
    else:
        # света нету
        scene 7

    stop music

    play sound "audio/sova.jgg"

    $ renpy.pause(22.0, hard=True)

    "Сарайка пришла"

    $ cellar_light = True

    scene 6

    $ t = 14

    "Вы достали банку с огурчиками и принесли их в дом"

    scene root

    "Вы октрыли банку"

    "Вы пошли в огород"

    scene 8

    s "Здравствуйте!"

    p "У вас тут огород?"

    s "Да"

    p "А бабушка эта!"

    scene home

    d "Это Сарайка"

    p "И что нам делать?"

    s "Надо запечатать Сарайку"

    d "Идём!"

    scene 10

    d "Мы пришли"

    show n normal at center

    show s normal at left

    show d normal at right

    n "Здравствуйте!"

    d "Здравствуйте!"

    p "Здравствуйте!"

    n "Сарайка дала мне деньги"

    n "Вы что хотите?"

    play sound "audio/horror.mp3"

    n "Сарайка уже пришла!"
    
    n "Это не Сарайка! Это слизни"

    n "Нет выхода"

    menu:
        "Идти дальше":
            $ strange += 1
            call attack

        "Идти назад":
            jump start    

    n "Это моя копия"

    n "Это была не я"

    n """
    В СНТ нашем страшные существа появились!
    Они у человека жизнь забирают
    Сарайка появилась из старого колодца
    Сарайка поглощает душу!
    Вы наверное слышали. Все погреба в нашем СНТ используют систему контроля версий. Кратко гит
    Когда вы кладёте в погреб соленья автоматически происходит коммит
    Можно отключить авто-коммит. Коммит это не только плюс. Вы можете взять из погреба, изменить местоположение
    Например: git commit -m "Новая банка" или git push
    Два человека могут взять 1 банку из своего погреба. И после git push в погребе пропадёт у всех только 1 банка
    У двух людей будет 2 банки. Сихронизация это! Можно из 1 банки в погребе сделать 2 на поверхности. Одну продать можно
    Так бесконечное количество раз делать можно. Из 1 банки можно сделать 100 банок
    В панели управление погребом есть консоль.
    Не хотите сихронизацию? Тогда: git remote remove origin
    Всё просто!
    Вы что хотите?
    """

    p "Остановить Сарайку"

    n "Лучше не надо"
    menu:
        "Оставить всё как есть":
            $ _main_menu = True
            call screen preferences
            "Вы уехали"
        "Пойти дальше":
            $ strange += 1
            n "Хорошо!"
            hide n normal
            show n fight

            n "Надо было бабушку послушать"

            s "Тут люди странные!"

            scene black

            call attack

    scene 11 at fullscreen_shake

    show s normal at left

    show d normal at right

    d "Бабушка бежит за нами!"

    play sound "audio/f.jgg"