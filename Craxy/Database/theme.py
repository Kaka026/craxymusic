# A Powerful ᴄʀᴀxʏ Music Bot Property Of marrkmusic Chatting Group
# Without Credit (Mother Fucker)
# Owner @K_A_k_A_03
# co owner @marrk85



from typing import Dict, List, Union

from Alexa import db

themedb = db.notes


async def _get_theme(chat_id: int) -> Dict[str, int]:
    _notes = await themedb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_theme(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_theme(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_theme(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_theme(chat_id)
    _notes[name] = note
    await themedb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )
