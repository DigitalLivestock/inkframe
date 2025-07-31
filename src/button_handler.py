#!/usr/bin/env python3

import gpiod
import gpiodevice
from gpiod.line import Bias, Direction, Edge
from datetime import timedelta
import threading
import queue
import time

class InkyButtonHandler:
    def __init__(self):

        self.gpio: list[int] = [5, 6, 16, 24] # GPIO pins used by buttons
        self.labels: list[str] = ["A", "B", "C", "D"] # Button names
        self.event_queue = queue.Queue(maxsize=32)
        self.button_lock = threading.Event()

        # Setup configuration for all pins as inputs with a pull-up, falling edge detection and debounce:
        self.input_settings = gpiod.LineSettings(
            direction=Direction.INPUT, 
            bias=Bias.PULL_UP, 
            edge_detection=Edge.FALLING, 
            debounce_period=timedelta(microseconds=50)
        )
        
        # Determine GPIO device:
        self.device = gpiodevice.find_chip_by_platform()
        
        # Connect input settings to GPIO pins:
        self.gpio_offsets = [self.device.line_offset_from_id(id) for id in self.gpio]
        self.gpio_lines = dict.fromkeys(self.gpio_offsets, self.input_settings)

        # Get GPIO event handler:
        self.event_handler = self.device.request_lines(consumer="inky-buttons", config=self.gpio_lines)

        # Create and start a thread for monitoring GPIO
        self.gpio_thread = threading.Thread(target=self._monitor_buttons, args=())
        self.gpio_thread.daemon = True
        self.gpio_thread.start()

    def _monitor_buttons(self) -> None:

        try:
            while True:
                self.event_handler.wait_edge_events()
                for event in self.event_handler.read_edge_events():
                    if not self.button_lock.is_set(): # Do no actions if buttons are disabled
                        self._action(event)
                
                time.sleep(0.05)

        finally:
            self.event_handler.release()

    def _action(self, event) -> None:
        index = self.gpio_offsets.index(event.line_offset)
        gpio_number = self.gpio[index]
        label = self.labels[index]
        self.event_queue.put(label)
        print(f"[DEBUG] Button press detected on GPIO #{gpio_number} label: {label}")

    def get_event(self) -> str:
        return self.event_queue.get()
    
    def is_event(self) -> bool:
        return not self.event_queue.empty()
    
    def clear_event_queue(self):
        while not self.event_queue.empty():
            self.event_queue.get()
    
    def disable_buttons(self):
        self.button_lock.set()

    def enable_buttons(self):
        self.button_lock.clear()

if __name__ == "__main__":

    inky_buttons = InkyButtonHandler()

    while True:
        for event in inky_buttons.get_edge_events():
            inky_buttons.action(event)
