#Telethon modules:
from telethon import TelegramClient, connection,sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
#utility modules:
from datetime import datetime
from config import *
#Libaries to load for this project: opencv-python, telethon.

def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time
def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"



client = TelegramClient( 'anon', api_id, api_hash, 
          connection=connection.ConnectionTcpMTProxyRandomizedIntermediate, 
          proxy=Proxy)
client.start()

client.send_message('me', 'Started successfully!')
foler = r'C:\Users\SoulSold\source\repos\Images\Images\time_images\\'

prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        #Because of pathing
        imagePath = prev_update_time.replace(':', '_') + '.jpg' 
        imagePath = foler + imagePath
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(imagePath)
        client(UploadProfilePhotoRequest(file))
