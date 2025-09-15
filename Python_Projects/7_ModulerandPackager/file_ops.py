def create_file(fname):
    with open(fname, "w") as f:
        pass
    print("File created!")

def write_file(fname, data):
    with open(fname, "w") as f:
        f.write(data)
    print("Data written!")

def read_file(fname):
    try:
        with open(fname, "r") as f:
            print("File Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found!")

def append_file(fname, data):
    with open(fname, "a") as f:
        f.write(data)
    print("Data appended!")
