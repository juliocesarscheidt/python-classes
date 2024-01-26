import segno

video = segno.make('https://www.youtube.com/@JulioScheidt?sub_confirmation=1')
video.save('channel.png', dark="black", light="white", scale=10)

# from segno import helpers

# qrcode = helpers.make_wifi(ssid='<SSID>', password='<PASSWORD>', security='WPA')
# qrcode.save("Wifi.png", dark="black", light="white", scale=10)
