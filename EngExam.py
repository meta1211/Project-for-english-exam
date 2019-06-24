from telethon import TelegramClient, connection,sync
from config import *
#opencv-python; telethon!




client = TelegramClient( 'anon', api_id, api_hash, 
          connection=connection.ConnectionTcpMTProxyRandomizedIntermediate, 
          proxy=Proxy)
client.start()
client.send_message('me', 'yes, sure')

