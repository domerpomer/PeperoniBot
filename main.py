import telebot
import webbrowser
import random
from telebot import types
from creds import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

list_commands = ['/start']
dict_players = {449182895:'Richard', 340041815:'Kamil', 6592001230:'Damir', 408119: 'ymid', 316889: 'udaf', 658390: 'nhoe', 169827: 'qgvg', 336413: 'rwnr', 163730: 'hmin', 390260: 'feih', 397265: 'jvjv', 150994: 'kzwr', 519865: 'gidt', 779129: 'sqmw', 408264: 'zrmf', 280381: 'tgui', 827189: 'pkui', 759269: 'hyes', 756885: 'wgjh', 904749: 'xpep', 441279: 'typz', 135449: 'iimi', 230851: 'fbfp', 290552: 'rajy', 915393: 'iast', 759081: 'hibf', 913096: 'rryf', 588067: 'zgbd', 166730: 'eftl', 794892: 'swzc', 870471: 'tgnf', 604801: 'klko', 713244: 'mjep', 657844: 'dzof', 424925: 'tmdm', 682286: 'srly', 766575: 'ydqz', 787946: 'hlfa', 103196: 'hoeu', 257323: 'logn', 792295: 'xodo', 654061: 'eziz', 254114: 'czpx', 272905: 'uqeu', 414007: 'qlwq', 518609: 'ymmo', 985885: 'wnxw', 633698: 'rhkj', 385232: 'ietz', 475315: 'bwil', 461430: 'dhin', 668270: 'jnaz', 427710: 'dksv'}
list_imposter = []
list_games = []
game_time = ''
game_name = ''

#rocket league mini game guess task!
list_task = ['0 голов', 'Взорвать 4 раза', 'Забей в свои ворота', 'Дойти до овертайма', '5 сейва', 'Squishy save', '3 ассиста',  'забить гол от кроссбара/штанги']
dict_guess_task_id_x_players = {449182895:'Richard', 340041815:'Kamil', 6592001230:'Damir'}
dict_guess_task_player_x_score = {'Ян': 67}
dict_guess_task_player_x_task = {}




@bot.message_handler(commands=['rocketleague'])
def rocketleague(message):
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
        if message.chat.id not in dict_guess_task_id_x_players.keys():
            dict_guess_task_id_x_players[message.chat.id] = message.from_user.first_name
        if message.chat.id not in dict_guess_task_player_x_score.keys():           
            dict_guess_task_player_x_score[message.from_user.first_name] = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Начинаем! (гуесс таск)')
        markup.row(btn1)
        #btn3 = types.KeyboardButton('Завершить раунд')
        #btn4 = types.KeyboardButton('Показать лидерборд')
        #markup.row(btn3, btn4)
        bot.send_message(message.chat.id, f'Хай, {message.from_user.first_name}! Занес в список игры! Когда все будут готовы нажми на кнопку', reply_markup=markup)
        if message.chat.id not in dict_guess_task_id_x_players.keys():
            dict_guess_task_id_x_players[message.chat.id] = message.from_user.first_name


    
    

    elif message.text.lower() == 'начинаем! (гуесс таск)':
        if message.chat.id not in dict_guess_task_id_x_players.keys():
            dict_guess_task_id_x_players[message.chat.id] = message.from_user.first_name
        if message.chat.id not in dict_guess_task_player_x_score.keys():           
            dict_guess_task_player_x_score[message.from_user.first_name] = 0


        list_task_copy = list_task.copy()
        for chatids in dict_guess_task_id_x_players.keys():
            try:
                random_task = random.choice(list_task_copy)
                list_task_copy.remove(random_task)
            except:
                random_task = 'будь афк 5 минут незаметно'
            bot.send_message(chatids, f'Все задачи -{'\n'.join(list_task)}')
            bot.send_message(chatids, f'{dict_guess_task_id_x_players[message.chat.id]} начал игру!')
            bot.send_message(chatids, f'Твоя задача - {random_task}!')
            dict_guess_task_player_x_task[dict_guess_task_id_x_players[chatids]] = random_task
    
#     elif message.text.lower() == 'показать лидерборд':
#         if message.chat.id not in dict_guess_task_id_x_players.keys():
#             dict_guess_task_id_x_players[message.chat.id] = message.from_user.first_name
#         if message.chat.id not in dict_guess_task_player_x_score.keys():           
#             dict_guess_task_player_x_score[message.from_user.first_name] = 0
#         ranked_list = [(player, score) for player, score in dict_guess_task_player_x_score.items()]
#         ranked_list.sort(key=lambda x: -x[1])
#         bot.send_message(message.chat.id, 'Таблица лидеров:')
#         for i, (player, score) in enumerate(ranked_list):
#             bot.send_message(message.chat.id, f'{i+1}. {player}: {score}')
        
    
    
#     elif message.text == 'Завершить раунд':
#         if message.chat.id not in dict_guess_task_id_x_players.keys():
#             dict_guess_task_id_x_players[message.chat.id] = message.from_user.first_name
#         if message.chat.id not in dict_guess_task_player_x_score.keys():           
#             dict_guess_task_player_x_score[message.from_user.first_name] = 0
#         list_player = list(dict_guess_task_id_x_players.keys())
#         markup_task_complete = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton('Да', callback_data='give_point')
#         btn2 = types.InlineKeyboardButton('Нет', callback_data='delete')
#         markup_task_complete.row(btn1,btn2)
        
          
#         for chatids in dict_guess_task_id_x_players.keys():
#             bot.send_message(chatids, 'Ты выполнил задание?', reply_markup=markup_task_complete)
#             for chatids2 in dict_guess_task_id_x_players.keys():
#                 markup_voit = types.InlineKeyboardMarkup()
#                 for i in range(0, len(list_task), 2):
#                     if i + 1 < len(list_task):
#                         btn_on_the_first_collumn = types.InlineKeyboardButton(list_task[i])
#                         btn_on_the_second_collumn = types.InlineKeyboardButton(list_task[i+1])
#                         markup_voit.row(btn_on_the_first_collumn, btn_on_the_second_collumn)
#                     else:
#                         btn_if_cnt_players_odd = types.InlineKeyboardButton(list_task[i])
#                         markup_voit.row(btn_if_cnt_players_odd)
#                     bot.send_message(chatids, f'Проголосуй за {dict_guess_task_id_x_players[chatids2]} и выбери его задачу', reply_markup=markup_voit)
#                     #bot.register_next_step_handler(message, vote_for_a_task)
    

    

#     elif message.text == 'ID':
#         print(message.chat.id, message.from_user.first_name)


# def vote_for_a_task(message):
#     if message.text in dict_guess_task_id_x_players.values():
#         global player_voited
#         player_voited = message.text
#         markup_voit2 = types.InlineKeyboardMarkup()
#         for i in range(0, len(list_task), 2):
#             if i + 1 < len(list_task):
#                 print(list_task[i])
#                 print(list_task[i])
#                 btn_on_the_first_collumn = types.InlineKeyboardButton(list_task[i])
#                 btn_on_the_second_collumn = types.InlineKeyboardButton(list_task[i+1])
#                 markup_voit2.row(btn_on_the_first_collumn, btn_on_the_second_collumn)
#             else:
#                 btn_if_cnt_players_odd = types.InlineKeyboardButton(list_task[i])
#                 markup_voit2.row(btn_if_cnt_players_odd)
#         bot.send_message(message.chat.id, 'Проголосуй за задачу, которая ты думаешь выпала человеку', reply_markup=markup_voit2)
#         bot.register_next_step_handler(message, check_right_task)

# def check_right_task(message):
#     if message.text == dict_guess_task_player_x_task[player_voited]:
#         bot.send_message(message.chat.id, 'Ты угадал. Получай очко')
#         dict_guess_task_player_x_score[message.from_user.first_name] += 1
#     else:
#         bot.send_message(message.chat.id, 'Увы ты не угадал. Получай в очко')
        


    
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
        dict_guess_task_player_x_score[callback.from_user.first_name] += 1
        bot.delete_message(callback.message.chat.id, callback.message.message_id) 
bot.polling(none_stop=True)
