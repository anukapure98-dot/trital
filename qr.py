import qrcode

img = qrcode.make('https://trital.onrender.com/')

img.save('qr.png')