# A Powerful ᴄʀᴀxʏ Music Bot Property Of marrkmusic Chatting Group
# Without Credit (Mother Fucker)
# Owner @K_A_k_A_03
# co owner @marrk85


from typing import Dict, List, Union

from Alexa import db

onoffdb = db.onoffper


async def is_on_off(on_off: int) -> bool:
    onoff = await onoffdb.find_one({"on_off": on_off})
    if not onoff:
        return False
    return True


async def add_on(on_off: int):
    is_on = await is_on_off(on_off)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": on_off})


async def add_off(on_off: int):
    is_off = await is_on_off(on_off)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": on_off})
