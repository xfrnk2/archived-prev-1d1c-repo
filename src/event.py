# coding=utf-8


from abc import ABC

from input import InputManager


class Event(ABC):
    pass


class VoidEvent(Event):
    pass


class GameExitEvent(Event):
    pass


class EventManager:
    def __init__(self):
        self.__input = InputManager()

    def close(self):
        self.__input.set_normal_term()

    def get_event(self) -> Event:
        input_manager = self.__input
        if input_manager.is_pressed():
            c = input_manager.get_key()
            if ord(c) == 27:  # ESC
                return GameExitEvent()

        return VoidEvent
