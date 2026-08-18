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

    s "Я видел САРАЙКУ!"