from ws4py.client.threadedclient import WebSocketClient


class DummyClient(WebSocketClient):
    def opened(self):
        def data_provider():
            yield 'hello...'

        self.send(data_provider())

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print(m)
        self.close(reason='Bye bye')


if __name__ == '__main__':
    try:
        ws = DummyClient('ws://0.0.0.0:9007/', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
