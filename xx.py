from stegano import lsb
from stegano import exifHeader


#img = lsb.hide("saydam.png","YouWinner")
#img.save("saydam2.png")

result_lsb_decode = lsb.reveal("saydam2.png")
print(result_lsb_decode)
# Decoded


from PIL import Image
import stepic
import base64
import hashlib
from Crypto.Hash import RIPEMD

message = "SenKazandin"
encoded_base = base64.b64encode(message.encode(encoding="utf-8"))

encoded_sha512_hash_base64 = hashlib.sha512(encoded_base).hexdigest().encode(encoding="utf-8")
ripemd_hash = RIPEMD.new(encoded_sha512_hash_base64).hexdigest().encode("utf-8")


image = Image.open("saydam2.png")

encoded_stepic_image = stepic.encode(image,ripemd_hash)
encoded_stepic_image.save("saydam3.png","PNG")
print("[+] Success ....")
