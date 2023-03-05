import time
import os

class FileWriter(object):
  filename: str
  file: object

  def __init__(self, filename: str):
    self.filename = filename
    # if the file already exists do not try to create it
    try:
      print(os.stat(self.filename))
    except Exception as e:
      self.file = open(self.filename, "x") # create file mode
    
  def write(self, content: str):
    self.file = open(self.filename, "w") # write file mode
    self.file.write(content)
  
  def read(self):
    self.file = open(self.filename, "r") # read file mode
    return self.file.read()
  
  def close(self):
    print("close")
    time.sleep(5)
    if self.file is not None:
      self.file.close()
    os.unlink(self.filename)

  def __enter__(self):
    print("__enter__")
    return self

  def __exit__(self, type, value, traceback):
    print("__exit__")
    self.close()

"""
file_writer = FileWriter("./output.txt")
print(file_writer.filename)
# ./output.txt
file_writer.write("Hello World")
print(file_writer.read())
# Hello World
file_writer.close()
# close
"""

# in a given object the "with" block will call the __enter__ and __exit__ methods
with FileWriter("./output.txt") as file_writer:
  print(file_writer.filename)
  # ./output.txt
  file_writer.write("Hello World")
  print(file_writer.read())
  # Hello World
  # print(dir(file_writer)) # show object methods
