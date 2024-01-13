
import websocket
import threading
import time
import asyncio
import websockets



def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    # Send any initial messages if required
    ws.send('{"action": "subscribe", "symbols": "EURUSD"}')

# Create a WebSocket connection
websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://ws.eodhistoricaldata.com/ws/forex?api_token=demo",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

# Start a separate thread to run the WebSocket connection
thread = threading.Thread(target=ws.run_forever)
thread.daemon = True
thread.start()

# Keep the main thread alive to continue listening
while True:
    time.sleep(0)
