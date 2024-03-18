import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)



def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = '🦷Услуги'
    btn2 = '🏥\nО клинике'
    btn4 = '💬\nЗаписаться на прием'
    btn5 = "👨‍⚕️👩‍⚕️Наша команда"
    btn6 = '📞📩\nКонтакты'
    btn7 = '💰Мои бонусы'
    btn8 = 'Фелиал Бетанкура 29'
    markup.add(btn1, btn2, btn4, btn5, btn6, btn7,btn8)
    return markup


def comanda():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = '🏡Главное меню'
    btn2 = '🏆Наши достижения'
    markup.add(btn1, btn2)
    return markup


def info():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = '🏡Главное меню'
    markup.add(btn2)
    return markup


def services():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Хирургия/имплантология", callback_data='1')
    btn2 = types.InlineKeyboardButton(text="Ортопедия", callback_data='2')
    btn3 = types.InlineKeyboardButton(text="Терапия", callback_data='3')
    btn4 = types.InlineKeyboardButton(text="Ортодонтия", callback_data='4')
    btn5 = types.InlineKeyboardButton(text="Главное меню", callback_data='5')

    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data.startswith('1'):
        img1 = open('image/хирургия.jpg', 'rb')
        bot.send_photo(call.message.chat.id, img1)
        bot.send_message(call.message.chat.id, text='🦷Консультация и диагностика стоматолога-имплантолога 500₽\n'
                                                    'Удаление зуба от 2600. Удаление зуба мудрости от 4000₽\n'
                                                    'Имплантат MIS SEVEN (Израиль) с установкой -27000₽\n'
                                                    'Имплантат MIS Seven под ключ(установка имплантата+коронка) от 54000₽\n'
                                                    'Имплантат Dentium (Корея) с установкой 34000₽\n'
                                                    'Имплантат Dentium под ключ( установка имплантата+коронка) от 65000₽\n',
                         reply_markup=services())
    if call.data.startswith('2'):
        img2 = open('image/ортопедия.jpg', 'rb')
        bot.send_photo(call.message.chat.id, img2)
        bot.send_message(call.message.chat.id, text='🦷Консультация и диагностика стоматолога-ортопеда - 500 ₽\n'
                                                    'Коронка металлокерамическая стандартная эстетика - от 12 500 ₽\n'
                                                    'Коронка металлокерамическая эстетическая с установкой (под ключ) - от '
                                                    '19 000 ₽\n'
                                                    'Коронка металлокерамическая на имплантат - от 19 500 ₽\n'
                                                    'Коронка керамическая на основе диоксида циркония – 27 000-33 000₽\n'
                                                    'Винир: безметалловая керамика – от 25 000 ₽\n'
                                                    'Съемный протез из акриловой пластмассы (1 челюсть) 30 000-40 000₽\n'
                                                    'Полный съемный протез из пластмассы Acry-Free (1 челюсть) – 60 000 ₽\n'
                         , reply_markup=services())
    if call.data.startswith('3'):
        img3 = open('image/терапия.jpg', 'rb')
        bot.send_photo(call.message.chat.id, img3)
        bot.send_message(call.message.chat.id, text='🦷Консультация и диагностика стоматолога-терапевта - 500 ₽\n'
                                                    'Лечение кариеса от 3800 ₽\n'
                                                    'Лечение кариеса системой Icon (без бормашины) – от 6500 ₽\n'
                                                    'Лечение пульпита зуба – от 7000 ₽\n', reply_markup=services())

    if call.data.startswith('4'):
        img4 = open('image/ортодонтия.jpg', "rb")
        bot.send_photo(call.message.chat.id, img4)
        bot.send_message(call.message.chat.id, text='🦷Консультация и диагностика врача-ортодонта - 500 ₽\n'
                                                    'Брекет-система с установкой (1 челюсть) – от 25000₽\n',
                         reply_markup=services())
    if call.data.startswith('5'):
        bot.send_message(call.message.chat.id, text='Добро пожаловать! Вас приветствует официальный робот-помощник '
                                                    'стоматологической клиники "Феличита". Здесь вы можете подробнее узнать'
                                                    ' о клинике и записаться на прием', reply_markup=main_menu())


def contacts():
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton(text='Telegram', url='https://t.me/Felichitatom')
    markup.add(btn2)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='😀Добро пожаловать!\n Вас приветствует официальный робот-помощник '
                                           'стоматологической клиники "Феличита". Здесь вы можете подробнее узнать о '
                                           'клинике и записаться на прием.', reply_markup=main_menu())


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "👨‍⚕️👩‍⚕️Наша команда":
        img1 = open('image/лпф.jpg', 'rb')
        bot.send_photo(message.chat.id, img1, caption='Лынов Петр Федорович, врач-стоматолог-ортопед высшей категории, '
                                                      'главный врач клиники')
        img2 = open('image/абрамова.jpg', 'rb')
        bot.send_photo(message.chat.id, img2, caption='Абрамова Елена Евгеньевна, врач-стоматолог-терапевт')
        img3 = open('image/лида.jpg', "rb")
        bot.send_photo(message.chat.id, img3, caption='Васильева Лидия Николаевна, врач-стоматолог-хирург, имплантолог')
        img4 = open('image/женч.jpg ', 'rb')
        bot.send_photo(message.chat.id, img4, caption='Сумская Евгения Ивановна, врач-стоматолог-терапевт')
        img5 = open('image/ястребова.jpg', 'rb')
        bot.send_photo(message.chat.id, img5, caption='Ястребова Екатерина Олеговна,врач-ортодонт')
        img6 = open('image/лог.jpg', 'rb')
        bot.send_photo(message.chat.id, img6, caption='Логачёва  Надежда Васильевна, врач-стоматолог-терапевт')
        img7 = open('image/надя.jpg', 'rb')
        bot.send_photo(message.chat.id, img7,
                       caption='Николаева Надежда Ивановна,врач-стоматолог-терапевт, пародонтолог',
                       reply_markup=comanda())
        img8= open('image/катя.jpg', 'rb')
        bot.send_photo(message.chat.id,img8,caption='Лынова Екатерина Николаевна, врач-стоматолог-ортопед',
                       reply_markup=comanda())

    if message.text == '🏥\nО клинике':
        bot.send_message(message.chat.id,
                         text='*Стоматология ФЕЛИЧИТА предоставляет профессиональные услуги высокого уровня.\n'
                              'Наша стоматология  отличается рядом преимуществ, которые делают ее выбором множества '
                              'пациентов:*\n'
                              '1️⃣ Широкий спектр медицинских услуг. Здесь Вы можете получить помощь в терапии, '
                              'хирургии, ортодонтии, имплантологии, эстетической стоматологии и многое другое\n'
                              '2️⃣ Современное оборудование и передовые технологии. Это позволяет '
                              'не только точно и эффективно диагностировать проблемы пациента, но и проводить лечение '
                              'с применением инновационных методов\n'
                              '3️⃣ Индивидуальный подход, учитывая особенности здоровья и пожелания'
                              'клиента.\n'
                              'Эти преимущества делают стоматологию ФЕЛИЧИТА привлекательным выбором для многих людей,'
                              'и подтверждают ее репутацию в качественной стоматологии.👌\n'
                              'С заботой о Вас стоматологическая клиника ФЕЛИЧИТА❤️\n', parse_mode='Markdown',
                         reply_markup=info())
    if message.text == '🦷Услуги':
        bot.send_message(message.chat.id, text='Позвольте позаботится о здоровье вашей улыбки профессионалам!')
        bot.send_message(message.chat.id, text='Пожалуйста выберите услугу', reply_markup=services())

    if message.text == '🏡Главное меню':
        bot.send_message(message.chat.id, text='Добро пожаловать! Вас приветствует официальный робот-помощник '
                                               'стоматологической клиники "Феличита". Здесь вы можете подробнее узнать'
                                               ' о клинике и записаться на прием', reply_markup=main_menu())
    if message.text == '💰Мои бонусы':
        img1 = open('image/-1.jpg', 'rb')
        bot.send_photo(message.chat.id, img1)
        img2 = open('image/-2.jpg', 'rb')
        bot.send_photo(message.chat.id, img2, reply_markup=info())
        bot.send_message(message.chat.id, text='*Присоединиться к нашей бонусной программе можно по ссылке:*\n'
                                               'https://felichita.uds.app/c/join?ref=rutj4648',parse_mode="Markdown",
        reply_markup=info())


    if message.text == '💬\nЗаписаться на прием':
        bot.send_message(message.chat.id, text='Telegram', reply_markup=contacts())

    if message.text == '📞📩\nКонтакты':
        img2 = open('image/felichita.jpg', 'rb')
        bot.send_photo(message.chat.id, img2)
        bot.send_message(message.chat.id, text='Мы находимся в Нижнем Новгороде, на улице Мануфактурная, дом 10.\n'
                                               'Ссылка на яндекс карты - https://yandex.ru/maps/org/felichita/1407739629\n'
                                               'Ссылка на сайт - https://felichita-stom.ru/ '
                                               '\nНомер телефона  +7 (831) 218-02-30',
                         reply_markup=info())

    if message.text == '🏆Наши достижения':
        img10 = open('image/топ 10.jpg', 'rb')
        bot.send_photo(message.chat.id, img10)
        img11 = open('image/т1.jpg', 'rb')
        bot.send_photo(message.chat.id, img11)
        img12=open('image/Снимок.jpg','rb')
        bot.send_photo(message.chat.id,img12)

        bot.send_message(message.chat.id, text='*Мы 3 года подряд в премии Продокторов входим в топ-10 клиник Нижнего '
                                               'Новгорода и Нижегородской области* ', parse_mode='Markdown',
                         reply_markup=comanda())
    if message.text == 'Фелиал Бетанкура 29🦷':
        bot.send_message(message.chat.id,
                         text='https://drive.google.com/drive/folders/1GqY20L5RJYeRG82L5T-UE-au_q2XNLhw?usp=drive_link',
                         reply_markup=info())


bot.polling(non_stop=True)
