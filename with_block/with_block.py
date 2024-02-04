import time
import os

# para uma classe funcionar com o with block, precisa ter os metodos __enter__, __exit__ e close
class FileWriter(object):
    filename: str

    def __init__(self, filename: str):
        self.filename = filename
    
    def get_filename(self) -> str:
        return self.filename

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, type, value, traceback):
        print("__exit__")
        self.close()

    def close(self):
        print("close, sleeping...")
        time.sleep(2)
        self.filename = None

"""
file_writer = FileWriter("./sample_file.txt")
print(file_writer.get_filename())
# ./output.txt
file_writer.close()
"""
# ./sample_file.txt
# close, sleeping...

# vai chamar os metodos __enter__, __exit__ e close
with FileWriter("./sample_file.txt") as file_writer:
    print(file_writer.get_filename())
    # ./output.txt

# __enter__
# ./sample_file.txt
# __exit__
# close, sleeping...
