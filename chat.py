import socketio
sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
socket_app = socketio.ASGIApp(sio)


@sio.on("connect")
async def connect(sid, env):
    # print("New Client Connected to This id :"+" "+str(sid))
    await sio.emit("send_msg", "Hello from Server")


@sio.on("disconnect")
async def disconnect(sid):
    print("Client Disconnected: "+" "+str(sid))


@sio.on('msg')
async def client_side_receive_msg(sid, msg):

    await sio.emit("send_msg", msg)
    print("Msg receive from " + str(sid) + "and msg is : ", str(msg))
