init 1 python:
    import random
    import time

    def run_fake_loading():
        # Выбираем случайное время загрузки от 80 до 127 секунд
        total_time = random.randint(80, 127)
        
        # Шаг обновления (в секундах). Чем меньше, тем плавнее полоса.
        # 0.1 секунды обеспечит очень плавное движение
        step_time = 0.1
        steps = int(total_time / step_time)
        
        # Показываем экран, передавая начальный прогресс (0%)
        renpy.show_screen("fake_loading_screen", progress_val=0)
        renpy.with_statement(fade) # Плавное появление экрана

        for i in range(steps + 1):
            # Рассчитываем текущий процент от 0 до 100
            current_pct = int((i / float(steps)) * 100)
            
            # Обновляем аргумент на экране без его перезапуска
            renpy.show_screen("fake_loading_screen", progress_val=current_pct)
            
            # Обновляем интерфейс Ren'Py, чтобы игрок видел изменения
            renpy.restart_interaction()
            
            # Пауза перед следующим шагом
            time.sleep(step_time)
            
        # Прячем экран после завершения загрузки
        renpy.hide_screen("fake_loading_screen")
        renpy.with_statement(fade) # Плавное исчезновение
init 999 python:
    config.developer = True
    config.console = True

init -1 python:
    import math
    import random
    

    class AirHockeyDisplayable(renpy.Displayable):
        def __init__(self):
            super(AirHockeyDisplayable, self).__init__()
            
            # Размеры игрового поля
            self.width = 800
            self.height = 600
            
            # Параметры шайбы
            self.puck_x = 400.0
            self.puck_y = 300.0
            self.puck_vx = random.choice([-5.0, 5.0])
            self.puck_vy = random.choice([-3.0, 3.0])
            self.puck_radius = 15
            
            # Параметры биты игрока
            self.player_x = 400.0
            self.player_y = 550.0
            self.paddle_radius = 25
            
            # Параметры биты ИИ (Скорость 5.0 для оптимальной сложности)
            self.ai_x = 400.0
            self.ai_y = 50.0
            self.ai_speed = 5.0 
            
            # Настройки счета (Игра идет ровно до 9 очков)
            self.player_score = 0
            self.ai_score = 0
            self.winning_score = 9  
            self.winner = None

        def render(self, width, height, st, at):
            # Вся физика и логика рассчитывается здесь на каждом кадре (60 FPS)
            if self.winner is None:
                # Движение ИИ за шайбой на его половине поля
                if self.puck_y < self.height // 2:
                    if self.ai_x < self.puck_x: self.ai_x += self.ai_speed
                    elif self.ai_x > self.puck_x: self.ai_x -= self.ai_speed
                    if self.ai_y < self.puck_y: self.ai_y += self.ai_speed
                    elif self.ai_y > 100: self.ai_y -= self.ai_speed
                else:
                    # Возврат ИИ в оборону, если шайба у игрока
                    if self.ai_y > 50: self.ai_y -= self.ai_speed
                    if self.ai_x < 400: self.ai_x += self.ai_speed
                    elif self.ai_x > 400: self.ai_x -= self.ai_speed

                # Движение шайбы
                self.puck_x += self.puck_vx
                self.puck_y += self.puck_vy

                # Отскоки от левой и правой стенки
                if self.puck_x - self.puck_radius <= 0 or self.puck_x + self.puck_radius >= self.width:
                    self.puck_vx *= -1
                    self.puck_x = max(self.puck_radius, min(self.puck_x, self.width - self.puck_radius))

                # Проверка гола в верхние ворота (забил Игрок)
                if self.puck_y - self.puck_radius <= 0:
                    if 300 <= self.puck_x <= 500:
                        self.player_score += 1
                        self.check_goals()
                    else:
                        self.puck_vy *= -1
                        self.puck_y = self.puck_radius

                # Проверка гола в нижние ворота (забил ИИ)
                if self.puck_y + self.puck_radius >= self.height:
                    if 300 <= self.puck_x <= 500:
                        self.ai_score += 1
                        self.check_goals()
                    else:
                        self.puck_vy *= -1
                        self.puck_y = self.height - self.puck_radius

                # Рассчет столкновения шайбы с обеими битами
                self.handle_collision(self.player_x, self.player_y)
                self.handle_collision(self.ai_x, self.ai_y)

            # Рендеринг графики (отрисовка игрового стола)
            render = renpy.Render(self.width, self.height)
            canvas = render.canvas()
            
            # Фон и разметка
            canvas.rect("#1a1a1a", (0, 0, self.width, self.height))
            canvas.rect("#00ffff", (0, 0, self.width, self.height), 4)
            canvas.line("#00ffff", (0, self.height // 2), (self.width, self.height // 2), 2)
            
            # Ворота красные и синие
            canvas.rect("#ff0000", (300, 0, 200, 10))
            canvas.rect("#0000ff", (300, self.height - 10, 200, 10))
            
            # Отрисовка объектов
            canvas.circle("#0000ff", (int(self.player_x), int(self.player_y)), self.paddle_radius)
            canvas.circle("#ff0000", (int(self.ai_x), int(self.ai_y)), self.paddle_radius)
            canvas.circle("#ffffff", (int(self.puck_x), int(self.puck_y)), self.puck_radius)
            
            # Принудительное обновление экрана на следующем кадре
            renpy.redraw(self, 0.0)
            return render

        def event(self, ev, x, y, st):
            # Передача победителя в сюжет по завершению игры
            if self.winner is not None:
                return self.winner

            # Управление мышью (игрок двигается только на своей нижней половине)
            if 0 < x < self.width and self.height // 2 < y < self.height:
                self.player_x = float(x)
                self.player_y = float(y)
                
            # Проверка достижения лимита в 9 очков
            if self.player_score >= self.winning_score or self.ai_score >= self.winning_score:
                return self.winner

            raise renpy.IgnoreEvent()

        def handle_collision(self, paddle_x, paddle_y):
            # Физика упругого столкновения круглых тел
            dx = self.puck_x - paddle_x
            dy = self.puck_y - paddle_y
            distance = math.hypot(dx, dy)
            min_dist = self.puck_radius + self.paddle_radius
            
            if distance < min_dist:
                if distance == 0: distance = 1.0
                nx = dx / distance
                ny = dy / distance
                
                # Выталкивание шайбы во избежание залипания
                self.puck_x = paddle_x + nx * min_dist
                self.puck_y = paddle_y + ny * min_dist
                
                # Изменение вектора скорости шайбы и придание ускорения (+0.5)
                curr_speed = math.hypot(self.puck_vx, self.puck_vy)
                curr_speed = max(7.0, curr_speed + 0.5)
                
                self.puck_vx = nx * curr_speed
                self.puck_vy = ny * curr_speed

        def check_goals(self):
            # Перезапуск шайбы в центре поля после гола
            self.puck_x = 400.0
            self.puck_y = 300.0
            self.puck_vx = random.choice([-5.0, 5.0])
            self.puck_vy = random.choice([-3.0, 3.0])
            
            # Установка победителя при наборе 9 очков
            if self.player_score >= self.winning_score:
                self.winner = "player"
            elif self.ai_score >= self.winning_score:
                self.winner = "ai"
style top_window:
    # Наследуем базовые отступы интерфейса
    is window 
    # Жестко ставим окно наверх (0.0 — самый верх)
    yalign 0.0 
screen air_hockey_screen():
    modal True
    
    # Размещение поля игры по центру экрана новеллы
    add AirHockeyDisplayable() id "hockey" xalign 0.5 yalign 0.5
    
    # Получение динамического счета из игрового процесса
    default hockey_obj = renpy.get_displayable("air_hockey_screen", "hockey")

    # Музыка
    on "show" action [Stop("music"), Play("music", "audio/fight.mp3")]

    
    if hockey_obj:
        # Отображение счета ИИ (Красный, сверху слева)
        text "[hockey_obj.ai_score]" size 50 color "#ff0000" xcenter 150 ycenter 100
        
        # Отображение счета Игрока (Синий, снизу слева)
        text "[hockey_obj.player_score]" size 50 color "#0000ff" xcenter 150 ycenter 500
# Игра
init python:
    import os
    import sys
    if renpy.game.persistent.game_is_dead or os.path.exists(os.path.join(config.gamedir, "lock.txt")):
        os._exit(0) 
# Вы можете расположить сценарий своей игры в этом файле.
default t = 0
default gold = True
default strange = 0
# Определение персонажей игры.
define s = Character('Саша', color="#070707")
define p = Character('Антон', color="#44ff00")
define d = Character('Денис', color="#b9a828")
define e = Character('Елена', color="#ffea00")
define c = Character(_("Баба Нюра"), screen="say_top", color = "#0000ffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
image s normal = "images/sasha.png"
image e normal = "images/elena.png"
image d normal = "images/d.png"
image c normal = "images/c.png"
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
screen tea_selection_screen(flavors):
    modal True
    add Solid("#000000a0") 
    vbox:
        align (0.5, 0.4)
        spacing 30
        text "Какой чай вы выберете?" xalign 0.5 size 32
        grid 4 6:
            xalign 0.5
            spacing 15 
            for flavor in flavors:
                textbutton flavor:
                    xsize 300 
                    ysize 80
                    style "button"
                    text_style "button_text"
                    xpadding 10
                    ypadding 10
                    action Return(flavor)

screen status():
    vbox:
        xalign 0.95
        yalign 0.05
        spacing 5
        
        text "Температура: [t]" size 40 color "#000000" xalign 1.0

# Игра начинается здесь:
label start:

    scene home

    show s normal

    s "Здравствуйте!"

    p "Привет!"

    e "Здравствуйте!"

    show e normal at left

    s "Беда у нас!"

    p "Какая?"
    hide s normal

    show d normal at right

    d "Электричество часто оключают"

    d "Днём очень жарко, а ночью очень холодно"

    $ t = 26

    show screen status

    s "Git не открывается!"

    show s normal

    menu:
        "Проверить судьбу":
            $ strange += 1
            s "Хорошо"
            $ temp = renpy.random.choice(["тигр фокусник", "сова на скакалке", "панда медетирует"])

            s "Вам выпала карта: [temp]"
        "Не проверять":
            s "Понятно"

    s "У нас по улицам ходят люди" 

    scene horror

    play music "audio/horror.mp3"

    s "Опять оно пришло"

    window hide

    $ renpy.pause(6.0, hard=True)

    window show

    scene homen

    s "Это Сарайка"

    stop music

    play music "audio/menu.mp3"

    show e normal at center

    show s normal at left

    show d normal at right

    e "Надо заходить в дом"

    scene home0

    p "А кто такая Сарайка?"

    d "У нас в деревне кто то отравил старый колодец"

    d "Из этого колодца вылезла Сарайка"

    d "Это существо не может проходить сквозь стены"

    d "Но если есть маленькое отверстие не больше одного"

    e "То существо кушает людей"

    $ t =  22

    p "Давай те в хоккей!"

    s "Я согласен"

    menu:
        "Сыграть в аир хоккей":
            $ air_hockey_game = AirHockeyDisplayable()

            $ result = renpy.call_screen("air_hockey_screen")

            if result == "player":
                s "Вы победили"
            else:
                "Саша победил"

        "Не играть (для истины)":
            s "Надо выпить чай"
            $ strange += 1


    p "Идём пить чай"

    scene root

    show s normal at center

    s "Выбирайте чай!"

    stop music

    play music "audio/fon.mp3"

    python:
        tea_flavors = [
            "Лемон Спарк", "Экзотик Опунция", "Блюберри Найтс", "Классик Брекфаст",
            "Роуз Пайнберри", "Тропикал Таррагон", "Вайлдберри Ройбош", "Эрл Грей Фэнтази",
            "Кристмас Мистери", "Барбери Гарден", "Рич Камомайл", "Флаинг Драгон",
            "Кениан Санрайз", "Гранд Фрут", "Грин Мелисса", "Куинс Джинджер",
            "Мэджик Юньнань", "Голден Цейлон", "Саммер Букет", "Уайт Линден",
            "Жасмин Дрим", "Спринг Мелоди", "Фестив Грейп", "Каррант энд Минт"
        ]

    call screen tea_selection_screen(tea_flavors)

    $ chosen_tea = _return    

    $ strange += 1

    s "Хороший чай!"

    p "Я выбрал [chosen_tea]"

    $ random_duration = renpy.random.randint(80, 127)

    call screen fake_loading_screen(duration=random_duration) with fade

    $ renpy.force_autosave()

    $ renpy.save("checkpoint_1", "Установка завершена")

    if not renpy.can_load("checkpoint_1"):
        $ renpy.quit()

    scene well

    p "Такой например"

    scene root

    show d normal at right

    show s normal at left

    s "В нашем колодце вода чистая"

    s "В нашем колодце воды очень много"

    s "Ночью на улице выходить нельзя"

    p "Почему?"

    d "Сарайка придёт"

    stop music

    play sound "audio/k.ogg"

    s "Кто мяукает!"

    p "Это не кот"

    d "И не кошка"

    e "Быстро в погреб!"

    scene black

    play sound "audio/shagi.ogg"

    p "Тут только я с тобой"

    d "Я тоже тут"
    
    d "Где вы?"

    scene pogreb

    s "Это не наш погреб!"

    play sound "audio/dver.mp3"

    $ renpy.pause(6)
    
    show c normal at center

    c "Здравствуйте!"

    p "Вы кто?"

    c "Я Анна"

    c "Вы хотели спуститься в свой погреб"

    c "Ваш погреб находиться в другой ветке"

    c "Произошло слияние"

    c "Вы не успели"

    p "И что теперь делать?"

    c "Вам нужно сделать запрос на слияние"

    play sound "audio/k.ogg"

    $ renpy.pause(6)

    p "Что это?"

    c "Выхода из этого погреба нету"

    c "Есть один!"

    c "Иди за мной!"

    menu:
        "Идти":
            "Вы пошли"
            $ strange += 1
        "Не идти":
            c "Твоё дело!"
            $ renpy.quit()

    scene black

    play sound "audio/shagi.ogg"

    $ renpy.pause(6)

    scene homed

    c "Мы вышли из погреба!"

    p "Как мне вернуться домой?"

    play sond "audio/shagi.ogg"

    show saraika

    c "Думаешь я добрая бабшука?"

    play sound "audio/krik.ogg"

    p "Это Сарайка"

    c "С"

    c "А"

    c "Райка"

    c "Сарайка"

    scene horror

    play sound "audio/krik.mp3"

    $ renpy.pause(8)

    stop sound

    stop music

    scene 0

    show c normal

    c "Это не я! Это Сарайка была"

    play music "audio/fon.mp3"

    p "Как отсюда выход найти?"

    c "Надо вызвать лифт"

    p "Лифт в погребе?"

    c "Да прям в погребе"

    python hide:
        # Открываем файл из папки game
        with renpy.file("dialog/plan.dialog") as f:
            # Читаем содержимое и декодируем в UTF-8
            file_content = f.read().decode("utf-8")
            
            # Сохраняем текст в глобальное хранилище store,
            # чтобы Ren'Py увидел переменную снаружи этого блока
            store.character_text = file_content.strip()

    c "[character_text]"


    hide  screen status

    p "Понятно"

    p "Как вы тут живёте?"

    scene 2

    p "Вот и лифт"

    scene 1

    c "Внучёк! Набери пожалуйста воду из колодца"

    "Вы набрали воду из колодца"

    scene homed2

    c "Спасибо!"

    c "Муравейник получил воду"

    c "Идите в подвал!"

    scene 3

    "Похоже бабушка ушла и заперла вас в погребе"

    stop music

    play sound "audio/horror.mp3"

    c "Что ты сделаешь?"

    c "Скоро тебя есть будем"

    menu:
        "Идти направо":
            "Вы пошли"

            show c normal

            c "Похоже ты внучёк будешь пельменями"

            $ main_menu = True

            c "Ну что"

            c "Давай"

            $ renpy.show_screen("load")
            
            $ renpy.quit()

        "Идти налево":
            $ strange += 1
            "Вы пошли и нашли выход"

    scene 4

    "Вы пошли по тропинке"

    scene home

    show d normal at center

    show s normal at left

    s "Здравствуйте! А где вы так долго были?"

    s "Мы в погребе спрятались от Сарайки"
    
    play music "audio/menu.mp3"                 

    p "Я встретил Бабушку Настю"

    p "Она хотела меня съесть"

    s "Так она 2 года назад умерла"           
    return
