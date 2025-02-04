from typing import Dict

from bot.base import database
from bot.utils import BOT_ID, logger


async def initial_database() -> None:
    """
    Initializes the database with default values if they are not already present.

    This function sets up initial configuration values in the database.
    It checks if certain keys exist in the database; if not, it adds them with default values.

    Default values added:
        - "GENERATE_URL": False
        - "PROTECT_CONTENT": False
        - "HUN_TEXT": A default picture start message
        - "IMG_TEXT": A default picture force message
        - "FORCE_TEXT": A default force text message
        - "START_TEXT": A default start text message
        - "REPLY_TEXT": A default reply text message
    """
    default_start_text = (
        "ᴡʜᴏᴏᴘꜱ!! {mention}!\n\n"
        "ꜱᴀʏᴀ ᴀᴅᴀʟᴀʜ ʙᴏᴛ ꜱᴛᴏʀᴀɢᴇ ʙᴇʀᴋᴀꜱ ʏᴀɴɢ ᴅɪᴅᴇꜱᴀɪɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ ʙᴇʀᴋᴀꜱ ᴘʀɪʙᴀᴅɪ ᴅɪ ᴄʜᴀɴɴᴇʟ ᴛᴇʀᴛᴇɴᴛᴜ, "
        "ᴅᴀɴ ᴍᴇɴʏᴇᴅɪᴀᴋᴀɴ ᴀᴋꜱᴇꜱ ʟᴇᴡᴀᴛ ᴛᴀᴜᴛᴀɴ ᴜɴɪᴋ ᴋᴇᴘᴀᴅᴀ ᴏʀᴀɴɢ ʟᴀɪɴ."
    )
    default_force_text = (
#        "ᴍᴀᴀꜰ {mention}!\n\n"
        "ᴋᴀᴍᴜ ʙᴀᴋᴋᴀᴀᴀᴀᴀ,{mention}!\n\n"
        "ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴘᴇꜱᴀɴ ᴅᴀʀɪ ʙᴏᴛ, ᴘᴀꜱᴛɪᴋᴀɴ ᴋᴀᴍᴜ ꜱᴜᴅᴀʜ ʙᴇʀɢᴀʙᴜɴɢ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ,"
        "ʟᴀʟᴜ ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴛʀʏ ᴀɢᴀɪɴ"
    )
    default_hun_text = (
        "https://im.gurl.eu.org/file/AgACAgEAAxkDAAILJmdifgogsVRpzXK9nNDasjDCEnVvAAJDrzEbi0UZRxoUVEc4xYqkAQADAgADdwADNgQ.webp"
    )
    default_img_text = (
        "https://im.gurl.eu.org/file/AgACAgEAAxkDAAILJGdifUxLckuY6mwbc9vK6j0-7seKAAJBrzEbi0UZR8HeBV2kD6gIAQADAgADdwADNgQ.webp"
    )
    default_reply_text = (
        "ᴇʜ, {mention} ɪᴅɪᴏᴛ﹗\n\n"
        "ᴋᴀᴍᴜ ʙᴜᴋᴀɴ sᴇɴᴘᴀɪᴋᴜ﹗ 😠\n"
        "ᴊᴀɴɢᴀɴ ɢᴀɴɢɢᴜ ᴀᴋᴜ ᴅᴇɴɢᴀɴ ᴘᴇsᴀɴ ᴀᴛᴀᴜ ʙᴀʟᴀsᴀɴ ʟᴀɢɪ﹗ 🚷"
    )
    default_key_value_db: Dict[str, bool] = {
        "GENERATE_URL": False,
        "PROTECT_CONTENT": False,
        "HUN_TEXT": default_hun_text,
        "IMG_TEXT": default_img_text,
        "FORCE_TEXT": default_force_text,
        "START_TEXT": default_start_text,
        "REPLY_TEXT": default_reply_text,
    }

    bot_id = int(BOT_ID)
    doc = await database.get_doc(
        bot_id
    )  # Fetch the document once to avoid multiple database calls

    for key, value in default_key_value_db.items():
        data = key.replace("_", " ").title()

        if doc is None or key not in doc:
            await database.add_value(bot_id, key, value)
            logger.info(f"{data}: Default")
        else:
            logger.info(f"{data}: Existed")
