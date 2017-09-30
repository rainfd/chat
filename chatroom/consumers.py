import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import rds


# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message, room_name):
    rds.sadd('userlist_%s' % room_name, message.user.username)
    # broadcast to another consumers
    # TO_DO: why this message also send to the reply_channel
    #        I add this reply_channel to Group at the next step?
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "message": message.user.username + " enter the room.",
            "userlist": True,
        })
    })
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat-%s" % room_name).add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_receive(message, room_name):
    text = json.loads(message.content["text"])
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "message": text["message"],
            "user": message.user.username,
        })
    })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message, room_name):
    rds.srem('userlist_%s' % room_name, message.user.username)
    Group("chat-%s" % room_name).discard(message.reply_channel)
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "message": message.user.username + " leave the room.",
            "userlist": True,
        })
    })
