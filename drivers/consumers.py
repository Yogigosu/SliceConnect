import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class AvailableDeliveries(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None

    # client to server
    def connect(self):
        self.room_name = "agent"

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name,
        )
 