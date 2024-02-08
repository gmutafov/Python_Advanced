import os


def save_extensions(dir):
    for file_name in os.listdir(dir):
        file = os.path.join(dir, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]
            extensions[extension] = extensions.get(extension, []) + [file_name]
        elif os.path.isdir(file):
            save_extensions(file)


directory = input()
extensions = {}

save_extensions(directory)
print(extensions)