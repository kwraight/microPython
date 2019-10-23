# based on https://github.com/Lepeshka92/TelegaGraph
import gc
from machine import UART

import tele_api as api
import myBots
#from qr204 import QR204

#printer = QR204(UART(1, 9600))
myBot= myBots.SetPpeFriend()

telegram = api.TelegramBot(myBot.botAC)

def message_handler(message):
    if message[2] == '/start':
        telegram.send(-297635338, 'Send me Message')
    else:
        '''
        printer.uline_enbl()
        printer.write('From: ')
        printer.write(message[1])
        printer.uline_dsbl()

        printer.newline(1)
        printer.write(message[2])
        printer.newline(1)
        printer.write('_ ' * 16)
        printer.newline()
        '''
        telegram.send(-297635338, 'Message printed: ')
    gc.collect()

telegram.listen(message_handler)
