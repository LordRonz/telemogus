from telegram import Update, Dice
from telegram.ext import CallbackContext, CommandHandler
from secrets import choice


def dice(update: Update, context: CallbackContext):
    if update.effective_chat is None:
        return

    context.bot.send_dice(
        chat_id=update.effective_chat.id, emoji=choice(Dice.ALL_EMOJI)
    )


dice_handler = CommandHandler("dice", dice)
