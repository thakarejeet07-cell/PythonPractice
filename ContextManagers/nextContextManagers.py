#without contextmanager
class FileManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print("File closed automatically")


with FileManager("notes.txt", "w") as f:
    f.write("Hello, this is written using a custom context manager!")



#with contextmanager    
from contextlib import contextmanager
@contextmanager
def open_file(filename,mode):
    file = open(filename,mode)
    try:
        yield file
    finally:
        file.close()
        print("File closed")    


with open_file("notes2.txt", "w") as f:
    f.write("Using contextlib version!")

                         
