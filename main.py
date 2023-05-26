from pynput import keyboard, mouse
import sqlite3
import time
import threading
from queue import Queue

last_time = time.time()
event_queue = Queue()


def process_events():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('key_log.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS key_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            key_or_button TEXT,
            time REAL
        )
    ''')

    # Commit the changes
    conn.commit()

    while True:
        event = event_queue.get()
        cursor.execute(
            "INSERT INTO key_log (type, key_or_button, time) VALUES (?, ?, ?)", event)
        conn.commit()


def on_press(key):
    global last_time
    try:
        current_time = time.time()
        time_diff = current_time - last_time
        last_time = current_time
        event_queue.put(('keyboard', '{0}'.format(key), time_diff))
    except AttributeError:
        pass


def on_click(x, y, button, pressed):
    global last_time
    if pressed:
        current_time = time.time()
        time_diff = current_time - last_time
        last_time = current_time
        event_queue.put(('mouse', '{0}'.format(button), time_diff))


event_thread = threading.Thread(target=process_events)
event_thread.start()

with keyboard.Listener(on_press=on_press) as listener1, mouse.Listener(on_click=on_click) as listener2:
    listener1.join()
    listener2.join()
