from WebSocketServer import WebSocketConnection, WebSocketServer

wsList = []

def connectionHandler(ws: WebSocketConnection):
    ws.onMessage(onMessage)
    wsList.append(ws)

def onMessage(text):
    print(text)
    for ws in wsList:
        ws.send("skrrait daytuh")
    


wss = WebSocketServer(3051, connectionHandler)
print('did we get here?')