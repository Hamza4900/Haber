from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import bot
import requests
from bs4 import BeautifulSoup

token = "8167758397:AAF87JJ7fquUj30-LQqknweKTDf2XNj6NfY"



def websites(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text("bot kullanılmaya hazır")
    url = requests.get("https://www.webtekno.com/rss.xml")
    if url.status_code == 200:
        soup = BeautifulSoup(url.content, "lxml")
        title = soup.select("channel > item > title")[0]
        url = soup.select("channel > item > guid")[0]
        id_ = soup.select("channel > item > pubDate")[0]
        response = "Webtekno yeni bir haber paylaştı!" + "\n\n" + " " + str(title.text) + "\n\n" + " " + str(url.text)
        temp = None
        veri = title.text

        while True:
            if veri != temp:
                temp = veri
                requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),data={'chat_id': chat_id, 'text':response}).json()
                print(temp)




def idT(update, context):
    print(update.message.chat_id)
if __name__ == '__main__':


    updater = Updater(token=token)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("idN",idT))
    dp.add_handler(CommandHandler("start",websites))

    # <----------------------------------------------------------------------->

    updater.start_polling()
    updater.idle()
