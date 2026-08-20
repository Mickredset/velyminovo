# Floppa AI init
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
            $ quick_menu = False
            $ _main_menu = True
            $ quick_menu = False
            $ renpy.full_restart() # Перезапускает игру в главное меню
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

    play sound "audio/f.ogg"

    $ renpy.pause (4)

    n "Пожалуйста! Не ходите!"

    $ t = 24

    call attack

    n "Я хочу вас остановить!"

    call attack

    n "Не надо!"

    n "Вспомните!"

    call res

    scene 11

    p "Бабушка! Тихо!"

    n "Правда?"

    call attack

    p "Бабушка отпустите нас!"

    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    call attack
    
    n """
    Сарайка будет бежать за вами!
    Там 3 замка! Первый замок это ключ! Я не знаю где он. Второй замок это кодовый! Третий это электрический замок.
    Вы можете отключить электричество и использовать магнит!
    """

    call attack

    call attack

    scene 12

    p "Люди тут ненормальные"

    play sound "audio/f.ogg"

    show stick:
        xalign -0.5 yalign 0.5 
        linear 3.0 xalign 0.5
        pause 3.0

    play sound "audio/f.ogg"    

    show stick:
        xalign -0.5 yalign 0.5 
        linear 3.0 xalign 0.5
        pause 3.0

    s "Это лифт!"

    play sound "audio/f.ogg"    

    show stick:
        xalign -0.5 yalign 0.5 
        linear 3.0 xalign 0.5
        pause 3.0

    hide stick

    jump pogreb2

label pogreb2:
    scene 13

    d "Мы в погребе!"

    show d normal at center

    show s normal at left

    p "Бабушка сумашедшая"

    n "Стоп!"

    n """
    Я̷͉͙̥͌̌ в̬̫̺̜̱ͣа̶̶͚̗̟͉̦̙̣̇͌ͮ͐ͥͫ̌с̶̶̫̣̳̞ н̶̸̠͙͔е̨͚͇̘̟͓͈̼ͨ о̵̰̍͌ͤс̨̧̫̥̺̮ͬт̶̧̫͚̗̍͛͋ͦ͐ͅа̲͚͎̝в̩͉̣͈ͯ͊͛̈л̴͇̼̖̪̜̘̤͋ю̷̸ͨͯͣ!͙ͯ͒ͨͫ͊̋̐ Н̵̅̃̋̾͗͒̐е̸̵͕͔͎̙̫̍̎͑͐͆ͅ и̵̫͉̺̯̾̏̉͐ͧд̵̶͕͓̼̒ͫ͆̾͋ͪͩͅи̧̝̳т̅̈ͣ̃е̧̨̹ͫ͂̿!̵̫͕̗͖ͯ 
    Я̞ в̹̍ͩк̭͍̀л̠ю̳̜ͥ̽ч̖̖̄у̥̯͗͒ с͙̠и̻͂ͤх̅р͍͋о̳ͣ̊н͔̹͗и̒͆з͌̈а̒ц̩͕ӥ̮ͭю͔!͚͗̉ Я̞ͪͫ с̺д͔̰ͮͨел͇̗ͯа̭͓̅ͬю́̄!͓͇
    """

    $ t = "Недоступно. Выполните: git init"

    s "Я нашёл консоль погреба!"

    s "Все погреба теперь одинаковые"

    s "Pull Request сделали"

    s "Бабка удалили репозиторий погреба. Этот погреб в котором мы сейчас не использует git."

    s "Нужно выйти!"

    s "git init"

    s "pogreb ssh -auto"

    s "Выходим!"

    scene black

    "Вы вышли из погреба"

    s "Наш погреб больше не привязан к общей системе"

    s "Уже вечер. Вы поужинали и пошли в погреб"

    scene 6

    "Вы взяли помидорчики"

    scene 5

    $ t = 6

    "Вы вернулись"

    e "Вы запечатали Сарайку?"

    p "Нет"

    s "Бабушка нас не пропускала"

    d "Бабушка сейчас у нас дома!"

    show d normal at center

    show s normal at left

    