import telebot

bot = telebot.TeleBot("7026053293:AAG5lWuKcTZcH0tbfezd5tjPYCmWG8gqlqM")


@bot.message_handler(commands=["start"])
def start_hotel(message):
    bot.send_message(message.chat.id,
                     "*ЗДРАВСТВУЙТЕ) Рады приветствовать Вас!* \n*The Plaza* — это отель в городе Нью-Йорк, в 800 м от такой достопримечательности, как *РОКФЕЛЛЕРОВСКИЙ ЦЕНТР*. Рядом с *The Plaza* находятся такие популярные достопримечательности, как *Концертный зал Carnegie Hall*, Смотровая площадка в *Рокфеллер-центре* и *Музей современного искусства*. *Аэропорт Ла-Гардия* находится в *10 км*. \n_Парам особенно нравится расположение — они оценили проживание в этом районе вдвоем на *9,7*._",
                     parse_mode='Markdown')


@bot.message_handler(commands=["adress"])
def adress_hotel(message):
    bot.send_message(message.chat.id,
                     "*768 5th Avenue, New York, 10019, USA*\n_Штат Нью-Йорк, район Манхэттен, 5-я авеню, 768_",
                     parse_mode='Markdown')


@bot.message_handler(commands=["inside"])
def inside_hotel(message):
    bot.send_message(message.chat.id, "Обстановка внутри радует глаз)", parse_mode='Markdown')


@bot.message_handler(commands=["conveniences"])
def conveniences_hotel(message):
    bot.send_message(message.chat.id,
                     "К услугам гостей услуги консьержа, фитнес-центр, бар, а также бесплатный Wi-Fi на всей территории. Также предоставляются гипоаллергенные номера. В распоряжении гостей отеля с *5 звездами* — экскурсионное бюро и место для хранения багажа. В распоряжении гостей доставка еды и напитков, бизнес-центр и услуга обмена валют.\nЕжедневно гостям The Plaza предлагается американский завтрак. При *The Plaza* работает ресторан, где подают блюда американской кухни, блюда британской кухни и блюда французской кухни. Гости могут попросить приготовить вегетарианские, безлактозные и веганские блюда.\nСотрудники стойки регистрации, говорящие на арабском, на немецком, на английском и на испанском, предоставят гостям информацию о регионе.",
                     parse_mode='Markdown')


@bot.message_handler(commands=["website"])
def website_hotel(message):
    bot.send_message(message.chat.id,
                     "[*Жми на меня и бронируй поскорее номер):*](https://www.booking.com/hotel/us/the-plaza.ru.html)",
                     parse_mode='Markdown')


bot.infinity_polling()