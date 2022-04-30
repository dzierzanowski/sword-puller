#!python
from time import sleep
from threading import Thread, Lock
from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Button, Controller

# Params - if you experience premature ejection of sword,
# try slightly reducing `movement_delta_max` or `movement_accel`.
toggle_key = 'p'
interval_sec = 0.001
movement_delta_max = 1500
movement_accel = 2

class SafeDict():
    def __init__(self):
        self._lock = Lock()
        self._data = {
            'mouse': Controller(),
            'is_pull': False,
            'movement_delta': 0,
            'exit': False
        }
    def get(self, key):
        self._lock.acquire()
        val = self._data[key]
        self._lock.release()
        return val
    def set(self, key, val):
        self._lock.acquire()
        self._data[key] = val
        self._lock.release()
        return val

def puller(data):
    while True:
        if data.get('exit'):
            break
        if data.get('is_pull'):
            mouse = data.get('mouse')
            movement_delta = data.get('movement_delta')
            mouse.move(0, -movement_delta)
            data.set('movement_delta', min(movement_delta + movement_accel, movement_delta_max))
        sleep(interval_sec)

class PyputHandler():
    def __init__(self, data):
        self.data = data
    def handler(self, key):
        if key == KeyCode.from_char(toggle_key):
            data = self.data
            mouse = data.get('mouse')
            if data.get('is_pull'):
                data.set('is_pull', False)
                mouse.release(Button.left)
            else:
                data.set('movement_delta', 0)
                mouse.position = (0, 0)
                data.set('is_pull', True)
                mouse.press(Button.left)

if __name__ == '__main__':
    print('See readme for instructions.')
    print('Press Ctrl+C to exit.')
    data = SafeDict()
    puller_thread = Thread(target=puller, args=(data,))
    puller_thread.start()
    ph = PyputHandler(data)
    with Listener(on_press=ph.handler) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            data.set('exit', True)
