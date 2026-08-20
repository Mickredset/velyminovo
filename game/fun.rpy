# Экран загрузки с логикой внутри
screen fake_loading_screen(duration):
    modal True
    add Solid("#ffffff")

    # Внутренние переменные экрана для подсчета прогресса
    default current_time = 0.0
    # Перевод времени в проценты (от 0 до 100)
    default progress_val = 0

    # Таймер срабатывает каждые 0.05 сек для максимальной плавности
    timer 0.05 repeat True action [
        SetScreenVariable("current_time", current_time + 0.05),
        SetScreenVariable("progress_val", min(100, int((current_time / duration) * 100))),
        # Если время вышло — автоматически закрываем экран
        If(current_time >= duration, Return())
    ]

    # Визуальная часть (черный текст и полоса на белом фоне)
    vbox:
        align (0.5, 0.5)
        spacing 20

        bar:
            value progress_val
            range 100
            xsize 500
            ysize 30
            left_bar "#000000"   # Черный цвет заполнения
            right_bar "#e0e0e0"  # Серый цвет пустой полосы

        text "[progress_val]%":
            xalign 0.5
            color "#000000"      # Черный текст
            size 32

# Погреб
default cellar_light = False         # Свет (вкл/выкл)
default cellar_door_locked = True    # Дверь (заблокирована/разблокирована)
default cellar_temp = 4              # Текущая температура в градусах
init python:
    # Ограничители для температуры погреба (от -5 до +20)
    def change_temp(amount):
        store.cellar_temp = max(-5, min(20, store.cellar_temp + amount))
        renpy.restart_interaction()
screen cellar_remote():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        background "#1a1a24"
        
        vbox:
            spacing 25
            xsize 400
            
            # Шапка пульта
            text "ПУЛЬТ ПОГРЕБА Ц-04" align (0.5, 0.0) size 26 color "#00ffcc" bold True
            
            null height 10
            
            # 1. Управление освещением
            hbox:
                spacing 20
                text "Освещение внутри:" yalign 0.5 size 18 xsize 210
                textbutton ("ВКЛ" if cellar_light else "ВЫКЛ"):
                    yalign 0.5
                    action ToggleVariable("cellar_light")
                    style "remote_button"
            
            # 2. Управление блокировкой двери
            hbox:
                spacing 20
                text "Гермозатвор:" yalign 0.5 size 18 xsize 210
                textbutton ("ЗАБЛОК." if cellar_door_locked else "ОТКРЫТ"):
                    yalign 0.5
                    action ToggleVariable("cellar_door_locked")
                    style "remote_button"
            
            # 3. Термостат (заменили квадратные скобки на безопасные символы/текст)
            vbox:
                spacing 5
                text "Термоконтроль:" size 18
                hbox:
                    spacing 15
                    yalign 0.5
                    textbutton " - " action Function(change_temp, -1) style "remote_button"
                    
                    if cellar_temp > 12:
                        text "[cellar_temp] °C (КРИТ)" yalign 0.5 size 22 color "#ff3333" bold True
                    else:
                        text "[cellar_temp] °C" yalign 0.5 size 22 color "#ffffff"
                        
                    textbutton " + " action Function(change_temp, 1) style "remote_button"
            
            null height 15
            
            # Кнопка закрытия пульта
            textbutton "ЗАКРЫТЬ ТЕРМИНАЛ" action Hide("cellar_remote") align (0.5, 1.0) style "close_button"


# Простые стили для красивого отображения кнопок
style remote_button:
    background "#2d2d3d"
    hover_background "#00ffcc"
    padding (12, 8)
    
style remote_button_text:
    color "#ffffff"
    hover_color "#000000"
    size 16

style close_button:
    background "#4a1515"
    hover_background "#ff3333"
    padding (15, 10)

style close_button_text:
    color "#ffffff"
    bold True
    size 16
transform fullscreen_shake:
    # Центрируем и слегка увеличиваем картинку (1.05 = 5%), 
    # чтобы при тряске не были видны пустые края экрана
    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.05
    subpixel True
    
    # Цикл тряски (сдвиги влево-вправо, вверх-вниз)
    linear 0.05 xoffset 10 yoffset -10
    linear 0.05 xoffset -10 yoffset 10
    linear 0.05 xoffset 8 yoffset 8
    linear 0.05 xoffset -8 yoffset -8
    linear 0.05 xoffset 0 yoffset 0
    repeat

# Экран с полосой HP и кнопкой
screen attack_screen:
    # Полоса HP
    frame:
        xalign 0.5
        yalign 0.5
        xsize 520
        ysize 90
        background "#000"
        padding (10, 10)

        bar:
            value 100
            range 100
            xsize 500
            ysize 70
            left_bar Solid("#0f0")
            right_bar Solid("#300")
            thumb None

    # Кнопка ПРОДОЛЖИТЬ
    textbutton "ПРОДОЛЖИТЬ":
        xalign 0.5
        yalign 0.75
        text_size 35
        text_color "#fff"
        background "#f80"
        padding (40, 15)
        action Return(True)

# Сама атака
label attack:
    
    show screen attack_screen
    $ result = ui.interact()
    hide screen attack_screen
    
    # Звук удара
    play sound "audio/f.ogg"
    
    pause 3
    
    return