def append_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)