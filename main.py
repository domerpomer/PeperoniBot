import telebot
import webbrowser
import random
from telebot import types
from creds import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

list_commands = ['/start']
dict_players = {}
list_imposter = []
list_games = []
game_time = ''
game_name = ''
list_guess_task = []
list_task = ['0 голов', 'Взорвать 4 раза', 'Забей в свои ворота', 'Дойти до овертайма', '5 сейва', 'Squishy save', '3 ассиста',  'забить гол от кроссбара/штанги', '']
dict_guess_task ={}




@bot.message_handler(commands=['rocketleague'])
def rocketleague(message):
    if message.from_user.first_name not in dict_players.values():           #при запуске бота все добаляются в словарь = [их чат айди]:[имя]
        dict_players[message.chat.id] = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Предатель')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Guess task!')
    markup.row(btn2)
    bot.reply_to(message, 'Какой режим?', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.first_name not in dict_players.values():           #при запуске бота все добаляются в словарь = [их чат айди]:[имя]
        bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name}!')
        dict_players[message.chat.id] = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup()                    #после высветится что человек хочет сделать
    btn3 = types.KeyboardButton('🎰Предложенные игры🎰')        #при нажатии будет отправлены все предложенные игры
    markup.row(btn3)
    btn4 = types.KeyboardButton('🕹Предложить игру🎮')          # при нажатии появится кнопки с популярными играми у нас, либо можно предложить
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name}!', reply_markup=markup)







@bot.message_handler()                                                          
def info(message):
    if message.text == '🎰Предложенные игры🎰':
        print(message)
        if len(list_games) > 0:
            count_game_invites = 0
            for game_invite in list_games:
                count_game_invites += 1
                bot.send_message(message.chat.id, str(count_game_invites)+ '. ' + game_invite)
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('🎈Вернуться назад↩')
            markup.row(btn1)
            bot.send_message(message.chat.id, 'КОНЕЦ СПИСКА', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('🎈Вернуться назад↩')
            markup.row(btn1)       
            bot.send_message(message.chat.id, 'Никто еще не предложил игру!', reply_markup=markup)
    elif message.text.lower() == '🕹предложить игру🎮':                                               #for chatids in dict_players:
        markup = types.ReplyKeyboardMarkup()                                                       #bot.send_message(chatids, f'{dict_players[message.chat.id]}') предложил сыграть в {game} в {time}!                   
        btn1 = types.KeyboardButton('🪓Sons of the forest🌲')                                      #             
        btn2 = types.KeyboardButton('⚽Rocket league🚗')                                           #     
        btn3 = types.KeyboardButton('🪂PUBG̸/̸̅̅ ̆̅ ̅̅ ̅̅')
        btn4 = types.KeyboardButton('🃏Liar`s bar🎲')
        markup.row(btn1, btn2, btn3, btn4)
        btn6 = types.KeyboardButton('сейчас')
        btn7 = types.KeyboardButton('вечером')
        btn8 = types.KeyboardButton('через час')
        btn9 = types.KeyboardButton('через 2 часа')
        markup.row(btn6, btn7, btn8, btn9)
        btn10 = types.KeyboardButton('🎈Вернуться назад↩')
        markup.row(btn10)
        bot.send_message(message.chat.id, 'Отправь название игры⬇(Либо воспользуйся кнопками!)', reply_markup=markup)
        bot.register_next_step_handler(message, get_game_name)
            
    elif message.text.lower() == 'переподключиться':
        if message.chat.id not in list_guess_task:
            list_guess_task.append(message.chat.id)
        if message.from_user.first_name not in dict_players.values():           
            dict_players[message.chat.id] = message.from_user.first_name
        if message.from_user.first_name not in dict_guess_task.keys():
            dict_guess_task[message.from_user.first_name] = 0




    elif message.text == '🎈Вернуться назад↩':
        if message.from_user.first_name not in dict_players.values():           
            dict_players[message.chat.id] = message.from_user.first_name
        markup = types.ReplyKeyboardMarkup()                    
        btn3 = types.KeyboardButton('🎰Предложенные игры🎰')        
        markup.row(btn3)
        btn4 = types.KeyboardButton('🕹Предложить игру🎮')          
        markup.row(btn4)
        bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name}!', reply_markup=markup)

#ROCKET LEAGUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    elif message.text.lower() == 'предатель':
        if message.from_user.first_name not in dict_players.values():           
            dict_players[message.chat.id] = message.from_user.first_name
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Начинаем! (сас)')
        markup.row(btn1)
        bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name}! Занес в список игры! Когда все будут готовы - нажми на кнопку', reply_markup=markup)
        if message.chat.id not in list_imposter:
            list_imposter.append(message.chat.id)


    elif message.text.lower() == 'начинаем! (сас)':
        if len(list_imposter) < 3:
            bot.send_message(message.chat.id, 'Недостаточно игроков!')
        else:
            if message.from_user.first_name not in dict_players.values():           
                dict_players[message.chat.id] = message.from_user.first_name
            for chatids in list_imposter:
                bot.send_message(chatids, f'{dict_players[message.chat.id]} начал игру!')
            random_name_imposter = random.choice(list_imposter)
            bot.send_message(random_name_imposter, 'Ты импостер!')
            list_imposter.remove(random_name_imposter)
            speed_imposter = random.randrange(0, 130, 10)
            for chatids in list_imposter:
                bot.send_message(chatids, f'Твоя скорость - {speed_imposter}')
            list_imposter.append(random_name_imposter)



    elif message.text.lower() == 'guess task!':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Начинаем! (гуесс таск)')
        btn2 = types.KeyboardButton('Переподключиться')
        markup.row(btn1, btn2)
        btn3 = types.KeyboardButton('Завершить раунд')
        btn4 = types.KeyboardButton('Показать лидерборд')
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name}! Занес в список игры! Когда все будут готовы нажми на кнопку', reply_markup=markup)
        if message.chat.id not in list_guess_task:
            list_guess_task.append(message.chat.id)
    

    elif message.text.lower() == 'начинаем! (гуесс таск)':
        list_task_copy = list_task.copy()
        random.shuffle(list_guess_task)
        for chatids in list_guess_task:
            try:
                random_task = random.choice(list_task_copy)
                list_task_copy.remove(random_task)
            except:
                random_task = 'будь афк 5 минут незаметно'
            bot.send_message(chatids, f'Все задачи -{'\n'.join(list_task)}')
            bot.send_message(chatids, f'{dict_players[message.chat.id]} начал игру!')
            bot.send_message(chatids, f'Твоя задача - {random_task}!')
    
    elif message.text == 'Завершить раунд':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Да', callback_data='give_point')
        btn2 = types.InlineKeyboardButton('Нет', callback_data='delete')
        markup.row(btn1,btn2)
        markup2 = types.ReplyKeyboardMarkup()
        #for  in dict_guess_task:
            #btn[i] = types.KeyboardButton(dict_guess_task[])
        for chatids in dict_players.keys():
            bot.send_message(chatids, 'Ты выполнил задание?', reply_markup=markup)
            bot.send_message(chatids, 'Проголосуй за задачу, которая ты думаешь ему выпала', reply_markup=markup2)
            

    
        

def get_game_name(message):
    global game_name
    game_name = message.text
    bot.send_message(message.chat.id, 'В какое время?(Пиши с преставкой "в" если указываешь конкретное время)')
    bot.register_next_step_handler(message, get_game_time)
        
def get_game_time(message):
    global game_time
    game_time = ''
    while game_time == '':
        try:
            game_time = message.text
        except Exception:
            bot.send_message(message.chat.id, 'СЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫР')
    markup = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') 
    markup.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    markup.add(key_no)
    bot.send_message(message.chat.id, f'Ты предлагаешь сыграть в {game_name} {game_time}! Опубликовать?', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'delete_name_from_list':
        bot.edit_message_text('Удалил!', callback.message.chat.id, callback.message.message_id)
        del dict_players[callback.message.chat.id]
    elif callback.data == 'yes':
        list_games.append(f'{callback.from_user.first_name} предлагает сыграть в {game_name} {game_time}. ')
        for i in range(7):
            bot.delete_message(callback.message.chat.id, callback.message.message_id-i)
        markup = types.ReplyKeyboardMarkup()                    
        btn3 = types.KeyboardButton('🎰Предложенные игры🎰')        
        markup.row(btn3)
        btn4 = types.KeyboardButton('🕹Предложить игру🎮')          
        markup.row(btn4)
        bot.send_message(callback.message.chat.id, f'Хай, {callback.from_user.first_name}!', reply_markup=markup)
        print(*list_games)
    elif callback.data == 'no':
        for i in range(7):
            bot.delete_message(callback.message.chat.id, callback.message.message_id-i)
        markup = types.ReplyKeyboardMarkup()                    
        btn3 = types.KeyboardButton('🎰Предложенные игры🎰')        
        markup.row(btn3)
        btn4 = types.KeyboardButton('🕹Предложить игру🎮')          
        markup.row(btn4)
        bot.send_message(callback.message.chat.id, f'Хай, {callback.from_user.first_name}!', reply_markup=markup)
    elif callback.data == 'give_point':
        dict_guess_task[callback.from_user.first_name] += 1
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
#print(callback.chat.id)        
#print(message.from_user.first_name)
#print([attr for attr in dir(callback) if not attr.startswith('_')])
#print(callback.from_user)
#print(callback.chat.id)    
bot.polling(none_stop=True)
