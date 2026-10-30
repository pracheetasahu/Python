class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed successfully")

with FileManager("notes.txt", "w") as file:
    file.write("Learning Python Context Managers\n")
    file.write("Managing files safely.")

with FileManager("notes.txt", "r") as file:
    print("File Contents:")
    print(file.read())
