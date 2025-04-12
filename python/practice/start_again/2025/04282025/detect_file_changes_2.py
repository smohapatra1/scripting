#   https://www.geeksforgeeks.org/how-to-detect-file-changes-using-python/

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            print(f"File {event.src_path} has been modified!")

# Create observer and event handler
observer = Observer()
event_handler = MyHandler()

# Set up observer to watch a specific directory
directory_to_watch = "."
observer.schedule(event_handler, directory_to_watch, recursive=True)

# Start the observer
observer.start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()