# based on https://github.com/Lepeshka92/TelegaGraph
import urequests as requests
import ujson as json


class TelegramBot(object):


    def __init__(self, token):
        self.token = token
        self.offset = 0
        self._url = 'https://api.telegram.org/bot' + token

    def _quote(self, t):
        return '%'.join('{:02x}'.format(c) for c in t)

    def send(self, chat_id, text):
        url = self._url + '/sendMessage?chat_id=' + str(chat_id) + \
              '&text=%' + self._quote(text.encode('utf-8'))

        try:
            requests.get(url)
            return True
        except:
            return False

    def update(self):
        url = self._url + '/getUpdates?timeout=30&limit=1&offset=' + \
              str(self.offset)

        try:
            r = requests.get(url)
            jo = json.loads(r.text)
        except:
            return None

        if len(jo['result']) > 0:
            self.offset = jo['result'][0]['update_id'] + 1
            if 'message' in jo['result'][0]:
                if 'text' in jo['result'][0]['message']:
                    return (jo['result'][0]['message']['chat']['id'],
                            str(jo['result'][0]['message']['from']['first_name']),
                            str(jo['result'][0]['message']['text']),
                            jo['result'][0]['message']['date'])

        return None

    def listen(self, handler):
        while True:
            message = self.update()
            if message:
                handler(message)
