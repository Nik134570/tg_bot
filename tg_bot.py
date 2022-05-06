import random
import telebot
from telebot import types # для указание типов

# создание переменных хранящих информацию о пользователе
cto_ti = 0
login = 0 # логин
parol = 0 # пароль
search = 0 # поиск пользователя в базе
user_pred = "" # предпологаемый логин
parolchik = "" # предпологаемый пароль
user = "" # окончательный логин
login_vvod = 0 # ввод логина
parol_vvod = 0 # ввод пароля
based = [] # база
user_parol = "" # пароль пользователя
ab = [] # строка информации
registr = 0 # регистрация
stroka_basa = "" # строка информации 
cho_skasat = 0 
level = 1 # уровень
exp = 0 # количество опыта
user_hp = 10 # hp игрока на данный момент
user_damage = "1-2" # конечный дамаг игрока
user_crit_damage = 10 # крин урон
user_chance_crit = 10 # крит шанс
mob = "" # атакуемый враг
max_hp = 10 # максимальное hp игрока
hp_mob = 0 # hp врага на данный момент
points = 0 # количество не используемых поинтов
sword = "" # экпированный меч
sword_char = 0
brona = "" 
brona_char = 0
artefact = ""
artefact_char = 0

# инвентарь:
inventory = "0*" * 38
inventory = inventory[:-1]
inventory_swords = "0*0*0"
zel = "0*0*0"

predmet_craft = ""
chari = "0*0*0" # чары мечей
real_damage = "1-2" # дамаг игрока без меча
location = "" # локация в которой находится игрок

# создание строки информации
stroka_basa += str(cto_ti) + "/" + str(login) + "/" + str(parol) + "/"
stroka_basa += user_pred + "/" + parolchik + "/" + user + "/"
stroka_basa += str(login_vvod) + "/" + str(parol_vvod) + "/" + user_parol + "/" + str(registr)
stroka_basa += "/" + str(level) + "/" + str(exp)
stroka_basa += "/" + str(user_hp)+ "/" + str(user_damage) + "/" + str(user_crit_damage) + "/" + str(user_chance_crit)
stroka_basa += "/" + mob + "/" + str(hp_mob) + "/" + str(max_hp) + "/" + inventory + "/" + str(points)
stroka_basa += "/" + str(sword) + "/" + str(sword_char)
stroka_basa += "/" + str(brona) + "/" + str(brona_char)
stroka_basa += "/" + str(artefact) + "/" + str(artefact_char) + "/" + predmet_craft + "/" + inventory_swords + "/" + str(chari) + "/" + str(real_damage) + "/" + str(zel)+ "/" + str(location)

# словарь мечей
based_sword = {
                "🌳 Wooden sword 🌳": {"type": "sword", "damage": "125%", "craft": {"🌳 обычное дерево 🌳": 30, "🐿 шкура белки 🐿": 5}},
                "🐁 Rat sword 🐀": {"type": "sword", "damage": "140%", "craft": {"🐁 крысиный хвост 🐁": 100, "🐀 крысина шкура 🐀": 70, "🥚 яйцо (Lvl 1) 🥚": 30, "⛓ кусочек цепи ⛓": 10, "💰 мешок монет 💰": 1}},
                "🗿 Stone sword 🗿": {"type": "sword", "damage": "170%", "craft": {"🗿  обычный камень  🗿": 40, "⛓ кусочек цепи ⛓": 30, "🐺 клык волка 🐺": 5}}
}

# словарь врагов в локации лес
based_monstrs_of_prosstoles_vvod = {
                "🌳  Странный куст  🌳": {"type": "mining"},
                "🗿  Камень  🗿": {"type": "mining"},
                "🍂 старый пень 🍂": {"type": "mining"},
                "🦎  Обычная ящерица  🦎  (Lvl 1)": {"type": "default", "hp": 7, "damage": 1, "exp": 8},
                "🐿  Белка  🐿  (Lvl 1)": {"type": "default", "hp": 5, "damage": 2, "exp": 10},
                "🦝  Енот  🦝  (Lvl 2)": {"type": "default", "hp": 8, "damage": 3, "exp": 12},
                "Гигантский воробей 🗿  (Lvl 2)": {"type": "default", "hp": 15, "damage": 1, "exp": 13},
                "💉  Ядовитая крыса  💉  (Lvl 3)": {"type": "default", "hp": 5, "damage": 7, "exp": 18},
                "🐺  Белый волк  🐺  (Lvl 3)": {"type": "default", "hp": 10, "damage": 5, "exp": 22},
                "🕷  Лесной паук  🕷  (Lvl 5)": {"type": "default", "hp": 25, "damage": 6, "exp": 50},
                "🐉  Детеныш лесного дракона  🐉  (Lvl 10)": {"type": "default", "hp": 50, "damage": 10, "exp": 300},
                "Загадочный призрак  👻": {"type": "bonus", "type_of_bonus": "hp", "chance_to_positive_reaction": "30%", "positive_reaction": "+10hp", "neggative_reaction": "-10hp"}
}

# словарь врагов в локации озеро
based_monstrs_of_ozero_vvod = {
                "💧 мокрый камень 🗿": {"type": "mining"},
                "🐚 ракушка 🐚": {"type": "mining"},
                "⛈ электрический коралл ⛈": {"type": "mining"},
                "🌿 водоросли 🌿": {"type": "mining"},
                "🐟 рыба 🐟 (Lvl 1)": {"type": "default", "hp": 3, "damage": 1, "exp": 2},
                "🐠 аксололь 🦎 (Lvl 3)": {"type": "default", "hp": 8, "damage": 6, "exp": 10},
                "💧 водяной змей 🐍 (Lvl 15)": {"type": "default", "hp": 120, "damage": 20, "exp": 550}
}

# словарь всех врагов
based_monstrs_of_prosstoles = {
                "🌳  Странный куст  🌳": {"type": "mining"},
                "🗿  Камень  🗿": {"type": "mining"},
                "🍂 старый пень 🍂": {"type": "mining"},
                "🦎  Обычная ящерица  🦎  (Lvl 1)": {"type": "default", "hp": 7, "damage": 1, "exp": 8},
                "🐿  Белка  🐿  (Lvl 1)": {"type": "default", "hp": 5, "damage": 2, "exp": 10},
                "🦝  Енот  🦝  (Lvl 2)": {"type": "default", "hp": 8, "damage": 3, "exp": 12},
                "Гигантский воробей 🗿  (Lvl 2)": {"type": "default", "hp": 15, "damage": 1, "exp": 13},
                "💉  Ядовитая крыса  💉  (Lvl 3)": {"type": "default", "hp": 5, "damage": 7, "exp": 18},
                "🐺  Белый волк  🐺  (Lvl 3)": {"type": "default", "hp": 10, "damage": 5, "exp": 22},
                "🕷  Лесной паук  🕷  (Lvl 5)": {"type": "default", "hp": 25, "damage": 6, "exp": 50},
                "🐉  Детеныш лесного дракона  🐉  (Lvl 10)": {"type": "default", "hp": 50, "damage": 10, "exp": 300},
                "Загадочный призрак  👻": {"type": "bonus", "type_of_bonus": "hp", "chance_to_positive_reaction": "30%", "positive_reaction": "+10hp", "neggative_reaction": "-10hp"},
                "💧 мокрый камень 🗿": {"type": "mining"},
                "🐚 ракушка 🐚": {"type": "mining"},
                "⛈ электрический коралл ⛈": {"type": "mining"},
                "🌿 водоросли 🌿": {"type": "mining"},
                "🐟 рыба 🐟 (Lvl 1)": {"type": "default", "hp": 3, "damage": 1, "exp": 2},
                "🐠 аксололь 🦎 (Lvl 3)": {"type": "default", "hp": 8, "damage": 6, "exp": 10},
                "💧 водяной змей 🐍 (Lvl 15)": {"type": "default", "hp": 120, "damage": 20, "exp": 550}
}

# словарь предметов падающих с врагов
based_monstrs_of_prosstoles_loot = {
                "🦎  Обычная ящерица  🦎  (Lvl 1)": {"type": "default",
                        "loot1": "🦎 хвост ящерицы 🦎", "loot1_chance": "80%", "loot1_count": "2-4",
                        "loot3": "🍈 чешуя (F) 🍈", "loot3_chance": "60%", "loot3_count": "1-3",
                        "loot2": "🃏 игральный камень 🃏", "loot2_chance": "10%", "loot2_count": "1-1"
                },

                "🐿  Белка  🐿  (Lvl 1)": {"type": "default",
                        "loot2": "🌰 орех 🌰", "loot2_chance": "100%", "loot2_count": "10-25",
                        "loot1": "🐿 шкура белки 🐿", "loot1_chance": "70%", "loot1_count": "1-3"
                },

                "🦝  Енот  🦝  (Lvl 2)": {"type": "default",
                        "loot1": "⛓ кусочек цепи ⛓", "loot1_chance": "60%", "loot1_count": "1-2",
                        "loot2": "💰 мешок монет 💰", "loot2_chance": "20%", "loot2_count": "1-3",
                        "loot3": "⭐ звезда (F) ⭐", "loot3_chance": "15%", "loot3_count": "1-3"
                },

                "Гигантский воробей 🗿  (Lvl 2)": {"type": "default",
                        "loot2": "🌾 зерно 🌾", "loot2_chance": "100%", "loot2_count": "5-7",
                        "loot1": "🥚 яйцо (F) 🥚", "loot1_chance": "90%", "loot1_count": "1-10"
                },

                "💉  Ядовитая крыса  💉  (Lvl 3)": {"type": "default",
                        "loot1": "🐁 крысиный хвост 🐁", "loot1_chance": "90%", "loot1_count": "3-7",
                        "loot4": "🐀 крысина шкура 🐀", "loot4_chance": "60%", "loot4_count": "3-4",
                        "loot3": "🥀 ядовитая роза 🥀", "loot3_chance": "5%", "loot3_count": "1-4",
                        "loot2": "💉 колба яд-826 💉", "loot2_chance": "3%", "loot2_count": "1-1"
                },

                "🐺  Белый волк  🐺  (Lvl 3)": {"type": "default",
                        "loot2": "🥩 мясо 🥩", "loot2_chance": "90%", "loot2_count": "2-5",
                        "loot1": "🐺 клык волка 🐺", "loot1_chance": "30%", "loot1_count": "1-2",
                        "loot3": "⚪ белая сфера ⚪", "loot3_chance": "10%", "loot3_count": "1-1"
                },

                "🕷  Лесной паук  🕷  (Lvl 5)": {"type": "default",
                        "loot2": "🕸 паутинка 🕸", "loot2_chance": "90%", "loot2_count": "1-2",
                        "loot1": "🦗 обычный жучок 🦗", "loot1_chance": "40%", "loot1_count": "1-2",
                        "loot3": "⚫ черная сфера ⚫", "loot3_chance": "5%", "loot3_count": "1-1",
                        "loot4": "⭐ звезда (F+) ⭐", "loot4_chance": "0.3%", "loot4_count": "1-1",
                },

                "🌳  Странный куст  🌳": {"type": "mining",
                        "loot1": "🌳 обычное дерево 🌳", "loot1_chance": "100%", "loot1_count": "1-5",
                        "loot2": "🦗 обычный жучок 🦗", "loot2_chance": "10%", "loot2_count": "1-1"
                },

                "🗿  Камень  🗿": {"type": "mining",
                        "loot1": "🗿  обычный камень  🗿", "loot1_chance": "100%", "loot1_count": "1-3",
                        "loot2": "⛓ кусочек цепи ⛓", "loot2_chance": "20%", "loot2_count": "1-2"
                },

                "🍂 старый пень 🍂": {"type": "mining",
                        "loot1": "🌳 обычное дерево 🌳", "loot1_chance": "80%", "loot1_count": "1-2",
                        "loot2": "🍂 зачахшие листья удачи 🍂", "loot2_chance": "10%", "loot2_count": "2-3",
                        "loot3": "🕸 паутинка 🕸", "loot3_chance": "5%", "loot3_count": "1-1",
                        "loot4": "⭐ звезда (F+) ⭐", "loot4_chance": "0.012%", "loot4_count": "1-2"
                },

                "🐉  Детеныш лесного дракона  🐉  (Lvl 10)": {"type": "default",
                        "loot1": "🍈 чешуя (F+) 🍈", "loot1_chance": "100%", "loot1_count": "5-7",
                        "loot2": "💰 мешок монет 💰", "loot2_chance": "80%", "loot2_count": "2-3",
                        "loot5": "⭐ звезда (F+) ⭐", "loot5_chance": "32%", "loot5_count": "1-2",
                        "loot3": "🃏 игральный камень 🃏", "loot3_chance": "30%", "loot3_count": "1-3",
                        "loot4": "🐉 шкура дракона (F-) 🐉", "loot4_chance": "4%", "loot4_count": "1-1",
                        "loot6": "⭐ звезда (F++) ⭐", "loot6_chance": "0.02%", "loot6_count": "1-1"
                },

                "Загадочный призрак  👻": {"type": "bonus"},

                "💧 мокрый камень 🗿": {"type": "mining",
                        "loot3": "💧 капля 💧", "loot3_chance": "100%", "loot3_count": "5-10",
                        "loot1": "🗿  обычный камень  🗿", "loot1_chance": "80%", "loot1_count": "1-1",
                        "loot2": "⛓ кусочек цепи ⛓", "loot2_chance": "5%", "loot2_count": "1-1"
                },

                "🐚 ракушка 🐚": {"type": "mining",
                        "loot1": "🐚 ракушка 🐚", "loot1_chance": "100%", "loot1_count": "3-5",
                        "loot2": "💧 капля 💧", "loot2_chance": "10%", "loot2_count": "1-3"
                },

                "⛈ электрический коралл ⛈": {"type": "mining",
                        "loot1": "⭐ звезда (F) ⭐", "loot1_chance": "90%", "loot1_count": "2-3",
                        "loot2": "💧 капля 💧", "loot2_chance": "20%", "loot2_count": "1-3",
                        "loot3": "⚡ электрический камень ⚡", "loot3_chance": "1%", "loot3_count": "1-1"
                },

                "🌿 водоросли 🌿": {"type": "mining",
                        "loot1": "🟢 зеленые водоросли 🌿", "loot1_chance": "100%", "loot1_count": "1-2",
                        "loot2": "🔴 красные водоросли 🌿", "loot2_chance": "60%", "loot2_count": "1-1"
                },

                "🐟 рыба 🐟 (Lvl 1)": {"type": "default",
                        "loot1": "🐟 рыба 🐟", "loot1_chance": "100%", "loot1_count": "4-6",
                        "loot3": "🟢 зеленые водоросли 🌿", "loot3_chance": "30%", "loot3_count": "1-1"
                },

                "🐠 аксололь 🦎 (Lvl 3)": {"type": "default",
                        "loot3": "🐚 ракушка 🐚", "loot3_chance": "50%", "loot3_count": "1-3",
                        "loot1": "⭐ звезда (F+) ⭐", "loot1_chance": "10%", "loot1_count": "1-2"
                },

                "💧 водяной змей 🐍 (Lvl 15)": {"type": "default",
                        "loot1": "🐚 ракушка 🐚", "loot1_chance": "100%", "loot1_count": "7-20",
                        "loot2": "💧 капля 💧", "loot2_chance": "97%", "loot2_count": "10-30",
                        "loot3": "⭐ звезда (F+) ⭐", "loot3_chance": "90%", "loot3_count": "5-10",
                        "loot8": "💀 змеиный клык 🐍", "loot8_chance": "80%", "loot8_count": "4-5",
                        "loot4": "⭐ звезда (F++) ⭐", "loot4_chance": "40%", "loot4_count": "3-6",
                        "loot7": "🥀 ядовитая роза 🥀", "loot7_chance": "25%", "loot7_count": "2-6",
                        "loot5": "⭐ звезда (F+++) ⭐", "loot5_chance": "12%", "loot5_count": "1-2",
                        "loot6": "⭐ звезда (E-) ⭐", "loot6_chance": "5%", "loot6_count": "1-1",
                        "loot9": "💧 шкура водяного змея 🐍", "loot9_chance": "2%", "loot9_count": "1-1",
                        "loot10": "🌀 руна водяного змея 🌀", "loot10_chance": "0.001%", "loot10_count": "1-1"
                }
}

bot = telebot.TeleBot('5145120712:AAHG4P6mA1SKhD-xtFbFXkb1vFvm1ew7iUY')

# последовательность записи в стрроку информации о инвенторе
posledovat = ["🦎 хвост ящерицы 🦎", "🍈 чешуя (F) 🍈", "🃏 игральный камень 🃏", "🌰 орех 🌰", "🐿 шкура белки 🐿", "⛓ кусочек цепи ⛓", "💰 мешок монет 💰",
                "🌾 зерно 🌾", "🥚 яйцо (F) 🥚", "🐁 крысиный хвост 🐁", "🐀 крысина шкура 🐀", "🥀 ядовитая роза 🥀", "💉 колба яд-826 💉", "🥩 мясо 🥩",
                "🐺 клык волка 🐺", "⚪ белая сфера ⚪", "🕸 паутинка 🕸", "🦗 обычный жучок 🦗", "⚫ черная сфера ⚫", "🌳 обычное дерево 🌳", "🗿  обычный камень  🗿",
                "🐉 шкура дракона (F-) 🐉", "🍂 зачахшие листья удачи 🍂", "💧 капля 💧", "🐚 ракушка 🐚", "⭐ звезда (F) ⭐", "⚡ электрический камень ⚡",
                "🟢 зеленые водоросли 🌿", "🔴 красные водоросли 🌿", "🐟 рыба 🐟", "⭐ звезда (F+) ⭐", "⭐ звезда (F++) ⭐", "⭐ звезда (F+++) ⭐", "⭐ звезда (E-) ⭐",
                "💀 змеиный клык 🐍", "💧 шкура водяного змея 🐍", "🌀 руна водяного змея 🌀", "🍈 чешуя (F+) 🍈"
]

# нереализованные функции
another = ["🔮 зачаровать снаряжение 🔮", "🔥 усовершенствовать снаряжение 🔥", "🎯 улучшить снаряжение 🎯", "🔮 рискнуть 🔮",
           "артефакт", "броня", "👑 артефакт 👑", "-броню-"]


# команда для получении информации о состоянии снаряжения пользователя
@bot.message_handler(commands=['equipment'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("go")
    btn2 = types.KeyboardButton("экипировать")
    markup.add(btn1)
    markup.add(btn2)

    # мечи
    sword_list = [
        "🌳 Wooden sword 🌳",
        "🐁 Rat sword 🐀",
        "🗿 Stone sword 🗿"
    ]
    f = open("f.txt", encoding="utf8", mode = 'r')
    global search, cho_skasat, ab
    search = 0
    lis = []
    cho_skasat = 0

    for gh in enumerate(f):
        line = gh[1][:-1]
        v = str(line).split("|")
        
        if v[0] == str(message.chat.id):
            stroka = v[1].split("/")
            search = 1
            
            if stroka[9] == "1":
                cho_skasat = 1
            ab = stroka
        
        if len(v) == 2:
            lis.append(v[0] + "|" + v[1])
    f.close()

    ay = ab[29].split("*")
    if ab[21] != "":
        y = ay[sword_list.index(ab[21])]

    # используемый меч
    if ab[21] != "":
        bot.send_message(message.chat.id, f"меч: {ab[21]}", reply_markup=markup)
        s = "@xxxx[{"
        s += int(y) * "🔶"
        s += (10 - int(y)) * "🔹"
        bot.send_message(message.chat.id, s, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "у вас используемого нет меча", reply_markup=markup)
    g = ab[28].split("*")
    
    # инвентарь мече1
    bot.send_message(message.chat.id, "Инвентарь мечей:", reply_markup=markup)
    ans_str_sword = ""
    for i in range(len(g)):
        if g[i] != "0":
            ans_str_sword += f"{sword_list[i]}:  {g[i]}"
            ans_str_sword += "\n"
            ans_str_sword += "\n"
    bot.send_message(message.chat.id, ans_str_sword, reply_markup=markup)

# команда для получении информации об инвенторе зелий пользователя
@bot.message_handler(commands=['potions'])
def start(message):
    f = open("f.txt", encoding="utf8", mode = 'r')
    for gh in enumerate(f):
        line = gh[1][:-1]
        v = str(line).split("|")
        if v[0] == str(message.chat.id):
            v[1] = v[1].split("/")
            lootik = v[1][31].split("*")
    f.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("go")
    print(ab)
    markup.add(btn1)

    # зелья
    loot_list = [
        "💜 малое зелье исцеления 💜",
        "💙 малое зелье исцеления 2.0 💙",
        "💚 небольшое зелье исцеления 💚"
    ]

    # инвентарь зелий
    ans_str = ""
    bot.send_message(message.chat.id, "Инвентарь зелий:", reply_markup=markup)
    for i in range(len(loot_list)):
       ans_str += f"{loot_list[i]}:  {lootik[i]}\n"
       ans_str += "\n"
    bot.send_message(message.chat.id, ans_str, reply_markup=markup)

# команда для получении информации об инвенторе пользователя
@bot.message_handler(commands=['inventory'])
def start(message):
    
    f = open("f.txt", encoding="utf8", mode = 'r')
    for gh in enumerate(f):
        line = gh[1][:-1]
        v = str(line).split("|")
        if v[0] == str(message.chat.id):
            v[1] = v[1].split("/")
            lootik = v[1][19].split("*")
    f.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("go")
    print(ab)
    markup.add(btn1)

    # список предметов
    loot_list = [
        "🦎 хвост ящерицы 🦎",
        "🍈 чешуя (F) 🍈",
        "🍈 чешуя (F+) 🍈",
        "🃏 игральный камень 🃏",
        "🌰 орех 🌰",
        "🐿 шкура белки 🐿",
        "⛓ кусочек цепи ⛓",
        "💰 мешок монет 💰",
        "🌾 зерно 🌾",
        "🥚 яйцо (F) 🥚",
        "🐁 крысиный хвост 🐁",
        "🐀 крысина шкура 🐀",
        "🥀 ядовитая роза 🥀",
        "💉 колба яд-826 💉",
        "🥩 мясо 🥩",
        "🐺 клык волка 🐺",
        "⚪ белая сфера ⚪",
        "🕸 паутинка 🕸",
        "🦗 обычный жучок 🦗",
        "⚫ черная сфера ⚫",
        "🌳 обычное дерево 🌳",
        "🗿  обычный камень  🗿",
        "🐉 шкура дракона (F-) 🐉",
        "🍂 зачахшие листья удачи 🍂",
        "💧 капля 💧",
        "🐚 ракушка 🐚",
        "⭐ звезда (F) ⭐",
        "⭐ звезда (F+) ⭐",
        "⭐ звезда (F++) ⭐",
        "⭐ звезда (F+++) ⭐",
        "⭐ звезда (E-) ⭐",
        "⚡ электрический камень ⚡",
        "🟢 зеленые водоросли 🌿",
        "🔴 красные водоросли 🌿",
        "🐟 рыба 🐟",
        "💀 змеиный клык 🐍",
        "💧 шкура водяного змея 🐍",
        "🌀 руна водяного змея 🌀"
    ]

    # инвентарь
    ans_str = ""
    bot.send_message(message.chat.id, "Инвентарь:", reply_markup=markup)
    for i in loot_list:
        ans_str += f"{i}: {lootik[posledovat.index(i)]}\n"
        ans_str += "\n"
    bot.send_message(message.chat.id, ans_str, reply_markup=markup)

# команда для получении информации о характеристиках пользователя
@bot.message_handler(commands=['stats'])
def start(message):
    
    f = open("f.txt", encoding="utf8", mode = 'r')
    for gh in enumerate(f):
        line = gh[1][:-1]
        v = str(line).split("|")
        if v[0] == str(message.chat.id):
            v[1] = v[1].split("/")
            hp = v[1][12]
            damage = v[1][13]
            crit = int(v[1][14])
            chance = v[1][15]
            level = int(v[1][10])
            expa = v[1][11]
            max_h = v[1][18]
            point = v[1][20]
    f.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("points")
    btn2 = types.KeyboardButton("go")
    print(ab)
    markup.add(btn1)
    markup.add(btn2)

    # вывод характеристик
    bot.send_message(message.chat.id, "Статистика игрока:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Lvl: {level}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Exp: {expa}/{level * 100}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Hp: {hp}/{max_h}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Damage: {damage}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Crit damage: {100 + crit}% от Damage", reply_markup=markup)
    bot.send_message(message.chat.id, f"Crit chance: {chance}%", reply_markup=markup)
    bot.send_message(message.chat.id, f"Free points: {point}", reply_markup=markup)

# начало диалога
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    f = open("f.txt", encoding="utf8", mode = 'r')
    global search, cho_skasat, ab
    search = 0
    lis = []
    cho_skasat = 0
    
    # поиск пользователя по базе данных
    for gh in enumerate(f):
        line = gh[1][:-1]
        v = str(line).split("|")
        if v[0] == str(message.chat.id):
            stroka = v[1].split("/")
            search = 1
            if stroka[9] == "1":
                cho_skasat = 1
            ab = stroka
        if len(v) == 2:
            lis.append(v[0] + "|" + v[1])
    f.close()
    
    if cho_skasat == 1:
            btn1 = types.KeyboardButton("Ладно")
            markup.add(btn1)
            bot.send_message(message.chat.id, "🖐", reply_markup=markup)
            bot.send_message(message.chat.id, f"Привет: {stroka[5]}", reply_markup=markup)
            bot.send_message(message.chat.id, f"у вас {stroka[10]} уровень", reply_markup=markup)
    
    else:
            btn1 = types.KeyboardButton("Кто ты ❓")
            markup.add(btn1)
            bot.send_message(message.chat.id, "🖐", reply_markup=markup)
            bot.send_message(message.chat.id, f"Привет user:{message.chat.id}", reply_markup=markup)
    
    # если новый пользователь
    if search == 0:
        information_user = str(message.chat.id) + "|" + stroka_basa
        lis.append(information_user)
        f = open("f.txt", encoding="utf8", mode = 'w')
        for i in range(len(lis)):
            print(lis[i], file=f)
        f.close()
        ab = stroka_basa.split("/")

@bot.message_handler(content_types=['text'])
def func(message):
    global ab
    print(ab)
    # строка пользователя
    ab = "677303548|0/0/0/.../.../.../1/1/.../1/2/15/10/1-2/10/10/🐿  Белка  🐿  (Lvl 1)/-1/10/0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0/2".split("/")
    f = open("f.txt", encoding="utf8", mode = 'r')
    lis = []
    for gh in enumerate(f):
        line = gh[1][:-1]
        v = str(line).split("|")
        if v[0] == str(message.chat.id):
            stroka = v[1].split("/")
            ab = stroka
        if len(v) == 2:
            lis.append(v[0] + "|" + v[1])
    f.close()
    pak = ab[19].split("*") # инвентарь
    pak_zel = ab[31].split("*") # инвентарь зелий
    pak_swords = ab[28].split("*") # инвентарь мечей
    list_pokypki = ["🗿  обычный камень  🗿", "💉 колба яд-826 💉"] # списко предметов для покупки
    list_pokypki_cena = [1, 1000]
    # информация о всех возможных зелиях
    loot_potions = {
        "💜 малое зелье исцеления 💜": pak_zel[0],
        "💙 малое зелье исцеления 2.0 💙": pak_zel[1],
        "💚 небольшое зелье исцеления 💚": pak_zel[2]
    }
    # эффект зелий
    loot_potions_effect = {
        "💜 малое зелье исцеления 💜": 10,
        "💙 малое зелье исцеления 2.0 💙": 15,
        "💚 небольшое зелье исцеления 💚": 25
    }
    # информация о всех возможных предметах
    loot_dict = {
        "🦎 хвост ящерицы 🦎": pak[0],
        "🍈 чешуя (F) 🍈": pak[1],
        "🍈 чешуя (F+) 🍈": pak[37],
        "🃏 игральный камень 🃏": pak[2],
        "🌰 орех 🌰": pak[3],
        "🐿 шкура белки 🐿": pak[4],
        "⛓ кусочек цепи ⛓": pak[5],
        "💰 мешок монет 💰": pak[6],
        "🌾 зерно 🌾": pak[7],
        "🥚 яйцо (F) 🥚": pak[8],
        "🐁 крысиный хвост 🐁": pak[9],
        "🐀 крысина шкура 🐀": pak[10],
        "🥀 ядовитая роза 🥀": pak[11],
        "💉 колба яд-826 💉": pak[12],
        "🥩 мясо 🥩": pak[13],
        "🐺 клык волка 🐺": pak[14],
        "⚪ белая сфера ⚪": pak[15],
        "🕸 паутинка 🕸": pak[16],
        "🦗 обычный жучок 🦗": pak[17],
        "⚫ черная сфера ⚫": pak[18],
        "🌳 обычное дерево 🌳": pak[19],
        "🗿  обычный камень  🗿": pak[20],
        "🐉 шкура дракона (F-) 🐉": pak[21],
        "🍂 зачахшие листья удачи 🍂": pak[22],
        "💧 капля 💧": pak[23],
        "🐚 ракушка 🐚": pak[24],
        "⭐ звезда (F) ⭐": pak[25],
        "⭐ звезда (F+) ⭐": pak[30],
        "⭐ звезда (F++) ⭐": pak[31],
        "⭐ звезда (F+++) ⭐": pak[32],
        "⭐ звезда (E-) ⭐": pak[33],
        "⚡ электрический камень ⚡": pak[26],
        "🟢 зеленые водоросли 🌿": pak[27],
        "🔴 красные водоросли 🌿": pak[28],
        "🐟 рыба 🐟": pak[29],
        "💀 змеиный клык 🐍": pak[34],
        "💧 шкура водяного змея 🐍": pak[35],
        "🌀 руна водяного змея 🌀": pak[36]
    }
    # информация о мечах
    swords_dict = {
        "🌳 Wooden sword 🌳": pak_swords[0],
        "🐁 Rat sword 🐀": pak_swords[1],
        "🗿 Stone sword 🗿": pak_swords[2]
    }
    # регистрация пользователя:
    if ab[9] == "0":
        if(message.text == "Кто ты ❓"):
            ab[0] = "1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да 🎲")
            btn2 = types.KeyboardButton("Нет 🥺")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "У меня нет имени", reply_markup=markup)
            bot.send_message(message.chat.id, "...", reply_markup=markup)
            bot.send_message(message.chat.id, "...", reply_markup=markup)
            bot.send_message(message.chat.id, "Но я много умею, давай приступим", reply_markup=markup)
            bot.send_message(message.chat.id, "...", reply_markup=markup)
            bot.send_message(message.chat.id, 'Если ты новичок нажми "начать"', reply_markup=markup)
            bot.send_message(message.chat.id, 'Если нет - "продолжить"', reply_markup=markup)
            bot.send_message(message.chat.id, "...", reply_markup=markup)
            bot.send_message(message.chat.id, "Готов ?", reply_markup=markup)

        elif message.text == "Да 🎲":
            ab[0] = "0"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Начать")
            btn2 = types.KeyboardButton("Продолжить")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Круто, приступим", reply_markup=markup)
            bot.send_message(message.chat.id, "🍀", reply_markup=markup)

        elif message.text == "Нет 🥺":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да 🎲")
            btn2 = types.KeyboardButton("Нет 🥺")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Я не спешу)", reply_markup=markup)
            bot.send_message(message.chat.id, "Скажи когда будешь готов...", reply_markup=markup)
            bot.send_message(message.chat.id, "...", reply_markup=markup)
            bot.send_message(message.chat.id, "Готов ?", reply_markup=markup)

        elif message.text == "Продолжить":
            photo1 = open('a.png', 'rb')
            bot.send_message(message.chat.id, "⚠ эта функция находится в разработке ⚠")
            bot.send_photo(message.chat.id, photo=photo1)

        # запись логина:
        elif message.text == "Начать" and ab[6] == "0":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("...")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="Придумайте логин:", reply_markup=markup)
            ab[1] = "1"

        elif ab[1] == "1":
            ab[3] = message.text
            ab[1] = "0"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да 😐")
            btn2 = types.KeyboardButton("Нет 😡")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f"ваш логин: {ab[3]} ?", reply_markup=markup)

        # запись пароля
        elif ab[1] == "0" and (message.text == "Да 😐") and ab[6] == "0":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("...")
            markup.add(btn1)
            ab[5] = ab[3]
            ab[6] = "1"
            bot.send_message(message.chat.id, "а теперь безопасность)", reply_markup=markup)
            bot.send_message(message.chat.id, text="Придумайте пароль:", reply_markup=markup)
            ab[2] = "1"

        elif ab[6] == "0" and ab[1] == "0" and (message.text == "Нет 😡"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("...")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="Упс... наверное это моя ошибка, попробуйте еще раз", reply_markup=markup)
            bot.send_message(message.chat.id, text="Напишите придуманный логин:", reply_markup=markup)
            ab[1] = "1"

        elif ab[2] == "1":
            ab[8] = message.text
            ab[2] = "0"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да 🤖")
            btn2 = types.KeyboardButton("Нет 👿")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f"ваш пароль: {ab[8]} ?", reply_markup=markup)

        # конец регистрации
        elif ab[2] == "0" and (message.text == "Да 🤖") and ab[7] == "0":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Ладно")
            markup.add(btn1)
            ab[4] = ab[8]
            ab[7] = "1"
            bot.send_message(message.chat.id, f"ваш логин: {ab[5]}", reply_markup=markup)
            bot.send_message(message.chat.id, f"ваш пароль: {ab[4]}", reply_markup=markup)
            bot.send_message(message.chat.id, text="вы успешно внесенны в базу)", reply_markup=markup)
            ab[9] = "1"
            stroka_basa = ""

            # обновление строки информации
            stroka_basa += str(ab[0]) + "/" + str(ab[1]) + "/" + str(ab[2]) + "/"
            stroka_basa += ab[3] + "/" + ab[4] + "/" + ab[5] + "/"
            stroka_basa += str(ab[6]) + "/" + str(ab[7]) + "/" + ab[8] + "/" + str(ab[9])
            stroka_basa += "/" + str(ab[10]) + "/" + str(ab[11])
            stroka_basa += "/" + str(ab[12])+ "/" + str(ab[13]) + "/" + str(ab[14]) + "/" + str(ab[15])
            stroka_basa += "/" + str(ab[16]) + "/" + str(ab[17]) + "/" + str(ab[18]) + "/" + str(ab[19]) + "/" + str(ab[20])
            stroka_basa += "/" + str(ab[21]) + "/" + str(ab[22])
            stroka_basa += "/" + str(ab[23]) + "/" + str(ab[24])
            stroka_basa += "/" + str(ab[25]) + "/" + str(ab[26]) + "/" + str(ab[27]) + "/" + str(ab[28]) + "/" + str(ab[29]) + "/" + str(ab[30]) + "/" + str(ab[31])+ "/" + str(ab[32])

            f = open("f.txt", encoding="utf8", mode = 'r')
            lis = []
            for gh in enumerate(f):
                line = gh[1][:-1]
                v = str(line).split("|")
                if v[0] == str(message.chat.id):
                    v[1] = stroka_basa
                    #ans = v[0] + v[1]
                if len(v) == 2:
                    lis.append(v[0] + "|" + v[1])
            f.close()
            f = open("f.txt", encoding="utf8", mode = 'w')
            for i in lis:
                print(i, file=f)
            f.close()

        elif ab[7] == "0" and ab[2] == "0" and (message.text == "Нет 👿"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("...")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="Упс... наверное это моя ошибка, попробуйте еще раз", reply_markup=markup)
            bot.send_message(message.chat.id, text="Напишите придуманный пароль:", reply_markup=markup)
            ab[2] = "1"
            print(ab)
        
        # при всех других командах:
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

        # запись обновленной строки в базу данных
        f = open("f.txt", encoding="utf8", mode = 'r')
        lis = []
        for gh in enumerate(f):
            line = gh[1][:-1]
            v = str(line).split("|")
            if v[0] == str(message.chat.id):
                v[1] = ""
                for i in ab:
                    v[1] += i
                    v[1] += "/"
            if len(v) == 2:
                lis.append(v[0] + "|" + v[1])
        f.close()
        f = open("f.txt", encoding="utf8", mode = 'w')
        for i in range(len(lis)):
            print(lis[i], file=f)
        f.close()

    else:
        global based_monstrs_of_prosstoles
        if message.text == "Ладно":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("go")
            btn2 = types.KeyboardButton("stop")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Отлично 👑", reply_markup=markup)
            bot.send_message(message.chat.id, "Пора бы уже начинать 👑", reply_markup=markup)

        elif message.text == "stop":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("go")
            markup.add(btn1)
            bot.send_message(message.chat.id, "не та кнопка", reply_markup=markup)
            bot.send_message(message.chat.id, "подумай еще раз)", reply_markup=markup)

        # локация алхимия
        elif message.text == "⚗️ Алхимия ⚗️":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚗️ создать зелье ⚗️")
            btn2 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, "Алхи́мия (лат. alchimia, alchymia) — специфическая область натурфилософии, сформировавшаяся в лоне герметической традиции", reply_markup=markup)
        
        elif message.text == "⚗️ создать зелье ⚗️":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            for i in loot_potions:
                btn = types.KeyboardButton(f'создать "{i}"')
                markup.add(btn)
            
            btn1 = types.KeyboardButton("⚗️ назад ⚗️")
            markup.add(btn1)
            bot.send_message(message.chat.id, "список зелий:", reply_markup=markup)
            bot.send_message(message.chat.id, "💜 малое зелье исцеления 💜:\n\n-ИНГРЕДИЕНТЫ-\n🌰 орех 🌰: 50\n\n-ЭФФЕКТ-:\n+10hp", reply_markup=markup)
            bot.send_message(message.chat.id, "💙 малое зелье исцеления 2.0 💙:\n\n-ИНГРЕДИЕНТЫ-\n🥩 мясо 🥩: 8\n\n-ЭФФЕКТ-:\n+15hp", reply_markup=markup)
            bot.send_message(message.chat.id, "💚 небольшое зелье исцеления 💚:\n\n-ИНГРЕДИЕНТЫ-\n🕸 паутинка 🕸: 3\n🌳 обычное дерево 🌳: 20\n\n-ЭФФЕКТ-:\n+25hp", reply_markup=markup)
        
        elif message.text == 'создать "💚 небольшое зелье исцеления 💚"':
            if int(loot_dict["🌳 обычное дерево 🌳"]) >= 20 and int(loot_dict["🕸 паутинка 🕸"]) >= 3:
                loot_dict["🌳 обычное дерево 🌳"] = str(int(loot_dict["🌳 обычное дерево 🌳"]) - 20)
                loot_dict["🕸 паутинка 🕸"] = str(int(loot_dict["🕸 паутинка 🕸"]) - 3)
                bot.send_message(message.chat.id, 'вы успешно создали\n"💚 небольшое зелье исцеления 💚"')
                loot_potions["💚 небольшое зелье исцеления 💚"] = str(int(loot_potions["💚 небольшое зелье исцеления 💚"]) + 1)
            
            else:
                 bot.send_message(message.chat.id, "недостаточно предметов")
        
        elif message.text == 'создать "💜 малое зелье исцеления 💜"':
            if int(loot_dict["🌰 орех 🌰"]) >= 50:
                loot_dict["🌰 орех 🌰"] = str(int(loot_dict["🌰 орех 🌰"]) - 50)
                bot.send_message(message.chat.id, 'вы успешно создали\n"💜 малое зелье исцеления 💜"')
                loot_potions["💜 малое зелье исцеления 💜"] = str(int(loot_potions["💜 малое зелье исцеления 💜"]) + 1)
            
            else:
                 bot.send_message(message.chat.id, "недостаточно предметов")
        
        elif message.text == 'создать "💙 малое зелье исцеления 2.0 💙"':
            if int(loot_dict["🥩 мясо 🥩"]) >= 8:
                loot_dict["🥩 мясо 🥩"] = str(int(loot_dict["🥩 мясо 🥩"]) - 8)
                bot.send_message(message.chat.id, 'вы успешно создали\n"💙 малое зелье исцеления 2.0 💙"')
                loot_potions["💙 малое зелье исцеления 2.0 💙"] = str(int(loot_potions["💙 малое зелье исцеления 2.0 💙"]) + 1)
            
            else:
                 bot.send_message(message.chat.id, "недостаточно предметов")
        
        elif message.text == "⚗️ назад ⚗️":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚗️ создать зелье ⚗️")
            btn2 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, "Алхи́мия (лат. alchimia, alchymia) — специфическая область натурфилософии, сформировавшаяся в лоне герметической традиции", reply_markup=markup)
        
        # главное меню
        elif message.text == "go":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🌳 лес 🌲")
            btn2 = types.KeyboardButton("✨тотем✨")
            btn3 = types.KeyboardButton("⛲ фонтан надежд ⛲")
            btn4 = types.KeyboardButton("локация 4")
            btn5 = types.KeyboardButton("команды")
            btn6 = types.KeyboardButton("🔮 кузница ⚒")
            btn7 = types.KeyboardButton("💸 Торговая лавка 💸")
            btn8 = types.KeyboardButton("⚗️ Алхимия ⚗️")
            btn9 = types.KeyboardButton("🌊 озеро 🌊")
            markup.add(btn1, btn9, btn6)
            markup.add(btn2, btn8)
            markup.add(btn3)
            markup.add(btn7)
            markup.add(btn4, btn5)
            bot.send_message(message.chat.id, "добро пожаловать в мир приключений", reply_markup=markup)
            bot.send_message(message.chat.id, "обучение не предусмотренно 😀", reply_markup=markup)
            bot.send_message(message.chat.id, "удачи", reply_markup=markup)
            bot.send_message(message.chat.id, "выберите локацию", reply_markup=markup)
        
        # локация кузница
        elif message.text == "🔮 кузница ⚒":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚒ создать снаряжение ⚒")
            btn2 = types.KeyboardButton("🎯 улучшить снаряжение 🎯")
            btn3 = types.KeyboardButton("🔥 усовершенствовать снаряжение 🔥")
            btn4 = types.KeyboardButton("🔮 зачаровать снаряжение 🔮")
            btn5 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            bot.send_message(message.chat.id, "добро пожаловать в кузницу)", reply_markup=markup)
        
        elif message.text == "🔮  назад  ⚒":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚒ создать снаряжение ⚒")
            btn2 = types.KeyboardButton("🎯 улучшить снаряжение 🎯")
            btn3 = types.KeyboardButton("🔥 усовершенствовать снаряжение 🔥")
            btn4 = types.KeyboardButton("🔮 зачаровать снаряжение 🔮")
            btn5 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            bot.send_message(message.chat.id, "добро пожаловать в кузницу)", reply_markup=markup)
        
        elif message.text == "⚒ создать снаряжение ⚒":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("меч")
            btn2 = types.KeyboardButton("броня")
            btn3 = types.KeyboardButton("артефакт")
            btn4 = types.KeyboardButton("🔮  назад  ⚒")
            markup.add(btn1, btn2, btn3)
            markup.add(btn4)
            bot.send_message(message.chat.id, "выберите предмет для создания", reply_markup=markup)
        
        elif message.text == "🔮 назад ⚒":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("меч")
            btn2 = types.KeyboardButton("броня")
            btn3 = types.KeyboardButton("артефакт")
            btn4 = types.KeyboardButton("🔮  назад  ⚒")
            markup.add(btn1, btn2, btn3)
            markup.add(btn4)
            bot.send_message(message.chat.id, "выберите предмет для создания", reply_markup=markup)
        
        elif message.text == "меч":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            for i in based_sword:
                btn = types.KeyboardButton(i)
                markup.add(btn)
            
            btn1 = types.KeyboardButton("🔮 назад ⚒")
            markup.add(btn1)
            bot.send_message(message.chat.id, "выберите меч для создания", reply_markup=markup)
        
        elif message.text in based_sword:
            ab[27] = message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("создать")
            btn2 = types.KeyboardButton("🔮назад⚒")
            
            # информация о мече
            bot.send_message(message.chat.id, f"{message.text}:", reply_markup=markup)
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, f'Upgrade attack: {based_sword[message.text]["damage"]}', reply_markup=markup)
            craft_item = "Craft:"
            craft_item += "\n"
            
            for i in based_sword[message.text]["craft"]:
                craft_item += i
                craft_item += ": "
                craft_item += str(based_sword[message.text]["craft"][i])
                craft_item += "\n"
            bot.send_message(message.chat.id, craft_item, reply_markup=markup)
        
        elif message.text == "🔮назад⚒":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            for i in based_sword:
                btn = types.KeyboardButton(i)
                markup.add(btn)
            
            btn1 = types.KeyboardButton("🔮 назад ⚒")
            markup.add(btn1)
            bot.send_message(message.chat.id, "выберите меч для создания", reply_markup=markup)
        
        elif message.text == "создать":
            cf = 0
            if ab[27] in based_sword:
                for i in based_sword[ab[27]]["craft"]:
                    if int(loot_dict[i]) < based_sword[ab[27]]["craft"][i]:
                        cf = 1
                
                if cf == 1:
                    bot.send_message(message.chat.id, "недостаточно ресурсов")
                
                else:
                    for i in based_sword[ab[27]]["craft"]:
                        loot_dict[i] = str(int(loot_dict[i]) - based_sword[ab[27]]["craft"][i])
                    bot.send_message(message.chat.id, f"вы создали {ab[27]}")
                    swords_dict[ab[27]] = str(int(swords_dict[ab[27]]) + 1)
        
        elif message.text == "экипировать":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚔ меч ⚔")
            btn2 = types.KeyboardButton("-броню-")
            btn3 = types.KeyboardButton("👑 артефакт 👑")
            btn4 = types.KeyboardButton("|назад|")
            markup.add(btn1, btn2, btn3)
            markup.add(btn4)
            bot.send_message(message.chat.id, "выберите предмет для экипировки", reply_markup=markup)
        
        elif message.text == "|назад|":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("go")
            btn2 = types.KeyboardButton("экипировать")
            markup.add(btn1)
            markup.add(btn2)

            sword_list = [
                "🌳 Wooden sword 🌳",
                "🐁 Rat sword 🐀",
                "🗿 Stone sword 🗿"
            ]

            ay = ab[29].split("*")
            y = ay[sword_list.index(ab[21])]

            if ab[21] != "":
                bot.send_message(message.chat.id, f"меч: {ab[21]}", reply_markup=markup)
                s = "@xxxx[{"
                s += int(y) * "🔶"
                s += (10 - int(y)) * "🔹"
                bot.send_message(message.chat.id, s, reply_markup=markup)
            
            else:
                bot.send_message(message.chat.id, "у вас используемого нет меча", reply_markup=markup)
            
            g = ab[28].split("*")
            bot.send_message(message.chat.id, "Инвентарь мечей:", reply_markup=markup)
            ans_str_sword = ""
            
            for i in range(len(g)):
                if g[i] != "0":
                    ans_str_sword += f"{sword_list[i]}:  {g[i]}"
                    ans_str_sword += "\n"
                    ans_str_sword += "\n"
            bot.send_message(message.chat.id, ans_str_sword, reply_markup=markup)
        
        elif message.text == "⚔ меч ⚔":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            # создание кнопок со всеми мечами для крафта
            for i in swords_dict:
                if swords_dict[i] != "0":
                    btn = types.KeyboardButton(f"-{i}-")
                    markup.add(btn)

            btn1 = types.KeyboardButton("-назад-")
            markup.add(btn1)
            bot.send_message(message.chat.id, "выберите меч для экипировки", reply_markup=markup)
        
        elif (message.text[0] == "-" and message.text[-1] == "-") and message.text[1:-1] in swords_dict:
            ab[21] = message.text[1:-1]
            ab[22] = str(based_sword[message.text[1:-1]]["damage"])[:-1]
            bot.send_message(message.chat.id, f"вы экипировали {ab[21]}")
        
        elif message.text == "-назад-":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚔ меч ⚔")
            btn2 = types.KeyboardButton("-броню-")
            btn3 = types.KeyboardButton("👑 артефакт 👑")
            btn4 = types.KeyboardButton("|назад|")
            markup.add(btn1, btn2, btn3)
            markup.add(btn4)
            bot.send_message(message.chat.id, "выберите предмет для экипировки", reply_markup=markup)
        
        # все доступные команды
        elif message.text == "команды":
            komands = ""
            komands += "/start - начать с приветствия"
            komands += "\n"
            komands += "\n"
            komands += "/stats - характеристики игрока"
            komands += "\n"
            komands += "\n"
            komands += "/inventory - инвентарь игрока"
            komands += "\n"
            komands += "\n"
            komands += "/equipment - снаряжение игрока"
            komands += "\n"
            komands += "\n"
            komands += "/potions - инвентарь зелий"
            bot.send_message(message.chat.id, komands)
        
        # локация тотем
        elif message.text == "✨тотем✨":
            if int(ab[12]) > 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn2 = types.KeyboardButton("назад")
                markup.add(btn2)
                bot.send_message(message.chat.id, "ты все ещё способен сражаться...", reply_markup=markup)
            
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("выпить зелье")
                btn2 = types.KeyboardButton("назад")
                markup.add(btn1)
                markup.add(btn2)
                bot.send_message(message.chat.id, "выглядишь ужасно, нужно зелье воскрешения ?", reply_markup=markup)
                bot.send_message(message.chat.id, text="при возрождении вы потеряете exp, однако ваш уровень останется прежним", reply_markup=markup)
        
        # локация фонтан
        elif message.text == "⛲ фонтан надежд ⛲":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("восстановить hp")
            btn2 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, "лучшее место для восполнения hp", reply_markup=markup)
            bot.send_message(message.chat.id, "правда работает с перебоями...", reply_markup=markup)
        
        elif message.text == "восстановить hp":
            if ab[12] != "0":
                x = random.randint(0, 5)
                
                if int(ab[12]) + x >= int(ab[18]):
                    x = int(ab[18]) - int(ab[12])
                ab[12] = str(int(ab[12]) + x)
                bot.send_message(message.chat.id, f"вы восстановили {x}hp")
                
                # если full hp
                if int(ab[12]) >= int(ab[18]):
                    ab[12] = ab[18]
                    bot.send_message(message.chat.id, f"вы полностью восстановили hp")
            else:
                bot.send_message(message.chat.id, "призраков не обслуживаем")
                bot.send_message(message.chat.id, "идите воскреситись...")
                bot.send_message(message.chat.id, 'вам сюда ---> "✨тотем✨"')
        
        elif message.text == "локация 4":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("спасибо 🥺")
            btn2 = types.KeyboardButton("🤬чо🤬")
            btn3 = types.KeyboardButton("назад")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Вы вошли в локацию "Локация 4"', reply_markup=markup)
            bot.send_message(message.chat.id, "у вас вычтенно: 5exp", reply_markup=markup)
            bot.send_message(message.chat.id, "нечего отлынивать и ходить по смонительнеым местам", reply_markup=markup)
            ab[11] = str(max(int(ab[11]) - 5, 0))
        
        elif message.text == "спасибо 🥺":
            bot.send_message(message.chat.id, "пожалуйста")
        
        elif message.text == "🤬чо🤬":
            bot.send_message(message.chat.id, "👇 ваш отзыв добавлен в книгу жалоб")
            bot.send_message(message.chat.id, "🗑")
        
        elif message.text == "назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🌳 лес 🌲")
            btn2 = types.KeyboardButton("✨тотем✨")
            btn3 = types.KeyboardButton("⛲ фонтан надежд ⛲")
            btn4 = types.KeyboardButton("локация 4")
            btn5 = types.KeyboardButton("команды")
            btn6 = types.KeyboardButton("🔮 кузница ⚒")
            btn7 = types.KeyboardButton("💸 Торговая лавка 💸")
            btn8 = types.KeyboardButton("⚗️ Алхимия ⚗️")
            btn9 = types.KeyboardButton("🌊 озеро 🌊")
            markup.add(btn1, btn9, btn6)
            markup.add(btn2, btn8)
            markup.add(btn3)
            markup.add(btn7)
            markup.add(btn4, btn5)
            bot.send_message(message.chat.id, "решили испытать удачу на новой локации ?) ", reply_markup=markup)
        
        # локация торговая лавка
        elif message.text == "💸 Торговая лавка 💸":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🥃 рынок предметов 🥃")
            btn2 = types.KeyboardButton("💎 разрушение предметов 💎")
            btn3 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            bot.send_message(message.chat.id, "добро пожжаловать покупатель)", reply_markup=markup)
        
        elif message.text == "🥃 рынок предметов 🥃":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            lot_pokypka = ""
            lot_pokypka += "№1 🗿  обычный камень  🗿"
            lot_pokypka += "\n"
            lot_pokypka += "№2 💉 колба яд-826 💉"
            btn1 = types.KeyboardButton("💲 купить 💲")
            btn3 = types.KeyboardButton("💲 назад 💎")
            markup.add(btn1)
            markup.add(btn3)
            bot.send_message(message.chat.id, "лоты для покупки:", reply_markup=markup)
            bot.send_message(message.chat.id, lot_pokypka, reply_markup=markup)
        
        elif message.text == "💲 купить 💲":
            bot.send_message(message.chat.id, "введите колличество товара в формате:")
            bot.send_message(message.chat.id, "☆(номер лота)_(кол-во)")
            bot.send_message(message.chat.id, "пример покупки\n100 - 🗿  обычный камень  🗿:")
            bot.send_message(message.chat.id, "☆1_100")
        
        elif message.text[0] == "☆":
            print(message.text[1])
            if message.text[1] == "1":
                list_pok = message.text.split("_")
                count_pok = int(list_pok[1])
                pokypka = list_pokypki[int(list_pok[0][1:]) - 1]
                
                # проверка наличия необходимого колличества опыта для покупки
                if list_pokypki_cena[int(list_pok[0][1:]) - 1] * count_pok > int(ab[11]):
                    bot.send_message(message.chat.id, "недостаточно опыта")
                else:
                    ab[11] = str(int(ab[11]) - list_pokypki_cena[int(list_pok[0][1:]) - 1] * count_pok)
                    bot.send_message(message.chat.id, f"вы успешно купили:\n{count_pok} - {pokypka}")
                    loot_dict[pokypka] = str(int(loot_dict[pokypka]) + count_pok)
        
        elif message.text == "💎 разрушение предметов 💎":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("(⚪ белая сфера ⚪)")
            btn2 = types.KeyboardButton("(💉 колба яд-826 💉)")
            btn3 = types.KeyboardButton("💲 назад 💎")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)

            bot.send_message(message.chat.id, "информация о разрушении:", reply_markup=markup)
            info_raz = "⚪ белая сфера ⚪:"
            info_raz += "\n"
            info_raz += "10 - 🐺 клык волка 🐺"
            info_raz += "\n"
            info_raz += "\n"
            info_raz += "💉 колба яд-826 💉:"
            info_raz += "\n"
            info_raz += "5 - 🥀 ядовитая роза 🥀"
            info_raz += "\n"
            info_raz += "20 - ⛓ кусочек цепи ⛓"
            bot.send_message(message.chat.id, info_raz, reply_markup=markup)
        
        elif message.text == "💲 назад 💎":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💲 рынок предметов 💲")
            btn2 = types.KeyboardButton("💎 разрушение предметов 💎")
            btn3 = types.KeyboardButton("назад")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            bot.send_message(message.chat.id, "выбирайте с умом", reply_markup=markup)
        
        elif message.text == "(⚪ белая сфера ⚪)":
            # проверка наличия всех ингридиентов
            if loot_dict["⚪ белая сфера ⚪"] != "0":
                loot_dict["⚪ белая сфера ⚪"] = str(int(loot_dict["⚪ белая сфера ⚪"]) - 1)
                loot_dict["🐺 клык волка 🐺"] = str(int(loot_dict["🐺 клык волка 🐺"]) + 10)
                bot.send_message(message.chat.id, "вы уcпешно разрушили ⚪ белая сфера ⚪")
            else:
                bot.send_message(message.chat.id, "недостаточно предметов для разрушения", reply_markup=markup)
        
        elif message.text == "(💉 колба яд-826 💉)":
            # проверка наличия всех ингридиентов
            if loot_dict["💉 колба яд-826 💉"] != "0":
                loot_dict["💉 колба яд-826 💉"] = str(int(loot_dict["💉 колба яд-826 💉"]) - 1)
                loot_dict["🥀 ядовитая роза 🥀"] = str(int(loot_dict["🥀 ядовитая роза 🥀"]) + 5)
                loot_dict["⛓ кусочек цепи ⛓"] = str(int(loot_dict["⛓ кусочек цепи ⛓"]) + 20)
                bot.send_message(message.chat.id, "вы успешно разрушили 💉 колба яд-826 💉")
            else:
                bot.send_message(message.chat.id, "недостаточно предметов для разрушения", reply_markup=markup)
        
        # локация лес
        elif message.text == "🌳 лес 🌲":
            ab[32] = "🌳 лес 🌲"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3 = types.KeyboardButton("🌵 природные ресурсы 🌵")
            btn2 = types.KeyboardButton("🐺 мобы 🐺")
            markup.add(btn3)
            markup.add(btn2)
            btn1 = types.KeyboardButton("назад")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Вы вошли в локацию "🌳 лес 🌲"', reply_markup=markup)
        
        # локация озеро
        elif message.text == "🌊 озеро 🌊":
            ab[32] = "🌊 озеро 🌊"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3 = types.KeyboardButton("💧 природные ресурсы 💧")
            btn2 = types.KeyboardButton("🐬 мобы 🐬")
            markup.add(btn3)
            markup.add(btn2)
            btn1 = types.KeyboardButton("назад")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Вы вошли в локацию "🌊 озеро 🌊"', reply_markup=markup)
        
        # мобы для добычи:
        elif message.text == "💧 природные ресурсы 💧":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in based_monstrs_of_ozero_vvod:
                if based_monstrs_of_ozero_vvod[i]["type"] == "mining":
                    btn = types.KeyboardButton(i)
                    markup.add(btn)
            btn1 = types.KeyboardButton("🌊 вернуться назад 🌊")
            markup.add(btn1)
            bot.send_message(message.chat.id, "камень не волк, сдачи не даст 🐺", reply_markup=markup)
        
        elif message.text == "🌵 природные ресурсы 🌵":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in based_monstrs_of_prosstoles_vvod:
                if based_monstrs_of_prosstoles_vvod[i]["type"] == "mining":
                    btn = types.KeyboardButton(i)
                    markup.add(btn)
            btn1 = types.KeyboardButton("🌲 вернуться назад 🌲")
            markup.add(btn1)
            bot.send_message(message.chat.id, "камень не волк, сдачи не даст 🐺", reply_markup=markup)
        
        # мобы для сражения
        elif message.text == "🐬 мобы 🐬":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in based_monstrs_of_ozero_vvod:
                if based_monstrs_of_ozero_vvod[i]["type"] == "default":
                    btn = types.KeyboardButton(i)
                    markup.add(btn)
            btn1 = types.KeyboardButton("🌊 вернуться назад 🌊")
            markup.add(btn1)
            bot.send_message(message.chat.id, "Иногда хватает мгновения, чтобы забыть жизнь, а иногда не хватает жизни, чтобы забыть мгновение 🐺", reply_markup=markup)
        
        elif message.text == "🐺 мобы 🐺":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in based_monstrs_of_prosstoles_vvod:
                if based_monstrs_of_prosstoles_vvod[i]["type"] == "default":
                    btn = types.KeyboardButton(i)
                    markup.add(btn)
            btn1 = types.KeyboardButton("🌲 вернуться назад 🌲")
            markup.add(btn1)
            bot.send_message(message.chat.id, "Иногда хватает мгновения, чтобы забыть жизнь, а иногда не хватает жизни, чтобы забыть мгновение 🐺", reply_markup=markup)
        
        elif message.text in loot_potions:
            
            # проверка наличия зелия
            if loot_potions[message.text] != "0":
                loot_potions[message.text] = str(int(loot_potions[message.text]) - 1)
                ab[12] = str(min(int(ab[18]), int(ab[12]) + loot_potions_effect[message.text]))
                bot.send_message(message.chat.id, "вы выпили зелье")
                bot.send_message(message.chat.id, f"hp игрока: {ab[12]}")
            
            else:
                bot.send_message(message.chat.id, "недостаточно зелий")
            
            if based_monstrs_of_prosstoles[ab[16]]["type"] == "default":
                g = based_monstrs_of_prosstoles[ab[16]]["damage"]
                bot.send_message(message.chat.id, text=f"вам нанесли {g} урона")
                ab[12] = str(int(ab[12]) - int(g))
                if int(ab[12]) < 0:
                    ab[12] = "0"
                bot.send_message(message.chat.id, text=f"оставшиеся hp игрока: {ab[12]}")
            
            # проверка hp игрока
            if int(ab[12]) <= 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("возродиться")
                btn2 = types.KeyboardButton("назад")
                markup.add(btn1)
                markup.add(btn2)
                bot.send_message(message.chat.id, text="вы умерли 💀")
                bot.send_message(message.chat.id, text="...")
                bot.send_message(message.chat.id, text="при возрождении вы потеряете exp, однако ваш уровень останется прежним", reply_markup=markup)
        
        elif message.text == "⚔️ назад ⚔️":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            if based_monstrs_of_prosstoles[ab[16]]["type"] == "default":
                btn1 = types.KeyboardButton("⚔️ ударить ⚔️")
            
            elif based_monstrs_of_prosstoles[ab[16]]["type"] == "bonus":
                btn1 = types.KeyboardButton("🔮 рискнуть 🔮")
            
            elif based_monstrs_of_prosstoles[ab[16]]["type"] == "mining":
                btn1 = types.KeyboardButton("⚒ добыть ⚒")
            
            btn3 = types.KeyboardButton("⚗️ выпить зелье ⚗️")
            
            if ab[32] == "🌳 лес 🌲":
                btn2 = types.KeyboardButton("🌲 вернуться назад 🌲")
            
            elif ab[32] == "🌊 озеро 🌊":
                btn2 = types.KeyboardButton("🌊 вернуться назад 🌊")
            
            markup.add(btn1)
            markup.add(btn3)
            markup.add(btn2)
            
            bot.send_message(message.chat.id, text="вы вернулись к битве", reply_markup=markup)
        elif message.text == "⚗️ выпить зелье ⚗️":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            # кнопки со всеми возможными зельями
            for i in loot_potions:
                btn = types.KeyboardButton(i)
                markup.add(btn)

            btn1 = types.KeyboardButton("⚔️ назад ⚔️")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="выберите зелье", reply_markup=markup)
        
        elif message.text in based_monstrs_of_prosstoles:

            # если началось сражение с монстром
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ab[16] = message.text
            
            if based_monstrs_of_prosstoles[message.text]["type"] == "default":
                ab[17] = str(based_monstrs_of_prosstoles[ab[16]]["hp"])
                btn1 = types.KeyboardButton("⚔️ ударить ⚔️")
            
            elif based_monstrs_of_prosstoles[message.text]["type"] == "bonus":
                btn1 = types.KeyboardButton("🔮 рискнуть 🔮")
            
            elif based_monstrs_of_prosstoles[message.text]["type"] == "mining":
                btn1 = types.KeyboardButton("⚒ добыть ⚒")
            
            btn3 = types.KeyboardButton("⚗️ выпить зелье ⚗️")
            
            if ab[32] == "🌳 лес 🌲":
                btn2 = types.KeyboardButton("🌲 вернуться назад 🌲")
            
            elif ab[32] == "🌊 озеро 🌊":
                btn2 = types.KeyboardButton("🌊 вернуться назад 🌊")
            
            markup.add(btn1)
            markup.add(btn3)
            markup.add(btn2)

            # информация о противнике
            bot.send_message(message.chat.id, text="Информация о противнике:", reply_markup=markup)
            
            for i in based_monstrs_of_prosstoles[message.text]:
                bot.send_message(message.chat.id, text=i + ": " + str(based_monstrs_of_prosstoles[message.text][i]), reply_markup=markup)
            loot = ""

            if based_monstrs_of_prosstoles_loot[message.text]["type"] == "default" or based_monstrs_of_prosstoles_loot[message.text]["type"] == "mining":
                    loot +="Информация о возможных предметах:"
                    loot += "\n"
                    
                    for i in based_monstrs_of_prosstoles_loot[message.text]:
                        
                        if i != "type":
                            if i[-5:] == "hance":
                                loot += based_monstrs_of_prosstoles_loot[message.text][i]
                                loot += "\n"
                            
                            elif i[-5:] != "count":
                                loot += based_monstrs_of_prosstoles_loot[message.text][i]
                                loot += " - "
            bot.send_message(message.chat.id, text=loot, reply_markup=markup)
        
        elif message.text == "⚒ добыть ⚒":
            poluchil = 0
            bot.send_message(message.chat.id, text="вы получили:")
            
            # получение лута с моба
            for i in range (1, 11):
                d1 = "loot" + str(i)
                d2 = d1 + "_count"
                d3 = d1 + "_chance"
                
                if d1 in based_monstrs_of_prosstoles_loot[ab[16]]:
                    d45 = based_monstrs_of_prosstoles_loot[ab[16]][d3][:-1]
                vipal = 0
                
                if d1 in based_monstrs_of_prosstoles_loot[ab[16]]:
                    # если шанс получения < 1
                    if d45[0] == "0":
                        
                        if random.randint(1, 100000000) <= int(float(d45) * 1000000):
                            vipal = 1
                    
                    else:
                        if random.randint(1, 100) <= int(d45):
                            vipal = 1
                    
                    if vipal == 1:
                        u = based_monstrs_of_prosstoles_loot[ab[16]][d2].split("-")
                        cou = random.randint(int(u[0]), int(u[1]))
                        loot_dict[based_monstrs_of_prosstoles_loot[ab[16]][d1]] = str(int(loot_dict[based_monstrs_of_prosstoles_loot[ab[16]][d1]]) + cou)
                        bot.send_message(message.chat.id, text=f'{based_monstrs_of_prosstoles_loot[ab[16]][d1]} - {cou}')
                        poluchil = 1
            
            # если не выпал ни один предмет
            if poluchil == 0:
                bot.send_message(message.chat.id, text="удача вам не благовалит, вы ничего не получили(")
        
        elif message.text == "⚔️ ударить ⚔️":
            poluchil = 0
            
            if int(ab[17]) <= 0:
                bot.send_message(message.chat.id, text="этого джентельмена вы уже залутали сударь")
            
            else:
                # генерация урона
                s = ab[13].split("-")
                s1 = random.randint(int(s[0]), int(s[1]))

                # кринт урон
                s2 = random.randint(0, 100)
                if s2 <= int(ab[15]):
                    s1 = s1 * (100 + int(ab[14])) // 100

                ab[17] = str(int(ab[17]) - s1)
                bot.send_message(message.chat.id, text=f"вы нанесли {s1} урона")
                
                # в случае победы
                if int(ab[17]) <= 0:
                    bot.send_message(message.chat.id, text="hp противника: 0")
                    bot.send_message(message.chat.id, text="победа 🏆")
                    
                    e = based_monstrs_of_prosstoles[ab[16]]["exp"]
                    bot.send_message(message.chat.id, text=f"вам начисленно: {e}exp")
                    bot.send_message(message.chat.id, text="вы получили:")
                    
                    # получение лута с моба
                    for i in range (1, 11):
                        d1 = "loot" + str(i)
                        d2 = d1 + "_count"
                        d3 = d1 + "_chance"
                        
                        if d1 in based_monstrs_of_prosstoles_loot[ab[16]]:
                            d45 = based_monstrs_of_prosstoles_loot[ab[16]][d3][:-1]
                        vipal = 0
                        
                        if d1 in based_monstrs_of_prosstoles_loot[ab[16]]:
                            # если шанс получения < 1
                            if d45[0] == "0":
                                if random.randint(1, 100000000) <= int(float(d45) * 1000000):
                                    vipal = 1
                            
                            else:
                                if random.randint(1, 100) <= int(d45):
                                    vipal = 1
                            
                            # вывод информации о выпавших предметах
                            if vipal == 1:
                                u = based_monstrs_of_prosstoles_loot[ab[16]][d2].split("-")
                                cou = random.randint(int(u[0]), int(u[1]))
                                loot_dict[based_monstrs_of_prosstoles_loot[ab[16]][d1]] = str(int(loot_dict[based_monstrs_of_prosstoles_loot[ab[16]][d1]]) + cou)
                                bot.send_message(message.chat.id, text=f'{based_monstrs_of_prosstoles_loot[ab[16]][d1]} - {cou}')
                                poluchil = 1
                    
                    # если не выпал ни один предмет
                    if poluchil == 0:
                        bot.send_message(message.chat.id, text="удача вам не благовалит, вы ничего не получили(")
                    
                    # обновление колличества опыта
                    ab[11] = str(int(ab[11]) + int(e))
                    if(int(ab[11]) >= int(ab[10]) * 100):
                        ab[11] = str(int(ab[11]) - int(ab[10]) * 100)
                        ab[10] = str(int(ab[10]) + 1)
                        ab[20] = str(int(ab[20]) + 1)
                        bot.send_message(message.chat.id, text="🎆 вы подняли уровень 🎆")
                
                else:
                    bot.send_message(message.chat.id, text=f"hp противника: {ab[17]}")
                    g = based_monstrs_of_prosstoles[ab[16]]["damage"]
                    bot.send_message(message.chat.id, text=f"вам нанесли {g} урона")
                    ab[12] = str(int(ab[12]) - int(g))
                    
                    if int(ab[12]) < 0:
                        ab[12] = "0"
                    bot.send_message(message.chat.id, text=f"оставшиеся hp игрока: {ab[12]}")
                    
                    # проверка hp игрока
                    if int(ab[12]) <= 0:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn1 = types.KeyboardButton("возродиться")
                        btn2 = types.KeyboardButton("назад")
                        markup.add(btn1)
                        markup.add(btn2)
                        bot.send_message(message.chat.id, text="вы умерли 💀")
                        bot.send_message(message.chat.id, text="...")
                        bot.send_message(message.chat.id, text="при возрождении вы потеряете exp, однако ваш уровень останется прежним", reply_markup=markup)
        
        elif message.text == "отмена":
            
            # извлечение информации о характеристиках
            f = open("f.txt", encoding="utf8", mode = 'r')
            for gh in enumerate(f):
                line = gh[1][:-1]
                v = str(line).split("|")
                if v[0] == str(message.chat.id):
                    v[1] = v[1].split("/")
                    hp = v[1][12]
                    damage = v[1][13]
                    crit = int(v[1][14])
                    chance = v[1][15]
                    level = int(v[1][10])
                    expa = v[1][11]
                    max_h = v[1][18]
                    point = v[1][20]
            f.close()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("points")
            btn2 = types.KeyboardButton("go")
            print(ab)

            # вывод информации о характеристиках
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, "Статистика игрока:", reply_markup=markup)
            bot.send_message(message.chat.id, f"Lvl: {level}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Exp: {expa}/{level * 100}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Hp: {hp}/{max_h}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Damage: {damage}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Crit damage: {100 + crit}% от Damage", reply_markup=markup)
            bot.send_message(message.chat.id, f"Crit chance: {chance}%", reply_markup=markup)
            bot.send_message(message.chat.id, f"Free points: {point}", reply_markup=markup)
        
        # прокачка за сет поинтов
        elif message.text == "points":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("hp")
            btn2 = types.KeyboardButton("damage")
            btn3 = types.KeyboardButton("отмена")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            
            bot.send_message(message.chat.id, text="выберите характеристику для улучшения", reply_markup=markup)
            bot.send_message(message.chat.id, text="1 улучшение = 1 point", reply_markup=markup)
            bot.send_message(message.chat.id, text="hp: +5 max hp", reply_markup=markup)
            bot.send_message(message.chat.id, text="damage: +1 min damage, + 1 max damage", reply_markup=markup)
        
        # улучшение характеристик
        elif message.text == "hp" or message.text == "damage":
            if ab[20] == "0":
                bot.send_message(message.chat.id, text="недостаточно points")
            
            elif message.text == "hp":
                ab[20] = str(int(ab[20]) - 1)
                ab[18] = str(int(ab[18]) + 5)
                bot.send_message(message.chat.id, text= f"max hp: {int(ab[18]) - 5} --> {ab[18]}")
            
            elif message.text == "damage":
                ab[20] = str(int(ab[20]) - 1)
                g = ab[30].split("-")
                ab[30] = str(int(g[0]) + 1) + "-" + str(int(g[1]) + 1)
                bot.send_message(message.chat.id, text= f"min damage: {g[0]} --> {str(int(g[0]) + 1)}")
                bot.send_message(message.chat.id, text= f"max damage: {g[1]} --> {str(int(g[1]) + 1)}")
        
        # моментальное возрождение
        elif message.text == "возродиться":
            ab[11] = "0"
            ab[12] = "1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            btn1 = types.KeyboardButton("go")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="вы успешно возродились 😷", reply_markup=markup)
        
        # возрождение через тотем
        elif message.text == "выпить зелье":
            ab[11] = "0"
            ab[12] = "1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            btn1 = types.KeyboardButton("go")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="вы успешно возродились 😷", reply_markup=markup)
        
        elif message.text == "🌊 вернуться назад 🌊":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3 = types.KeyboardButton("💧 природные ресурсы 💧")
            btn2 = types.KeyboardButton("🐬 мобы 🐬")
            markup.add(btn3)
            markup.add(btn2)
            
            btn1 = types.KeyboardButton("назад")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Вы вошли в локацию "🌊 озеро 🌊"', reply_markup=markup)
        
        elif message.text == "🌲 вернуться назад 🌲":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn3 = types.KeyboardButton("🌵 природные ресурсы 🌵")
            btn2 = types.KeyboardButton("🐺 мобы 🐺")
            markup.add(btn3)
            markup.add(btn2)
            
            btn1 = types.KeyboardButton("назад")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Вы вошли в локацию "🌳 лес 🌲"', reply_markup=markup)
        
        # если функция не реализованна
        elif message.text in another:
            photo1 = open('a.png', 'rb')
            bot.send_message(message.chat.id, "⚠ эта функция находится в разработке ⚠")
            bot.send_photo(message.chat.id, photo=photo1)
        
        # если незапрограммированнная команда
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

        # обновление инвенторя
        es = ""
        for i in posledovat:
            es += loot_dict[i]
            es += "*"
        ab[19] = es[:-1]

        # обновление инвенторя зелий
        es = ""
        for i in loot_potions:
            es += loot_potions[i]
            es += "*"
        ab[31] = es[:-1]

        # обновление инвенторя мечей
        es = ""
        for i in swords_dict:
            es += swords_dict[i]
            es += "*"
        ab[28] = es[:-1]

        # обновление урона
        if ab[21] != "":
            da = ab[30].split("-")
            x1 = int(da[0])
            x2 = int(da[1])
            ab[13] = str(x1 * int(ab[22]) // 100) + "-" + str(x2 * int(ab[22]) // 100)
        
        # обновление строки информациии
        stroka_basa = ""
        stroka_basa += str(ab[0]) + "/" + str(ab[1]) + "/" + str(ab[2]) + "/"
        stroka_basa += ab[3] + "/" + ab[4] + "/" + ab[5] + "/"
        stroka_basa += str(ab[6]) + "/" + str(ab[7]) + "/" + ab[8] + "/" + str(ab[9])
        stroka_basa += "/" + str(ab[10]) + "/" + str(ab[11])
        stroka_basa += "/" + str(ab[12])+ "/" + str(ab[13]) + "/" + str(ab[14]) + "/" + str(ab[15])
        stroka_basa += "/" + str(ab[16]) + "/" + str(ab[17]) + "/" + str(ab[18]) + "/" + str(ab[19]) + "/" + str(ab[20])
        stroka_basa += "/" + str(ab[21]) + "/" + str(ab[22])
        stroka_basa += "/" + str(ab[23]) + "/" + str(ab[24])
        stroka_basa += "/" + str(ab[25]) + "/" + str(ab[26]) + "/" + str(ab[27]) + "/" + str(ab[28]) + "/" + str(ab[29]) + "/" + str(ab[30]) + "/" + str(ab[31]) + "/" + str(ab[32])
        
        # обновление базы данных
        f = open("f.txt", encoding="utf8", mode = 'r')
        lis = []
        for gh in enumerate(f):
            line = gh[1][:-1]
            v = str(line).split("|")
            if v[0] == str(message.chat.id):
                v[1] = stroka_basa
            if len(v) == 2:
                lis.append(v[0] + "|" + v[1])
        f.close()
        f = open("f.txt", encoding="utf8", mode = 'w')
        for i in lis:
            print(i, file=f)
        f.close()



bot.polling(none_stop=True)
