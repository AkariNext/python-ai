from typing import Callable


class UseStorage[T]:
    def __init__(self, default: T, *, callback: Callable | None = None):
        self.observers = []
        self._value: T = default
        self.callback = callback

    def subscribe(self, func):
        self.observers.append(func)

    def set(self, value: T):
        if self.callback:
            value = self.callback(value)
        self._value = value

        for observer in self.observers:
            observer(value)

    def get(self):
        return self._value
