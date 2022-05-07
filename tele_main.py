# based on https://github.com/Lepeshka92/TelegaGraph
import gc
from machine import UART

import tele_api as api
import myBots
#from qr204 import QR204

#printer = QR204(UART(1, 9600))
myBot= myBots.SetTestTron()

telegram = api.TelegramBot(myBot.ac)

def message_handler(message):
    if message[2] == '/start':
        telegram.send(myBot.gid, 'Send me Message')
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
        telegram.send(myBot.gid, 'Message printed: ')
    gc.collect()

telegram.listen(message_handler)
