import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import sys

class MyHandler(PatternMatchingEventHandler):
  patterns = ["*.py"]

  # def __init__(self, file):
  #   self.filename = file
  #   print(self.filename)

  def on_modified(self, event):
    # print('hello')
    # print(self.file[0])
    # os.system("python testing_tool.py python"+self.file[0])
    os.system("python3 testing_tool.py python3 p1.py")

if __name__ == "__main__":
  args = sys.argv[1:]
  observer = Observer()
  observer.schedule(MyHandler(), path=args[0] if args else '.')
  # observer.schedule(MyHandler(args[0]), path='.')
  observer.start()
  print('Started watching {}'.format(args[0]))

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()

  observer.join()
