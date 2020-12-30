# Bu araç @matesa tarafından | @POLESTAR_CHAT için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama" : "DesperadoSpatula'dan YouTube Video bilgilerini verir..",
        "kullanim" : [
            "link"
            ],
        "ornekler" : [
            ".kekiktube link"
            ]
    }
})

from pyrogram import Client, filters
from pyrogram.types import Message
from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from DesperadoSpatula import DesperadoTube

@Client.on_message(filters.command(['desperadotube'],['!','.','/']))
async def desperadotube(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)
    yanit_id  = await yanitlanan_mesaj(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id      = yanit_id,
        disable_web_page_preview = True
    )
    girilen_yazi = message.command
    #------------------------------------------------------------- Başlangıç >

    if len(girilen_yazi) == 1:
        await ilk_mesaj.edit("__Arama yapabilmek için `link` girmelisiniz..__")
        return

    link   = girilen_yazi[1]

    try:
        desperado = DesperadoTube(link).veri['veri'][0]
    except IndexError:
        await ilk_mesaj.edit(f'`{link}` __bulunamadı..__')
        return

    await ilk_mesaj.delete()

    mesaj = f"""
**Sahip :** __{desperado['sahip']}__
**Başlık :** __{desperado['baslik']}__
**Süre :** __{desperado['sure']}__
**İzlenme :** __{desperado['izlenme']}__
**Açıklama :** __{desperado['aciklama'][:500]}...__


**Kalite :** __{desperado['kalite']}__
**Boyut :** __{desperado['boyut']}__
[Video'yu İndir]({desperado['url']})
"""

    try:
        await message.reply_photo(
            photo   = kekik['resim'],
            caption = mesaj
        )
    except Exception as hata:
        await hata_log(hata, client, ilk_mesaj)
        return
