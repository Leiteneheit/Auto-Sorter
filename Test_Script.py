import os
import shutil
import eyed3
import re


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
    lines = list()
    with open(file, "r") as target:
        print(f"Last {n} tasks from the file: {file}.\n")
        for line in target.readlines()[-(n+(n-1)):]:
            if line != "\n":
                lines.append(line)
            else:
                continue
    return lines


def regSplit(array):
    pattern = r"(\|.*\|).*(\~.*\~)"
    holder = {}
    for line in array:
        result = re.search(pattern, line)
        if result:
            holder[result[1][1:(len(result[1])-1)]] = result[2][1:(len(result[2])-1)]
        else:
            continue
    return holder


def test():
    pattern = r"(\|.*\|)(?:.*)(\~.*\~)"
    holder = {}
    result = re.search(pattern,
                       "The file |All Quiet on the Western Front (2022) [720p] [WEBRip] [YTS.MX].torrent| will be moved to ~/Users/mac/Downloads/Torrentz~.")
    holder[result[1][1:(len(result[1]) - 1)]] = result[2][1:(len(result[2]) - 1)]
    print(holder)


print(regSplit(readLast("/Users/mac/Downloads/sorting_log.txt", 10)))
