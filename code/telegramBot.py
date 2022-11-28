#demo class of telegram bot using telegram API

import telegram

class t3legram:
    def __init__(self, token: str):
        self.bot = telegram.Bot(token = token)
        self.offset = 0

    #sends a message
    def mesg(self, chat_id, message):
        self.bot.send_message(chat_id = chat_id, text = message)

    #sends a documents
    def doc(self, chat_id, docu):
        self.docu = docu
        self.bot.send_document(chat_id = chat_id, document = open(self.docu, 'rb'))

    #sends a photo into the group chat
    def photo(self, chat_id, foto):
        self.foto = foto
        self.bot.send_photo(chat_id = chat_id, photo = open(self.foto, 'rb'))

    #generates an invitation link, it has no expiration time
    def invitation(self, chat_id):
        url = self.bot.create_chat_invite_link(chat_id = chat_id)
        return url["invite_link"]
        
    @property
    def update(self):
        try:
            messages = self.bot.get_updates(offset = self.offset)
        
        except:
            messages = []
        
        if messages:
            self.offset = messages[-1]['update_id'] + 1
        return messages
        