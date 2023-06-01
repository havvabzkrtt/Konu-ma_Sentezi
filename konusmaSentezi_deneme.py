from typing import Text
from gtts import gTTS
import os
import qrcode

data=qrcode.make("""Parol
Parol Tabletin aktif maddesi parasetamol, klinik olarak kanıtlanmış, analjezik ve
antipiretik etkili bir ilaçtır. Hipotalamustaki termoregülasyon merkezi üzerindeki etkisi
ile antipiretik etki gösterir. Parasetamol, prostaglandin sentezini önler. Gastrointestinal
sistemden hızla absorbe olur. Parol, analjezik ve antipiretik etkilerini 15-30 dakikada ve 3-4
saat süreyle gösterir. soğuk algınlığı, influenza ve diğer bakteriyel ve viral
enfeksiyonlar da ise hem analjezik hem de antipiretik etki gösterir.
Kontrendikasyonları:Anemili veya kardiyak, pulmoner, renal ya da hepatik hastalıkları olan kişilerde doktor
kontrolü olmadan kullanılmamalıdır.""")

data.save("deneme2.png")

from pyzbar import pyzbar 
from PIL import Image

qr=pyzbar.decode(Image.open("deneme2.png"))
print( qr[0].data.decode('utf-8'))
data = qr[0].data.decode('utf-8')

text = data

language = 'tr'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")

os.system("start text.mp3")
