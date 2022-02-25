# A Powerful ᴄʀᴀxʏ Music Bot Property Of marrkmusic Chatting Group
# Without Credit (Mother Fucker)
# Owner @K_A_k_A_03
# co owner @marrk85


from Alexa import BOT_USERNAME, LOG_GROUP_ID, app
from Alexa.Database import blacklisted_chats, is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ɢʀᴏᴜᴘ**...😜\n**ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs...**🥺"
            )
        blacklisted_chats_list = await blacklisted_chats()
        if message.chat.id in blacklisted_chats_list:
            await message.reply_text(
                f"**ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ**\n\n**ʏᴏᴜʀ ᴄʜᴀᴛ ʜᴀs ʙᴇᴇɴ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ʙʏ sᴜᴅᴏ ᴜsᴇʀs ᴀsᴋ ᴀɴʏ SUDO USER ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ**...🤦\n**ᴄʜᴇᴄᴋ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ** 😜 [ғʀᴏᴍ ʜᴇʀᴇ](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
            return await app.leave_chat(message.chat.id)
        if await is_on_off(1):
            if int(message.chat.id) != int(LOG_GROUP_ID):
                return await message.reply_text(
                    f"**ʙᴏᴛ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪɴᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ** 🤭"
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**ɢʙᴀɴɴᴇᴅ ᴜsᴇʀ**\n\n**ʏᴏᴜ'ʀᴇ ɢʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ʙᴏᴛ ᴀsᴋ ᴀɴʏ SUDO USER ᴛᴏ ᴜɴɢʙᴀɴ**...🙈\n**ᴄʜᴇᴄᴋ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ** 😜[ғʀᴏᴍ ʜᴇʀᴇ](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        blacklisted_chats_list = await blacklisted_chats()
        if CallbackQuery.message.chat.id in blacklisted_chats_list:
            return await CallbackQuery.answer(
                "**ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ**", show_alert=True
            )
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOG_GROUP_ID):
                return await CallbackQuery.answer(
                    "**ʙᴏᴛ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪɴᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ...** 🤭",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "**ʏᴏᴜ'ʀᴇ ɢʙᴀɴɴᴇᴅ** 😜", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
