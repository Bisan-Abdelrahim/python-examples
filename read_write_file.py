def read_write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

    with open(filename, "r") as file:
        return file.read()



