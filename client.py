from pyromod import Client

import config


bot = Client(
    "my_bot",
    api_id=config.API_ID,
    bot_token=config.BOT_TOKEN,
    api_hash=config.API_HASH

)

