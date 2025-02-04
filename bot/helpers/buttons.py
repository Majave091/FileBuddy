from typing import List, Optional, Tuple

from hydrogram import Client
from hydrogram.helpers import ikb
from hydrogram.types import Message

from bot.utils import config

from .handlers import helper_handlers


def admin_buttons() -> ikb:
    database_chat_id = config.DATABASE_CHAT_ID
    database_ch_link = f"tg://openmessage?chat_id={str(database_chat_id)[4:]}"
    """
    Creates an inline keyboard with buttons for admin-related actions.

    Returns:
        ikb: An inline keyboard with buttons for managing chats and additional settings.
    """
    buttons: List[Tuple[str, str, str]] = []
    fs_data = helper_handlers.fs_chats
    if fs_data:
        for chat_id, chat_info in fs_data.items():
            chat_type = chat_info.get("chat_type", "Unknown")
            invite_link = chat_info.get("invite_link", "#")
            if chat_type == "Channel":
                result = "📰 ᴄʜᴀɴɴᴇʟ"
            elif chat_type == "Group":
                 result = "🎭 ɢʀᴏᴜᴘ"
            else:
                result = "Unknown"

            buttons.append((result, invite_link, "url"))

    button_layouts: List[List[Tuple[str, str, str]]] = [
        buttons[i : i + 3] for i in range(0, len(buttons), 3)
    ]
    button_layouts.append([("🤖 ᴘᴇɴɢᴀᴛᴜʀᴀɴ ʙᴏᴛ 🔧", "settings"), 
                           ("🗄️ ᴅᴀᴛᴀʙᴀsᴇ ᴄʜᴀɴɴᴇʟ", database_ch_link, "url")])
    button_layouts.append([("❌ ᴛᴜᴛᴜᴘ", "close")])
     # multi line append
#    button_layouts.append([("❌ 𝑪𝒍𝒐𝒔𝒆", "close")])

    return ikb(button_layouts)


async def join_buttons(client: Client, message: Message, user_id: int) -> Optional[ikb]:
    """
    Creates an inline keyboard with buttons for joining chats the user hasn't joined yet.

    Args:
        client (Client): The hydrogram client instance.
        message (Message): The message that triggered this action.
        user_id (int): The ID of the user for whom the join buttons are being created.

    Returns:
        Optional[ikb]: An inline keyboard with join buttons, or None if the user is already joined.
    """
    no_join_ids = await helper_handlers.user_is_not_join(user_id)
    if not no_join_ids:
        Cancel: List[List[Tuple[str, str]]] = [[("❌ ᴛᴜᴛᴜᴘ", "closes")]]
        return ikb(Cancel)

    buttons: List[Tuple[str, str, str]] = []
    fs_data = helper_handlers.fs_chats
    for chat_id in no_join_ids:
        chat_info = fs_data.get(chat_id, {})
        chat_type = chat_info.get("chat_type", "Unknown")
        invite_link = chat_info.get("invite_link", "#")
        if chat_type == "Channel":
            result = "ᴄʜᴀɴɴᴇʟ (🧳)"
        elif chat_type == "Group":
            result = "ɢʀᴏᴜᴘ (💬)"
        else:
            result = "Unknown"

        buttons.append((f"➕ ᴊᴏɪɴ {result}", invite_link, "url"))

    button_layouts: List[List[Tuple[str, str, str]]] = [
        buttons[i : i + 2] for i in range(0, len(buttons), 2)
    ]

    if len(message.command) > 1:
        start_url = f"https://t.me/{client.me.username}?start={message.command[1]}"
#        button_layouts.append([("❌ 𝑪𝒍𝒐𝒔𝒆", "close")])
        button_layouts.append([("🔄 ᴛʀʏ ᴀɢᴀɪɴ", start_url, "url"), ("❌ ᴛᴜᴛᴜᴘ", "closes")])

    return ikb(button_layouts)


class HelperButtons:
    """
    Defines various inline button layouts for the bot.
    """
    Contact: List[List[Tuple[str, str, str]]] = [
        [("📞 ᴄᴏɴᴛᴀᴄᴛ ᴜs", f"https://t.me/{config.OWNER_USERNAME}/3", "url")]
    ]
    Close: List[List[Tuple[str, str]]] = [[("❌ ᴄʟᴏsᴇ ᴍᴇɴᴜ", "close")]]
    Broadcast: List[List[Tuple[str, str]]] = [[("📢 ʙʀᴏᴀᴅᴄᴀsᴛ ɴᴏᴛɪᴄᴇs", "broadcast")]]
    Ping: List[List[Tuple[str, str]]] = [[("📡 ᴘɪɴɢ ᴛᴇsᴛ", "ping")]]
    Uptime: List[List[Tuple[str, str]]] = [[("⏳ ᴄʜᴇᴄᴋ ᴜᴘᴛɪᴍᴇ", "uptime")]]
    Menu: List[List[Tuple[str, str]]] = [
        [("⚙️ ɢᴇɴᴇʀᴀᴛᴇ sᴛᴀᴛᴜs", "menu generate")],
        [("🚀 sᴛᴀʀᴛ sᴇʀᴠɪᴄᴇ", "menu start"), ("💪 ꜰᴏʀᴄᴇ sᴇʀᴠɪᴄᴇ", "menu force")],
        [("✉️  ʀᴇᴘʟʏ ᴛᴇxᴛ ᴜsᴇʀs", "menu reply")],
        [("🖼️ ᴘɪᴄᴛᴜʀᴇ sᴛᴀʀᴛ", "menu image"), ("🎨 ᴘɪᴄᴛᴜʀᴇ ꜰᴏʀᴄᴇ", "menu hunter")],
        [("🔒 ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ", "menu protect")],
        [("👥 ᴀᴅᴍɪɴ ᴍᴀɴᴀɢᴇʀ", "menu admins"), ("📈 ꜰ-sᴜʙs ᴛʀᴀᴄᴋᴇʀ", "menu fsubs")],
        [("❌ ᴄʟᴏsᴇ ᴍᴇɴᴜ", "home")],
#        [("❌ 𝑪𝒍𝒐𝒔𝒆", "close"), ("Cancel", "home")],
    ]
    Cancel: List[List[Tuple[str, str]]] = [[("🔙 ᴄᴀɴᴄᴇʟ ᴏᴘᴇʀᴀᴛɪᴏɴ", "cancel")]]
    Generate: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("🔄 ᴄʜᴀɴɢᴇ ᴏᴘᴛɪᴏɴs", "change generate")]
    ]
    Generate_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu generate")]]
    Start: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("⚡ sᴇᴛ sᴛᴀʀᴛ sᴇʀᴠɪᴄᴇ", "update start")]
    ]
    Start_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu start")]]
    Force: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("⚡ sᴇᴛ ꜰᴏʀᴄᴇ sᴇʀᴠɪᴄᴇ", "update force")]
    ]
    Force_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu force")]]
    Reply: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("⚡ sᴇᴛ ʀᴇᴘʟʏ ᴜsᴇʀs sᴇʀᴠɪᴄᴇ", "update reply")]
    ]
    Reply_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu reply")]]
    Image: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("🖼️ sᴇᴛ ɪᴍᴀɢᴇ sᴛᴀʀᴛ", "update image")]
    ]
    Image_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu image")]]
    Hunter: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("🖼️ sᴇᴛ ɪᴍᴀɢᴇ ꜰᴏʀᴄᴇ", "update hunter")]
    ]
    Hunter_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu hunter")]]
    Protect: List[List[Tuple[str, str]]] = [
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings"), ("🔒 ᴄʜᴀɴɢᴇ ᴘʀᴏᴛᴇᴄᴛ", "change protect")]
    ]
    Protect_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu protect")]]
    Admins: List[List[Tuple[str, str]]] = [
        [("➕ ᴀᴅᴅ ᴀᴅᴍɪɴ", "add admin"), ("➖ ᴅᴇʟᴇᴛᴇ ᴀᴅᴍɪɴ", "del admin")],
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings")],
    ]
    Admins_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu admins")]]
    Fsubs: List[List[Tuple[str, str]]] = [
        [("➕ ᴀᴅᴅ ꜰ-sᴜʙs", "add f-sub"), ("➖ ᴅᴇʟᴇᴛᴇ ꜰ-sᴜʙs", "del f-sub")],
        [("🔙 ʙᴀᴄᴋ ᴛᴏ sᴇᴛᴛɪɴɢs", "settings")],
    ]
    Fsubs_: List[List[Tuple[str, str]]] = [[("🔙 ʀᴇᴛᴜʀɴ ᴛᴏ ᴍᴇɴᴜ", "menu fsubs")]]



helper_buttons: HelperButtons = HelperButtons()

