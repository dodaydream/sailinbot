from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

whitelist = []
full_text = ['透来', '皮夹', '啊囊死给']
def echo(update, context):
    """Echo the user message."""
    if (random.randint(0, 99) < 5):
        if update.message.from_user.id in whitelist:
            return

        if (random.random() < 0.5):
            append = random.choice(['你老母', '恁母', '你🐴', '你个肺'])
            reply = update.message.text[0] + append
        else:
            reply = random.choice(full_text)

        update.message.reply_text(reply)


def enroll(update, context):
    update.message.reply_text('使恁母')
    uid = update.message.from_user.id
    whitelist.remove(uid)


def drop(update, context):
    update.message.reply_text('使，使...' + update.message.from_user.username + '是小天使！')
    uid = update.message.from_user.id
    whitelist.append(uid)


def fire(update, context):
    uid = update.message.reply_to_message.from_user.id
    if uid in whitelist:
        update.message.reply_text('麻痹你骂人家干嘛呀')
    else:
        context.bot.send_message(uid, random.choice(full_text))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(os.getenv('TG_BOT_SAILIN_TOKEN'), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('enroll', enroll))
    dp.add_handler(CommandHandler('drop', drop))
    dp.add_handler(CommandHandler('fire', fire))
    dp.add_handler(MessageHandler(Filters.group, echo))
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
