from authorization import bot
from config import MY_CHANNEL_ID
import pyrogram

WLC_TEMPLATE = "{}Welcome to Kurigram Learning Session: {}"


@bot.on_message(pyrogram.filters.command("start"))
async def start(client, message):
    chat = message.chat
    response = await chat.ask("Hey user, what is your name?")
    name = response.text.capitalize()
    response = await chat.ask(f"Hello {name}, what is your age?")
    age = response.text.strip()
    text = WLC_TEMPLATE.format("✨", (message.from_user.mention))
    await message.reply(text)
    await bot.send_message(chat_id=MY_CHANNEL_ID, text=(f"""New User:-
Name: {name}
Age: {age}"""))


bot.run()