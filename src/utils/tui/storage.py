class UseStorage[T]:
    def __init__(self, default: T):
        self.observers = []
        self._value: T = default

    def subscribe(self, func):
        self.observers.append(func)

    def set(self, value: T):
        self._value = value
        for observer in self.observers:
            observer(value)

    def get(self):
        return self._value
