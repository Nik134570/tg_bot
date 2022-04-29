import numbers
import random
import telebot
from telebot import types # для указание типов
cto_ti = 0
login = 0
parol = 0
search = 0
user_pred = ""
parolchik = ""
user = ""
login_vvod = 0
parol_vvod = 0
based = []
user_parol = ""
ab = []
registr = 0
stroka_basa = ""
cho_skasat = 0
level = 1
exp = 0
user_hp = 10
user_damage = "1-2"
user_crit_damage = 10
user_chance_crit = 10
mob = ""
max_hp = 10
hp_mob = 0
points = 0
inventory = "0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0*0"
stroka_basa += str(cto_ti) + "/" + str(login) + "/" + str(parol) + "/"
stroka_basa += user_pred + "/" + parolchik + "/" + user + "/"
stroka_basa += str(login_vvod) + "/" + str(parol_vvod) + "/" + user_parol + "/" + str(registr)
stroka_basa += "/" + str(level) + "/" + str(exp)
stroka_basa += "/" + str(user_hp)+ "/" + str(user_damage) + "/" + str(user_crit_damage) + "/" + str(user_chance_crit)
stroka_basa += "/" + mob + "/" + str(hp_mob) + "/" + str(max_hp) + "/" + inventory + "/" + str(points)

based_monstrs_of_prosstoles = {
                "🦎  Обычная ящерица  🦎  (Lvl 1)": {"type": "default", "hp": 7, "damage": 1, "exp": 8},
                "🐿  Белка  🐿  (Lvl 1)": {"type": "default", "hp": 5, "damage": 2, "exp": 10},
                "🦝  Енот  🦝  (Lvl 2)": {"type": "default", "hp": 8, "damage": 3, "exp": 12},
                "Гигантский воробей 🗿  (Lvl 2)": {"type": "default", "hp": 15, "damage": 1, "exp": 13},
                "💉  Ядовитая крыса  💉  (Lvl 3)": {"type": "default", "hp": 5, "damage": 7, "exp": 18},
                "🐺  Белый волк  🐺  (Lvl 3)": {"type": "default", "hp": 10, "damage": 5, "exp": 22},
                "🕷  Лесной паук  🕷  (Lvl 5)": {"type": "default", "hp": 25, "damage": 6, "exp": 50},
                "Загадочный призрак  👻": {"type": "bonus", "type_of_bonus": "hp", "chance_to_positive_reaction": "30%", "positive_reaction": "+10hp", "neggative_reaction": "-10hp"}
}
based_monstrs_of_prosstoles_loot = {
                "🦎  Обычная ящерица  🦎  (Lvl 1)": {"type": "default",
                        "loot1": "🦎 хвост ящерицы 🦎", "loot1_chance": "80%", "loot1_count": "2-4",
                        "loot3": "🍈 чешуя (Lvl 1) 🍈", "loot3_chance": "60%", "loot3_count": "1-3",
                        "loot2": "🃏 игральный камень 🃏", "loot2_chance": "10%", "loot2_count": "1-2"
                },
                "🐿  Белка  🐿  (Lvl 1)": {"type": "default",
                        "loot2": "🌰 орех 🌰", "loot2_chance": "100%", "loot2_count": "10-25",
                        "loot1": "🐿 шкура белки 🐿", "loot1_chance": "70%", "loot1_count": "1-3"
                },
                "🦝  Енот  🦝  (Lvl 2)": {"type": "default",
                        "loot1": "⛓ кусочек цепи ⛓", "loot1_chance": "60%", "loot1_count": "1-2",
                        "loot2": "💰 мешок монет 💰", "loot2_chance": "20%", "loot2_count": "1-3"
                },
                "Гигантский воробей 🗿  (Lvl 2)": {"type": "default",
                        "loot2": "🌾 зерно 🌾", "loot2_chance": "100%", "loot2_count": "5-7",
                        "loot1": "🥚 яйцо (Lvl 1) 🥚", "loot1_chance": "90%", "loot1_count": "1-10"
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
                        "loot3": "⚫ черная сфера ⚫", "loot3_chance": "5%", "loot3_count": "1-1"
                },
                "Загадочный призрак  👻": {"type": "bonus"}
}

bot = telebot.TeleBot('5145120712:AAHG4P6mA1SKhD-xtFbFXkb1vFvm1ew7iUY')

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
    loot_list = ["🦎 хвост ящерицы 🦎",
        "🍈 чешуя (Lvl 1) 🍈",
        "🃏 игральный камень 🃏",
        "🌰 орех 🌰",
        "🐿 шкура белки 🐿",
        "⛓ кусочек цепи ⛓",
        "💰 мешок монет 💰",
        "🌾 зерно 🌾",
        "🥚 яйцо (Lvl 1) 🥚",
        "🐁 крысиный хвост 🐁",
        "🐀 крысина шкура 🐀",
        "🥀 ядовитая роза 🥀",
        "💉 колба яд-826 💉",
        "🥩 мясо 🥩",
        "🐺 клык волка 🐺",
        "⚪ белая сфера ⚪",
        "🕸 паутинка 🕸",
        "🦗 обычный жучок 🦗",
        "⚫ черная сфера ⚫"
    ]
    ans_str = ""
    bot.send_message(message.chat.id, "Инвентарь:", reply_markup=markup)
    for i in range(len(loot_list)):
       ans_str += f"{loot_list[i]} - {lootik[i]}\n"
       ans_str += "\n"
    bot.send_message(message.chat.id, ans_str, reply_markup=markup)


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
    bot.send_message(message.chat.id, "Статистика игрока:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Lvl: {level}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Exp: {expa}/{level * 100}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Hp: {hp}/{max_h}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Damage: {damage}", reply_markup=markup)
    bot.send_message(message.chat.id, f"Crit damage: {100 + crit}% от Damage", reply_markup=markup)
    bot.send_message(message.chat.id, f"Crit chance: {chance}%", reply_markup=markup)
    bot.send_message(message.chat.id, f"Free points: {point}", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
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
    pak = ab[19].split("*")
    loot_dict = {
        "🦎 хвост ящерицы 🦎": pak[0],
        "🍈 чешуя (Lvl 1) 🍈": pak[1],
        "🃏 игральный камень 🃏": pak[2],
        "🌰 орех 🌰": pak[3],
        "🐿 шкура белки 🐿": pak[4],
        "⛓ кусочек цепи ⛓": pak[5],
        "💰 мешок монет 💰": pak[6],
        "🌾 зерно 🌾": pak[7],
        "🥚 яйцо (Lvl 1) 🥚": pak[8],
        "🐁 крысиный хвост 🐁": pak[9],
        "🐀 крысина шкура 🐀": pak[10],
        "🥀 ядовитая роза 🥀": pak[11],
        "💉 колба яд-826 💉": pak[12],
        "🥩 мясо 🥩": pak[13],
        "🐺 клык волка 🐺": pak[14],
        "⚪ белая сфера ⚪": pak[15],
        "🕸 паутинка 🕸": pak[16],
        "🦗 обычный жучок 🦗": pak[17],
        "⚫ черная сфера ⚫": pak[18]
    }
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
            stroka_basa += str(ab[0]) + "/" + str(ab[1]) + "/" + str(ab[2]) + "/"
            stroka_basa += ab[3] + "/" + ab[4] + "/" + ab[5] + "/"
            stroka_basa += str(ab[6]) + "/" + str(ab[7]) + "/" + ab[8] + "/" + str(ab[9])
            stroka_basa += "/" + str(ab[10]) + "/" + str(ab[11])
            stroka_basa += "/" + str(ab[12])+ "/" + str(ab[13]) + "/" + str(ab[14]) + "/" + str(ab[15])
            stroka_basa += "/" + str(ab[16]) + "/" + str(ab[17]) + "/" + str(ab[18]) + "/" + str(ab[19]) + "/" + str(ab[20])

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
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
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
        elif message.text == "go":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("просто лес 😐")
            btn2 = types.KeyboardButton("✨тотем✨")
            btn3 = types.KeyboardButton("⛲ фонтан надежд ⛲")
            btn4 = types.KeyboardButton("локация 4")
            btn5 = types.KeyboardButton("команды")
            btn6 = types.KeyboardButton("🔮 кузница ⚒")
            markup.add(btn1, btn4, btn6)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn5)
            bot.send_message(message.chat.id, "добро пожаловать в мир приключений", reply_markup=markup)
            bot.send_message(message.chat.id, "обучение не предусмотренно 😀", reply_markup=markup)
            bot.send_message(message.chat.id, "удачи", reply_markup=markup)
            bot.send_message(message.chat.id, "выберите локацию", reply_markup=markup)
        elif message.text == "🔮 рискнуть 🔮":
            photo1 = open('a.png', 'rb')
            bot.send_message(message.chat.id, "⚠ эта функция находится в разработке ⚠")
            bot.send_photo(message.chat.id, photo=photo1)
        elif message.text == "🔮 кузница ⚒":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("⚒ создать снаряжение ⚒")
            btn2 = types.KeyboardButton("🔮 улучшить снаряжение 🔮")
            btn3 = types.KeyboardButton("назад")
            markup.add(btn1, btn2)
            markup.add(btn3)
            bot.send_message(message.chat.id, "добро пожаловать в кузницу)", reply_markup=markup)
        elif message.text == "⚒ создать снаряжение ⚒":
            photo1 = open('a.png', 'rb')
            bot.send_message(message.chat.id, "⚠ эта функция находится в разработке ⚠")
            bot.send_photo(message.chat.id, photo=photo1)
        elif message.text == "🔮 улучшить снаряжение 🔮":
            photo1 = open('a.png', 'rb')
            bot.send_message(message.chat.id, "⚠ эта функция находится в разработке ⚠")
            bot.send_photo(message.chat.id, photo=photo1)
        elif message.text == "команды":
            komands = ""
            komands += "/start - начать с приветствия"
            komands += "\n"
            komands += "\n"
            komands += "/stats - характеристики игрока"
            komands += "\n"
            komands += "\n"
            komands += "/inventory - инвентарь игрока"
            bot.send_message(message.chat.id, komands)
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
            btn1 = types.KeyboardButton("просто лес 😐")
            btn2 = types.KeyboardButton("✨тотем✨")
            btn3 = types.KeyboardButton("⛲ фонтан надежд ⛲")
            btn4 = types.KeyboardButton("локация 4")
            btn5 = types.KeyboardButton("команды")
            btn6 = types.KeyboardButton("🔮 кузница ⚒")
            markup.add(btn1, btn4, btn6)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn5)
            bot.send_message(message.chat.id, "решили испытать удачу на новой локации ?) ", reply_markup=markup)
        elif message.text == "просто лес 😐":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in based_monstrs_of_prosstoles:
                btn = types.KeyboardButton(i)
                markup.add(btn)
            btn1 = types.KeyboardButton("назад")
            markup.add(btn1)
            bot.send_message(message.chat.id, 'Вы вошли в локацию "просто лес 😐"', reply_markup=markup)
        elif message.text in based_monstrs_of_prosstoles:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ab[16] = message.text
            if based_monstrs_of_prosstoles[message.text]["type"] == "default":
                ab[17] = str(based_monstrs_of_prosstoles[ab[16]]["hp"])
                btn1 = types.KeyboardButton("⚔️ ударить ⚔️")
            elif based_monstrs_of_prosstoles[message.text]["type"] == "bonus":
                btn1 = types.KeyboardButton("🔮 рискнуть 🔮")
            btn2 = types.KeyboardButton("🌲 вернуться назад 🌲")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, text="Информация о противнике:", reply_markup=markup)
            for i in based_monstrs_of_prosstoles[message.text]:
                bot.send_message(message.chat.id, text=i + ": " + str(based_monstrs_of_prosstoles[message.text][i]), reply_markup=markup)
            loot = ""
            if based_monstrs_of_prosstoles_loot[message.text]["type"] == "default":
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
        elif message.text == "⚔️ ударить ⚔️":
            if ab[17] == "0":
                bot.send_message(message.chat.id, text="этого джентельмена вы уже залутали сударь")
            else:
                s = ab[13].split("-")
                s1 = random.randint(int(s[0]), int(s[1]))
                ab[17] = str(int(ab[17]) - s1)
                bot.send_message(message.chat.id, text=f"вы нанесли {s1} урона")
                if int(ab[17]) <= 0:
                    bot.send_message(message.chat.id, text="hp противника: 0")
                    bot.send_message(message.chat.id, text="победа 🏆")
                    e = based_monstrs_of_prosstoles[ab[16]]["exp"]
                    bot.send_message(message.chat.id, text=f"вам начисленно: {e}exp")
                    bot.send_message(message.chat.id, text="вы получили:")
                    if "loot1" in based_monstrs_of_prosstoles_loot[ab[16]]:
                        if random.randint(1, 100) <= int(based_monstrs_of_prosstoles_loot[ab[16]]["loot1_chance"][:-1]):
                            u = based_monstrs_of_prosstoles_loot[ab[16]]["loot1_count"].split("-")
                            cou = random.randint(int(u[0]), int(u[1]))
                            loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot1"]] = str(int(loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot1"]]) + cou)
                            bot.send_message(message.chat.id, text=f'{based_monstrs_of_prosstoles_loot[ab[16]]["loot1"]} - {cou}')
                    if "loot2" in based_monstrs_of_prosstoles_loot[ab[16]]:
                        if random.randint(1, 100) <= int(based_monstrs_of_prosstoles_loot[ab[16]]["loot2_chance"][:-1]):
                            u = based_monstrs_of_prosstoles_loot[ab[16]]["loot2_count"].split("-")
                            cou = random.randint(int(u[0]), int(u[1]))
                            loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot2"]] = str(int(loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot2"]]) + cou)
                            bot.send_message(message.chat.id, text=f'{based_monstrs_of_prosstoles_loot[ab[16]]["loot2"]} - {cou}')
                    if "loot3" in based_monstrs_of_prosstoles_loot[ab[16]]:
                        if random.randint(1, 100) <= int(based_monstrs_of_prosstoles_loot[ab[16]]["loot3_chance"][:-1]):
                            u = based_monstrs_of_prosstoles_loot[ab[16]]["loot3_count"].split("-")
                            cou = random.randint(int(u[0]), int(u[1]))
                            loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot3"]] = str(int(loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot3"]]) + cou)
                            bot.send_message(message.chat.id, text=f'{based_monstrs_of_prosstoles_loot[ab[16]]["loot3"]} - {cou}')
                    if "loot4" in based_monstrs_of_prosstoles_loot[ab[16]]:
                        if random.randint(1, 100) <= int(based_monstrs_of_prosstoles_loot[ab[16]]["loot4_chance"][:-1]):
                            u = based_monstrs_of_prosstoles_loot[ab[16]]["loot4_count"].split("-")
                            cou = random.randint(int(u[0]), int(u[1]))
                            loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot4"]] = str(int(loot_dict[based_monstrs_of_prosstoles_loot[ab[16]]["loot4"]]) + cou)
                            bot.send_message(message.chat.id, text=f'{based_monstrs_of_prosstoles_loot[ab[16]]["loot4"]} - {cou}')
                    ab[11] = str(int(ab[11]) + int(e))
                    if(int(ab[11]) >= int(ab[10]) * 100):
                        ab[11] = str(int(ab[11]) - int(ab[10]) * 100)
                        ab[10] = str(int(ab[10]) + 1)
                        ab[20] = str(int(ab[20]) + 1)
                else:
                    bot.send_message(message.chat.id, text=f"hp противника: {ab[17]}")
                    g = based_monstrs_of_prosstoles[ab[16]]["damage"]
                    bot.send_message(message.chat.id, text=f"вам нанесли {g} урона")
                    ab[12] = str(int(ab[12]) - int(g))
                    if int(ab[12]) < 0:
                        ab[12] = "0"
                    bot.send_message(message.chat.id, text=f"оставшиеся hp игрока: {ab[12]}")
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
            bot.send_message(message.chat.id, "Статистика игрока:", reply_markup=markup)
            bot.send_message(message.chat.id, f"Lvl: {level}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Exp: {expa}/{level * 100}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Hp: {hp}/{max_h}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Damage: {damage}", reply_markup=markup)
            bot.send_message(message.chat.id, f"Crit damage: {100 + crit}% от Damage", reply_markup=markup)
            bot.send_message(message.chat.id, f"Crit chance: {chance}%", reply_markup=markup)
            bot.send_message(message.chat.id, f"Free points: {point}", reply_markup=markup)
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
        elif message.text == "hp" or message.text == "damage":
            if ab[20] == "0":
                bot.send_message(message.chat.id, text="недостаточно points")
            elif message.text == "hp":
                ab[20] = str(int(ab[20]) - 1)
                ab[18] = str(int(ab[18]) + 5)
                bot.send_message(message.chat.id, text= f"max hp: {int(ab[18]) - 5} --> {ab[18]}")
            elif message.text == "damage":
                ab[20] = str(int(ab[20]) - 1)
                g = ab[13].split("-")
                ab[13] = str(int(g[0]) + 1) + "-" + str(int(g[1]) + 1)
                bot.send_message(message.chat.id, text= f"min damage: {g[0]} --> {str(int(g[0]) + 1)}")
                bot.send_message(message.chat.id, text= f"max damage: {g[1]} --> {str(int(g[1]) + 1)}")
        elif message.text == "возродиться":
            ab[11] = "0"
            ab[12] = "1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("go")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="вы успешно возродились 😷", reply_markup=markup)
        elif message.text == "выпить зелье":
            ab[11] = "0"
            ab[12] = "1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("go")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="вы успешно возродились 😷", reply_markup=markup)
        elif message.text == "🌲 вернуться назад 🌲":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in based_monstrs_of_prosstoles:
                btn = types.KeyboardButton(i)
                markup.add(btn)
            btn1 = types.KeyboardButton("назад")
            markup.add(btn1)
            bot.send_message(message.chat.id, text="аххахаха не смогли смириться с поражанием", reply_markup=markup)
            bot.send_message(message.chat.id, text=" и решили все таки выбрать противника полегче ?", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
        es = ""
        for i in loot_dict:
            es += loot_dict[i]
            es += "*"
        ab[19] = es[:-1]
        stroka_basa = ""
        stroka_basa += str(ab[0]) + "/" + str(ab[1]) + "/" + str(ab[2]) + "/"
        stroka_basa += ab[3] + "/" + ab[4] + "/" + ab[5] + "/"
        stroka_basa += str(ab[6]) + "/" + str(ab[7]) + "/" + ab[8] + "/" + str(ab[9])
        stroka_basa += "/" + str(ab[10]) + "/" + str(ab[11])
        stroka_basa += "/" + str(ab[12])+ "/" + str(ab[13]) + "/" + str(ab[14]) + "/" + str(ab[15])
        stroka_basa += "/" + str(ab[16]) + "/" + str(ab[17]) + "/" + str(ab[18]) + "/" + str(ab[19]) + "/" + str(ab[20])
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