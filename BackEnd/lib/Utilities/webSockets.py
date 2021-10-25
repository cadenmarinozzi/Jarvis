from websocket_server import WebsocketServer
import _thread, math

def websocketServer(host, port):
    websocket = WebsocketServer(port, host = host);

    def thread(threadName, delay):
        websocket.run_forever();

    _thread.start_new_thread(thread, ("Thread-3", math.inf, ));

    return websocket; 