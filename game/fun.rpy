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
