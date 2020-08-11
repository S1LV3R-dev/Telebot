import sys

class Logger:
    def __init__(self, filename, lb = "lg"):
        path = "Log"
        if lb == "bo":
            path = "Bugs-offers"
        self.out_file = open("./"+str(path)+"/"+str(filename)+".txt", 'a')
        self.old_stdout = sys.stdout
        sys.stdout = self
    def write(self, text): 
        self.old_stdout.write(text)
        self.out_file.write(text)
    def __enter__(self): 
        return self
    def __exit__(self, type, value, traceback): 
        sys.stdout = self.old_stdout
