
import time
import typing

import telebot
from telebot import types

TOKEN = '1826903678:AAEIczJXIb03N2okBY_N2RDe92HLUpcJ-44'

knownUsers = [] 
userStep = {}  

commands = { 
    
    'start'         : 'Iniciar el bot\n\n',
    'help'          : 'Muestra los comandos disponibles\n\n',
    'conversion'    : 'Use este comando para mostrar el teclado de conversión de unidades\n\n',
    'chatcomands'   : 'Cargará una lista de comandos, con los cuales el bot y usted podrán intercambiar textos. \nRecuerde, este comando solo despliega una lista de textos con los cuales el bot dará una respuesta\n\n¡Diviertete!'
    
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  
imageSelect.add('Milímetro', 'Centímetro', 'Metro', 'Kilómetro','Pulgada' ,'Yarda','Milla')

hideBoard = types.ReplyKeyboardRemove()  


def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuarios detectado, pero no ha usado \"/start\" ")
        return 0


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
                    print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener) 


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers: 
        
        knownUsers.append(cid)  
        userStep[cid] = 0 
        bot.send_message(cid, '¡Hola!')
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        bot.send_message(cid, "Estoy acá para ayudarte")
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        command_help(m) 
    else:
        bot.send_message(cid, "Ya usaste el comando /start, usa el comando /help para visualizar más comandos\n\nÓ bien puedes usar el comando /conversion para realizar una conversion de unidad\n\nPero, si deseas tener una conversacion amena con el bot usa /chatscomands")
        bot.send_chat_action(cid, 'typing')  
        time.sleep(4)

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguientes comandos están disponibles:\n\n\n"
    bot.send_chat_action(cid, 'typing')  
    time.sleep(5)
    for key in commands: 
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  



@bot.message_handler(commands=['chatcomands'])
def command_long_text(m):
    cid = m.chat.id
    bot.send_message(cid, "Puede escribir estas palabras y mantener una conversacion con el bot")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "hola")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "hi")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "hey")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Hola")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Hi")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Hey")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Como estas?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Saludos")  
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "como estas?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "edad")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Edad?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Cual es tu edad?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Cual es tu edad")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "cual es tu edad")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "cual es tu edad?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Cual es tu sexo?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "cual es tu sexo?")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Cual es tu sexo")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "cual es tu sexo")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)
    bot.send_message(cid, "Gracias")
    bot.send_chat_action(cid, 'typing')
    time.sleep(5)
    bot.send_message(cid, "Si usas una secuencia de palabras que no esten incluida en esta lista, lamentablemente el bot no podrá responderte de la manera que tu deseas, amigo. ")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(3)
    bot.send_message(cid, "No fui programado para autoaprender, todas mis respuestas fueron previamente programadas.")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(3)
    bot.send_message(cid, "RECUERDE:\n\nESTE ES SOLO UN LISTADO DE LAS PALABRAS QUE USTED COMO USUARIO LE PUEDE ENVIAR AL BOT Y AUTOMATICAMENTE OBTENER UNA RESPUESTA DEL BOT")
    bot.send_chat_action(cid, 'typing')  
    time.sleep(1)


@bot.message_handler(commands=['conversion'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Presiona la tecla de tu preferencia para mostrar la conversion de la opcion seleccionada a las demas unidades de area ", reply_markup=imageSelect)  
    userStep[cid] = 1 



@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

   
    if text == 'Milímetro':
        bot.send_message(cid, "Has seleccionado la unidad: \nMilímetro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Milímetro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('mm\mm a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('mm\mm a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('mm\mm a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Centímetro':
        bot.send_message(cid, "Has seleccionado la unidad: \nCentímetro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Centímetro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('cm\cm a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('cm\cm a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('cm\cm a yarda.png', 'rb'),
                       reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Metro':
        bot.send_message(cid, "Has seleccionado la unidad: \nMetro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Metro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('m\m a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('m\m a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('m\m a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Kilómetro':
        bot.send_message(cid, "Has seleccionado la unidad: \nKilometro")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Kilometro a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('km\km a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('km\km a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('km\km a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Pulgada':
        bot.send_message(cid, "Has seleccionado la unidad: \nPulgada")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Pulgada a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('plg\plg a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('plg\plg a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('plg\plg a yarda.png', 'rb'),
                       reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

    elif text == 'Yarda':
        bot.send_message(cid, "Has seleccionado la unidad: \nYarda")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Yarda a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a mila.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('yarda\yarda a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('yarda\yarda a plg.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('yarda\yarda a yarda.png', 'rb'),
                       reply_markup=hideBoard) 

        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0   

    elif text == 'Milla':
        bot.send_message(cid, "Has seleccionado la unidad: \nMilla")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "A continuacíon se le mostrará la conversion de la unidad Milla a otras unidades de area")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a cm.png', 'rb'),
                       reply_markup=hideBoard)  
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a m.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a milla.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a mm.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('milla\milla a yarda.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('milla\milla km.png', 'rb'),
                       reply_markup=hideBoard) 
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3) 
        bot.send_photo(cid, open('milla\milla plg.png', 'rb'),
                       reply_markup=hideBoard) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Usa el comando /conversion para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "😁")
        userStep[cid] = 0 

       
       
    else:
        bot.send_message(m.chat.id, "No entiendo el texto:\"" + m.text + "\"\nIntenta usar /help para visualizar la lista de comandos disponibles")
        bot.send_message(cid, "Vamos, intentalo de nuevo. ")
        bot.send_message(cid, "😄👍")

   
@bot.message_handler(func=lambda message: message.text == "hola")
def command_text_hola(m):
    bot.send_message(m.chat.id, "Hola")


@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "No doy respuestas en ese idioma")


@bot.message_handler(func=lambda message: message.text == "hey")
def command_text_hey(m):
    bot.send_message(m.chat.id, "hey, que onda?")


@bot.message_handler(func=lambda message: message.text == "Hola")
def command_text_Hola(m):    
    bot.send_message(m.chat.id, "Hola")


@bot.message_handler(func=lambda message: message.text == "Hi")
def command_text_Hi(m):
    bot.send_message(m.chat.id, "hi, brother")


@bot.message_handler(func=lambda message: message.text == "Hey")
def command_text_Hey(m):
    bot.send_message(m.chat.id, "¿Que me contás?")


@bot.message_handler(func=lambda message: message.text == "Como estas?")
def command_text_Como_estas(m):
    bot.send_message(m.chat.id, "Bien y vos?")


@bot.message_handler(func=lambda message: message.text == "Saludos")
def command_text_Saludos(m): 
    bot.send_message(m.chat.id, "Gusto saludarte")


@bot.message_handler(func=lambda message: message.text == "edad")
def command_text_edad(m):
    bot.send_message(m.chat.id, "Cuantos me calculas?")


@bot.message_handler(func=lambda message: message.text == "Edad?")
def command_text_Edad(m):
    bot.send_message(m.chat.id, "No sé")


@bot.message_handler(func=lambda message: message.text == "Cual es tu edad?")
def command_text_Cual_es_tu_edad(m):
    bot.send_message(m.chat.id, "Ya estoy en la tercra edad")


@bot.message_handler(func=lambda message: message.text == "Cual es tu edad")
def command_text_Cual_es_tu_edad(m):
    bot.send_message(m.chat.id, "40 y pico jajaja no te creas naci hace 5 dias")


@bot.message_handler(func=lambda message: message.text == "cual es tu edad")
def command_text_cual_es_tu_edad(m):
    bot.send_message(m.chat.id, "Deja de hacer tantas preguntas incomodas")


@bot.message_handler(func=lambda message: message.text == "cual es tu edad?")
def command_text_Cual_es_tu_edad(m):
    bot.send_message(m.chat.id, "Averigualo")


@bot.message_handler(func=lambda message: message.text == "Cual es tu sexo?")
def command_text_Cual_es_tu_sexo(m):
    bot.send_message(m.chat.id, "Soy un bot no, tengo sexo, jaja")


@bot.message_handler(func=lambda message: message.text == "cual es tu sexo?")
def command_text_cual_es_tu_sexo(m):
    bot.send_message(m.chat.id, "Soy un bot no, tengo sexo, jaja")


@bot.message_handler(func=lambda message: message.text == "Cual es tu sexo")
def command_text_cual_es_tu_sexo(m):
    bot.send_message(m.chat.id, "Soy un bot no, tengo sexo, jaja")


@bot.message_handler(func=lambda message: message.text == "cual es tu sexo")
def command_text_cual_es_tu_sexo(m):
    bot.send_message(m.chat.id, "Soy un bot no, tengo sexo, jaja")

@bot.message_handler(func=lambda message: message.text == "Gracias")
def command_text_Gracias(m):

    bot.send_message(m.chat.id, "Fue un gusto, vuelve cuando quieras")



@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    bot.send_message(m.chat.id,"No entiendo el texto:\"" + m.text + "\"\nIntenta usar /help para visualizar la lista de comandos disponibles")
    bot.send_message(m, "Vamos, intentalo de nuevo. ")
    bot.send_message(m, "😄👍")

bot.infinity_polling()