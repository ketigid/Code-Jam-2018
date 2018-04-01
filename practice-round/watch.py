import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import sys

global_filename = ''
global_stdin = ''

class MyHandler(PatternMatchingEventHandler):
  patterns = ["*.py"]

  def on_modified(self, event):
    # os.system("python3 testing_tool.py python3 "+global_filename) # problem a
    msg = "python3 "+global_filename
    if global_stdin:
      msg += " < "+global_stdin
    os.system(msg)

if __name__ == "__main__":
  args = sys.argv[1:]
  if args[0]:
    global_filename = args[0]
  if args[1]:
    global_stdin = args[1]
  observer = Observer()
  observer.schedule(MyHandler(), path='.')
  # observer.schedule(MyHandler(args[0]), path='.')
  observer.start()
  print('Started watching {}'.format(args[0]))

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()

  observer.join()
