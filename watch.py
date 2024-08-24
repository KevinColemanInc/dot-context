import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            if event.src_path.endswith(".instruct"):
                print(f"File {event.src_path} has been modified.")
                subprocess.run(["python", "-m", "main", event.src_path])
            else:
                print(f"Ignored file {event.src_path}; not an .instruct file.")


if __name__ == "__main__":
    watcher = Watcher(".")
    watcher.run()
