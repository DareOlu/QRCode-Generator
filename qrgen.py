import io
import pyqrcode
from base64 import b64encode
import eel
from pyqrcode import QRCode
import png

eel.init('frontend')

@eel.expose
def generateQRCode(s):
    img = pyqrcode.create(s)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR Code Generated.")
    return "data:image/png;base64, " + encoded


eel.start('index.html', size=(900, 600))