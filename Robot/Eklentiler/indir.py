# Bu araç @matesa tarafından | @POLESTAR_CHAT için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "Yanıtlanan mesajı metin olmaması halinde indirir..",
        "kullanim"  : [
            "Yanıtlanan Mesaj"
            ],
        "ornekler"  : [
            ".indir"
            ]
    }
})

from pyrogram import Client, filters
from pyrogram.types import Message
from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from Robot.Edevat._pyrogram.progress import pyro_progress
from Robot import INDIRME_ALANI, YETKILI
from time import time
from asyncio import sleep

@Client.on_message(filters.command(['indir'], ['!','.','/']))
async def indir(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__", reply_to_message_id=yanit_id)
        return

    ilk_mesaj = await message.reply("`Hallediyorum..`",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    cevaplanan_mesaj = message.reply_to_message
    if (not cevaplanan_mesaj) or (cevaplanan_mesaj.text):
        await ilk_mesaj.edit("__jajaja güldük..__")
        await sleep(3)
        await ilk_mesaj.delete()
        return

    try:
        gelen_dosya = await client.download_media(
            message         = cevaplanan_mesaj,
            progress        = pyro_progress,
            file_name       = INDIRME_ALANI,
            progress_args   = ("**__Dosyayı indiriyorum kankamm...__**", ilk_mesaj, time())
        )
    except Exception as hata:
        await hata_log(hata, client, ilk_mesaj)
        return

    dosya = gelen_dosya.split(INDIRME_ALANI)[1]
    
    await ilk_mesaj.edit(f"`{dosya}`\n\n__Olarak Kaydettim Kanka..__")
