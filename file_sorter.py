import os
import shutil


def renamer(curr="/Users/mac/Downloads"):
    targets = os.listdir(curr)
    pattern = "yt1s.com - "
    for item in targets:
        if pattern in item:
            os.rename(f"{curr}/{item}", f"{curr}/{item[len(pattern):]}")


def mover():
    path = "/Users/mac/Downloads"
    os.chdir(path)
    items = os.listdir(path)

    categories = {"/Users/mac/Movies/Container": ["mp4", "mpeg"],
                  "/Users/mac/Downloads/Testing": ["mkv"],
                  "/Users/mac/Downloads/Setups": ["dmg", "zip", "iso"],
                  "/Users/mac/Downloads/Torrentz": ["torrent"],
                  "/Users/mac/Downloads/Pictures": ["jpeg", "jpg", "png", "webp", "gif", "avif"]}

    for item in items:
        # noinspection PyRedeclaration
        name, ext = os.path.splitext(item)
        ext = ext[1:]
        holder = ""

        if ext == '':
            continue

        for x in categories.keys():
            if ext in categories[x]:
                holder = x

        if os.path.exists(holder) and holder != "":
            shutil.move(path + '/' + item, holder + '/' + item)
        elif not os.path.exists(holder) and holder != "":
            os.makedirs(holder)
            shutil.move(path + '/' + item, holder + '/' + item)


def cleaner():
    pass


def moveLogger():
    path = "/Users/mac/Downloads"
    os.chdir(path)
    items = os.listdir(path)

    categories = {"/Users/mac/Movies/Container": ["mp4", "mpeg"],
                  "/Users/mac/Downloads/Testing": ["mkv"],
                  "/Users/mac/Downloads/Setups": ["dmg", "zip", "iso"],
                  "/Users/mac/Downloads/Torrentz": ["torrent"],
                  "/Users/mac/Downloads/Pictures": ["jpeg", "jpg", "png", "webp", "gif", "avif"]}

    for item in items:
        # noinspection PyRedeclaration
        name, ext = os.path.splitext(item)
        ext = ext[1:]
        holder = ""

        if ext == '':
            continue

        for x in categories.keys():
            if ext in categories[x]:
                holder = x

        if os.path.exists(holder) and holder != "":
            if os.path.exists("/Users/mac/Downloads/sorting_log.txt"):
                with open("/Users/mac/Downloads/sorting_log.txt", "a") as log:
                    log.write(f"\nThe file |{item}| will be moved to ~{holder}~.\n")
            else:
                with open("/Users/mac/Downloads/sorting_log.txt", "w") as log:
                    log.write("FORMATTING: |File Name| ~Destination Folder~ \n\n")
                    log.write(f"\nThe file |{item}| will be moved to ~{holder}~.\n")
        elif not os.path.exists(holder) and holder != "":
            if os.path.exists("/Users/mac/Downloads/sorting_log.txt"):
                with open("/Users/mac/Downloads/sorting_log.txt", "a") as log:
                    log.write(f"1. The folder ~{holder}~ has been newly created.\n")
                    log.write(f"2. The file |{item}| will be moved to ~{holder}~.\n")
            else:
                with open("/Users/mac/Downloads/sorting_log.txt", "w") as log:
                    log.write("FORMATTING: |File Name| ~Destination Folder~ \n\n")
                    log.write(f"1. The folder ~{holder}~ has been newly created.\n")
                    log.write(f"2. The file |{item}| will be moved to ~{holder}~.\n")


def main():
    renamer()
    moveLogger()
    mover()


while __name__ == '__main__':
    main()
