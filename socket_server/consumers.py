from channels.generic.http import AsyncHttpConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json
class ChatWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept
        return await super().connect()
    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', None)
        