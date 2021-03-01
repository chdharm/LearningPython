from functools import partial
from dataclasses import dataclass, field
import sys
from typing import List, Callable


@dataclass
class Observable:
    observers: List[Callable] = field(default_factory=list)

    def register(self, observer: Callable):
        self.observers.append(observer)

    def deregister(self, observer: Callable):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer(*args, **kwargs)


def usage_demo():
    observable = Observable()

    # Register two anonymous observers using lambda.
    observable.register(
        lambda *args, **kwargs: print(f'Observer 1 called with args={args}, kwargs={kwargs}'))
    observable.register(
        lambda *args, **kwargs: print(f'Observer 2 called with args={args}, kwargs={kwargs}'))

    # Create an observer function, register it, then deregister it.
    def callable_3():
        print('Observer 3 NOT called.')

    observable.register(callable_3)
    observable.deregister(callable_3)

    # Create a general purpose observer function and register four observers.
    def callable_x(*args, **kwargs):
        print(f'{args[0]} observer called with args={args}, kwargs={kwargs}')

    for gui_field in ['Form field 4', 'Form field 5', 'Form field 6', 'Form field 7']:
        observable.register(partial(callable_x, gui_field))

    observable.notify('test')


if __name__ == '__main__':
    sys.exit(usage_demo())