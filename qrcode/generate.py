import segno

video = segno.make('https://www.youtube.com/@JulioScheidt?sub_confirmation=1')
video.save('channel.png', dark="black", light="white", scale=10)
