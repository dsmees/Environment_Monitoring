#front room temp and humidity monitor
#checking the see the effects of a dehumidifier when clothes washing has been
#in a room for 1 hour

import serial
import time
import csv
import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

def humidity_handler(update, context):
    str_to_send = " The humidity of the room as of the last reading is: " + (humidity) + "%"
    context.bot.send_message(chat_id=update.effective_chat.id, text = str_to_send)

print("Init telegram Bot")
chat_id = "-871594984"
with open ("/home/djsme94/.local/share/.telegram_bot_token", "r") as f:
    telegram_token = f.read().rstrip()
#bot = Bot(token=telegram_token)
updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('humidity', humidity_handler))
updater.start_polling()
print("Telegram bot ready")
#updater.idle()

print("Trying to connect to Serial...")
while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
        print("Successfully connected to Serial!")
        break
    except serial.SerialException:
        print("Could not connect to Serial. Retrying in 1 second..")
        time.sleep(1)
        
time.sleep(3)
ser.reset_input_buffer()
print("Serial, ok")
file = open ("Humidity.csv","w")

try:
    while True:
            time.sleep(0.01)
            if ser.in_waiting > 0:
                    humidity = ser.readline().decode('utf-8').rstrip()
                    file.write(str(humidity) + "\n")
                    file.flush()
                    time.sleep(5)
                    print("The humidity of the room is : " )
                    print((humidity)+ "%")
                    #time.sleep(5)
                    humidity = int(str(humidity))
                    if (humidity > 80):
                        print("Humidity high, consider turning on the dehumidifier")
                    else:
                        print("Humidity in room ok")
                    
                    
                    

        
except KeyboardInterrupt:
    print("---")
    print("Closing Serial communication")
    ser.close()
    print("Stopping serial comms to the humidity sensor")
    print("End of program")
    
