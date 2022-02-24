# A Powerful ᴄʀᴀxʏ Music Bot Property Of marrkmusic Chatting Group
# Without Credit (Mother Fucker)
# Owner @K_A_k_A_03
# co owner @marrk85



from typing import Union, List
from pyrogram import filters

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded


def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands,"")
