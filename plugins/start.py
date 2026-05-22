import pyrogram
from database import register_bot

WLC_TEMPLATE = "✨Welcome to Kurigram Learning Session: {}"
ADMIN = 6456050659


@pyrogram.client.Client.on_message(
    pyrogram.filters.command("start") & pyrogram.filters.incoming
)
async def start(client: pyrogram.client.Client, message: pyrogram.types.Message):
    message.command[1]
    if register_bot.is_exists({"id": message.from_user.id}):
        return await message.reply("Already started")

    chat = message.chat

    response = await chat.ask(
        text="Hey user, what is your name?",
        filters=(pyrogram.filters.text & pyrogram.filters.incoming),
    )
    name = response.text.capitalize()

    await message.reply(text=f"Hello {name}, what is your age?")
    while True:
        response = await chat.listen(
            filters=(pyrogram.filters.text & pyrogram.filters.incoming), timeout=60
        )

        age_input = response.text.strip()

        if not age_input.isdigit():
            await message.reply(text="Age must be a number!")
            continue

        elif not 0 < int(age_input) < 100:
            await message.reply(text="Please input a valid age!")
            continue

        age = int(age_input)

        break

    await message.reply(
        text="Add your mobile number to continue",
        reply_markup=pyrogram.types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    pyrogram.types.KeyboardButton(
                        text="Add Mobile Number", request_contact=True
                    ),
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        ),
    )

    contact_response = await chat.listen(filters=(pyrogram.filters.contact))
    contact_no = contact_response.contact.phone_number

    user_mention = message.from_user.mention
    user_id = message.from_user.id
    joined_at = str(message.date)
    contact_no = contact_no

    text = WLC_TEMPLATE.format(user_mention)

    await message.reply(text)

    await client.send_message(
        chat_id=ADMIN,
        text=(
            f"""New User:-
Name: {name} ({user_mention}/{user_id})
Age: {age}
Phone Number: {contact_no}
Joined at {joined_at}"""
        ),
    )

    user_info = {
        "name": name,
        "mention": user_mention,
        "id": user_id,
        "age": age,
        "contact_no": contact_no,
        "joined_at": joined_at,
    }

    register_bot.add_user(user_info)
