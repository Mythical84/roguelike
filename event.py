class Dispatcher:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def broadcast_event(self):
        for listener in self.listeners:
            listener.print()


class Listener:
    def print(self):
        print("test")


dispatcher = Dispatcher()

listener = Listener()
listener2 = Listener()

dispatcher.add_listener(listener)
dispatcher.add_listener(listener2)

dispatcher.broadcast_event()
