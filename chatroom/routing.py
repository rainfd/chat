from channels.routing import route, include
from chatroom.consumers import ws_receive, ws_connect, ws_disconnect


channel_routing = [
    # include(chat_routing, path=r"^/chat/"),
    route("websocket.connect", ws_connect, path=r"^/chat/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.receive", ws_receive, path=r"^/chat/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/chat/(?P<room_name>[a-zA-Z0-9_]+)/$"),
]
