from bot.base import database
from bot.utils import BOT_ID


async def add_hun_text_msg(value: str) -> None:
    """
    Adds or updates the hun text message in the database.

    Args:
        value (str): The hun text message to set.
    """
    await database.add_value(int(BOT_ID), "HUN_TEXT", value)


async def del_hun_text_msg() -> None:
    """
    Clears the hun text message from the database.
    """
    await database.clear_value(int(BOT_ID), "HUN_TEXT")


async def get_hun_text_msg() -> str:
    """
    Retrieves the current hun text message from the database.

    Returns:
        str: The hun text message. Defaults to an empty string if not set.
    """
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("HUN_TEXT", [""])[0] if doc else ""


async def update_hun_text_msg(value: str) -> None:
    """
    Updates the force text message in the database.

    This function first deletes the existing force text message and then
    adds the new message.

    Args:
        value (str): The new force text message to set.
    """
    await del_hun_text_msg()
    await add_hun_text_msg(value)


async def add_img_text_msg(value: str) -> None:
    """
    Adds or updates the IMG text message in the database.

    Args:
        value (str): The IMG text message to set.
    """
    await database.add_value(int(BOT_ID), "IMG_TEXT", value)


async def del_img_text_msg() -> None:
    """
    Clears the img text message from the database.
    """
    await database.clear_value(int(BOT_ID), "IMG_TEXT")


async def get_img_text_msg() -> str:
    """
    Retrieves the current img text message from the database.

    Returns:
        str: The img text message. Defaults to an empty string if not set.
    """
    doc = await database.get_doc(int(BOT_ID))
    return doc.get("IMG_TEXT", [""])[0] if doc else ""


async def update_img_text_msg(value: str) -> None:
    """
    Updates the img text message in the database.

    This function first deletes the existing img text message and then
    adds the new message.

    Args:
        value (str): The new img text message to set.
    """
    await del_img_text_msg()
    await add_img_text_msg(value)
