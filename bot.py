import telebot
from telebot import types
from telebot import telebot
import func
from func import Result
import math


bot = telebot.TeleBot('2061536097:AAF_nC-l-FA53QePd7I_MXaxKVEHFN2uEaI')

vp_5 = {'2' : [i for i in range(0,25)], 
        '3' : [i for i in range(25,50)], 
        '4' : [i for i in range(50,150)],
        '6' : [i for i in range(150,250)],
        '8' : [i for i in range(250,550)],
       '16' : [i for i in range(500,1000)]}

vvk_3 = {'4' : [i for i in range(0,25)],
         '8' : [i for i in range(25,50)],
        '13' : [i for i in range(50,150)],
        '20' : [i for i in range(150,250)],
        '31' : [i for i in range(250,550)],
        '38' : [i for i in range(500,1000)]}

@bot.message_handler(commands=['start']) 
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, если хочешь произвести расчёт огнетушителей нажми /razchet. Если хочешь проверить соответствие количества нажми /sootvetstvie ! для прочего /TO /znak ')
            
@bot.message_handler(commands=['help'])  
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(telebot.types.InlineKeyboardButton('Написать автору', url = 'https://web.telegram.org/z/'))  
    bot.send_message(message.chat.id, 'Если у тебя есть вопросы или пожелание напиши мне', reply_markup=keyboard)

@bot.message_handler(commands=['podskazka'])  
def podskazka_command(message):  
    bot.send_message(message.chat.id, 'Огнетушители должны проходить ежегодное ТО нажми /TO \n'
                                      'чтобы узнать как проверить актуальность технического обслуживания.\n'
                                      'Огнетушители не могут эксплуатироваться больше 10 лет.\n'
                                      'Огнетушители должны распологаться на самом видном месте\n' 
                                      'Огнетушители должны быть помечены знаком /znak !')

@bot.message_handler(commands=['TO'])
def TO_command(message):  
    bot.send_photo(message.chat.id, open('D:/project/2.jpg', 'rb'))
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(telebot.types.InlineKeyboardButton('Написать автору', url = 'https://web.telegram.org/z/'))  
    bot.send_message(message.chat.id, 'Если у тебя есть вопросы или пожелание напиши мне', reply_markup=keyboard)


@bot.message_handler(commands=['znak'])  
def znak_command(message):  
    bot.send_photo(message.chat.id, open('D:/project/1.jpeg', 'rb'))
    
    
@bot.message_handler(commands=['razchet'])
def razchet_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(telebot.types.InlineKeyboardButton('Офис', callback_data='get-of'))  
    keyboard.row(telebot.types.InlineKeyboardButton('Производство', callback_data= 'get-pr'))  


    bot.send_message(message.chat.id,'Выберите необходимую локацию: ', reply_markup=keyboard )   
    
    
@bot.message_handler(commands=['sootvetstvie'])
def sootvetstvie_command(message):
	keyboard = telebot.types.InlineKeyboardMarkup() 
	keyboard.row(telebot.types.InlineKeyboardButton('ВВК-3.5', callback_data = 'vvk'))  
	keyboard.row(telebot.types.InlineKeyboardButton('ВП-5', callback_data = 'vp')) 
	
	bot.send_message(message.chat.id,'Выберите марку огнетушитля: ', reply_markup=keyboard) 

@bot.callback_query_handler(func=lambda call: True)	
def call_rashet(message):
    if message.data == "get-pr":
        bot.send_message(message.from_user.id, "Укажите площадь локации !")
        bot.register_next_step_handler(message.message, say_1)
    elif message.data == 'get-of':
        bot.send_message(message.from_user.id, 'Укажите количество кабинетов !')
        bot.register_next_step_handler(message.message, say_2)
    elif message.data == 'vvk':
        bot.send_message(message.from_user.id, 'Укажите количество огнетушителей !')
        bot.register_next_step_handler(message.message, vvk)
    elif message.data == 'vp':
        bot.send_message(message.from_user.id, 'Укажите количество огнетушителей !')
        bot.register_next_step_handler(message.message, vp)    
                
def say_1(message):
	global square
	square = message.text
	b = float(square)
	a = Result(b, 0)
	bot.send_message(message.chat.id, f'{a.proizvodstvo()}')
		
    
def say_2(message):
    global q
    q = message.text
    msg = bot.send_message(message.from_user.id, "Укажите площадь локации !")
    bot.register_next_step_handler(msg, say_3)

def say_3(message):
    global sq;
    sq = message.text
    d = float(sq)
    a = Result(d, q)
    bot.send_message(message.chat.id, f'{a.ofice()}')

@bot.message_handler(commands=['sootvetstvie'])
def sootvetstvie_command(message):
	keyboard = telebot.types.InlineKeyboardMarkup() 
	keyboard.row(telebot.types.InlineKeyboardButton('ВВК-3.5', callback_data = 'vvk'))  
	keyboard.row(telebot.types.InlineKeyboardButton('ВП-5', callback_data = 'vp')) 
	
	bot.send_message(message.chat.id,'Выберите марку огнетушитля: ', reply_markup=keyboard)  
      
             
def vvk(message):
	global num
	num = message.text 
	msg = bot.send_message(message.from_user.id, "Укажите площадь локации !")
	bot.register_next_step_handler(msg, res_vvk)
	
def vp(message):
	global num
	num = message.text 
	msg = bot.send_message(message.from_user.id, "Укажите площадь локации !")
	bot.register_next_step_handler(msg, res_vp)

def res_vvk(message):
	global square
	try:
		square = message.text 
		if square in vvk_3.get(str(num)):
			bot.send_message(message.from_user.id, 'Количество огнетушителей соответствует норме')
		elif square not in vvk_3.get(str(num)):
			bot.send_message(message.from_user.id, 'Количество огнетушителей не соответствует норме')
	except:
		bot.send_message(message.from_user.id,'Количество огнетушителей не соответствует норме')

def res_vp(message):
	global square
	try:
		square = message.text 
		if square in vp_5.get(str(num)):
			bot.send_message(message.from_user.id,'Количество огнетушителей соответствует норме')
		elif square not in vp_5.get(str(num)):
			bot.send_message(message.from_user.id,'Количество огнетушителей не соответствует норме')
	except:
		bot.send_message(message.from_user.id,'Количество огнетушителей не соответствует норме')
		
		
if __name__ == '__main__': 
	bot.polling(none_stop=True)
