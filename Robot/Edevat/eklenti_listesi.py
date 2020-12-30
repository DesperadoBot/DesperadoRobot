# Bu araç @matesa tarafından | @POLESTAR_CHAT için yazılmıştır.

from os import listdir

def eklentilerim() -> str:
    eklenti_listele = ""

    for dosya in listdir("./Robot/Eklentiler/"):
        if not dosya.endswith(".py") or dosya.startswith("_"):
            continue
        eklenti_listele += f"🥷 `{dosya.replace('.py','')}`\n"

    return eklenti_listele
