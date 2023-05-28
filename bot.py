import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(level=logging.INFO, encoding="utf-8", format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m")

app = Client(
    "Session_bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins={'root':'StringSessionBot'},
)


if __name__ == "__main__":
    logging.info("Starting the bot")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("الايبي ايدي أو الايبي هاش خطا.")
    except AccessTokenInvalid:
        raise Exception("توكن بوت خطا.")
    uname = app.me.username
    logging.info(f"@{uname} الان شغال!")
    idle()
    app.stop()
    logging.info("توقف بوت")
