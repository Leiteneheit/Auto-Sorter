import os
import shutil
import eyed3


def movement():
    path = "/Users/mac/Downloads/Test_Dir"
    os.chdir(path)
    items = os.listdir(path)

    categories = {"Documents": ["docx", "txt", "pdf"],
                  "Movies": ["mkv", "mp4", "mpeg"],
                  "Torrents": "torrent",
                  "Pictures": ["jpeg", "jpg", "png", "webp", "gif"],
                  "Music": "mp3"}

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

        if os.path.exists(path + "/" + holder):
            shutil.move(path + '/' + item, path + '/' + holder + '/' + item)
        else:
            os.makedirs(path + '/' + holder)
            shutil.move(path + '/' + item, path + '/' + holder + '/' + item)


def renameTest(path="/Users/mac/Downloads/Test_Dir/Music"):
    os.chdir(path)
    items = os.listdir(path)

    pattern = "yt1s.com - "
    for item in items:
        if pattern in item:
            print(f"{item[len(pattern):]}")
        else:
            print(item)


def pullID():
    path = "/Users/mac/Downloads/Test_Dir/Music"
    os.chdir(path)
    items = os.listdir(path)

    audiofile = eyed3.load("yt1s.com - ADAM RAP SONG  Eyes On Me  DizzyEight X DJ Grace Record of Ragnarok AMV.mp3")
    print(audiofile.tag.artist)


def torrentMove():
    path = "/Users/mac/Downloads/Test_Dir"
    os.chdir(path)
    items = os.listdir(path)

    categories2 = {"Torrents": ["torrent"],
                   "Pictures": ["jpeg", "jpg", "png", "webp", "gif"]}

    categories = {"Documents": ["docx", "txt", "pdf"],
                  "Movies": ["mkv", "mp4", "mpeg"],
                  "Torrents": "torrent",
                  "Pictures": ["jpeg", "jpg", "png", "webp", "gif"],
                  "Music": "mp3"}

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

        if os.path.exists(path + "/" + holder):
            shutil.move(path + '/' + item, path + '/' + holder + '/' + item)
        else:
            os.makedirs(path + '/' + holder)
            shutil.move(path + '/' + item, path + '/' + holder + '/' + item)


def replaceTest():
    test = "ADAM RAP SONG  Eyes On Me  DizzyEight X DJ Grace Record of Ragnarok AMV.mp3"
    holder = test.replace(" ", "_")
    print(holder)


def readLast(file, n):
    """READ THE LAST N LINES OF A GIVEN FILE"""
    with open(file) as target:
        print(f"Last {n} lines from the file: {file}.")
        for line in file.readlines()[-n:]:
            print(line, end='')


def test():
    path = "/Users/mac/Downloads"
    os.chdir(path)
    items = os.listdir(path)

    categories = {"/Users/mac/Movies/Container": ["mkv", "mp4", "mpeg"],
                  "/Users/mac/Downloads/Torrentz": ["torrent"],
                  "/Users/mac/Downloads/Pictures": ["jpeg", "jpg", "png", "webp", "gif"]}

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
            print(f"The file [{item}] will be moved to [{holder}].\n")
        elif not os.path.exists(holder) and holder != "":
            print(f"The folder [{holder}] has been newly created.\n")
            print(f"The file [{item}] will be moved to [{holder}].\n")


test()
