import asyncio
import websockets

clientes = set()

class Cliente:
    def __init__(self, name, websocket):
        self.name = name
        self.websocket = websocket

async def chat_server(websocket, path):
    clientes.add(Cliente('David', websocket))
    try:
        async for message in websocket:
            print(clientes)
            for cliente in clientes:
                message_nuevo = f"{cliente.name}: {message}"
                await cliente.websocket.send(message_nuevo)
    finally:
        clientes.remove(websocket)

if __name__ == "__main__":
    start_server = websockets.serve(chat_server, "3.142.80.86", 8300)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()