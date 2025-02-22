﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define r = Character('Руусаан', color="#FF4D00")

define k = Character('Клос', color="00693E")

define t = Character('Ти Рэн', color="#6A5ACD")

define i = Character('Саша-ситх', color="#256D7B")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:

    image bg hallway = "images/backgrounds/hallway.png"

    image pda = "images/ruusaan/pda.jpg"

# Игра начинается здесь:
label start:

    play music theforcetheme

    scene bg hallway

    show ruusaan happy

    r "Приветствую друг."

    r "Кажется мы не виделись уже много лет. После победы Ревана мы кое как сводили концы с концами."

    hide ruusaan

    show klos climsy

    k "Привет, привет, давно не виделись, действительно."

    t "Привет"

    i "Привет"

label meet_ruusaan:

    play music theforcetheme

    scene bg hallway

    show ruusaan happy

    "играет какая нибудь музыка для кантины"

    "Руусаан пьет эль, получает сообщение на свой кпк."

    hide ruusaan

menu:

    "Открыть КПК":
        jump open_pda

label open_pda:

    show pda at truecenter
    with fade

    "..."

    hide pda

label meet_klos:

    show klos climsy

    "хз где и как он начинает"

    hide klos

    return