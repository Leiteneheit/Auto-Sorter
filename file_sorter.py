import os
import shutil
import re


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
                    log.write("FORMATTING: |File Name| ~Destination Folder~     RN##> - Renamed File        MV## - Moved File\n\n")
                    log.write(f"\nMV{round(len(item)/len(holder))}> The file |{item}| will be moved to ~{holder}~.\n")
        elif not os.path.exists(holder) and holder != "":
            if os.path.exists("/Users/mac/Downloads/sorting_log.txt"):
                with open("/Users/mac/Downloads/sorting_log.txt", "a") as log:
                    log.write(f"MV{round(len(item)/len(holder))}-1> The folder ~{holder}~ has been newly created.\n")
                    log.write(f"MV{round(len(item)/len(holder))}-2> The file |{item}| will be moved to ~{holder}~.\n")
            else:
                with open("/Users/mac/Downloads/sorting_log.txt", "w") as log:
                    log.write("FORMATTING: |File Name| ~Destination Folder~ \n\n")
                    log.write(f"MV{round(len(item)/len(holder))}-1> The folder ~{holder}~ has been newly created.\n")
                    log.write(f"MV{round(len(item)/len(holder))}-2> The file |{item}| will be moved to ~{holder}~.\n")



# Functions to aid undoing actions.



def readLast(file, n):
    """READ THE LAST N LINES OF A GIVEN FILE"""
    lines = list()
    with open(file, "r") as target:
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


def addressBuilder(diction):
    addresses = list()
    names = list()
    for key in diction.keys():
        target = f"{diction[key]}/{key}"
        addresses.append(target)
        names.append(key)
    return [addresses, names]


def undoMove(array, target="/Users/mac/Downloads"):
    for address in array[0]:
        nameIndex = array[0].index(address)
        shutil.move(address, f"{target}/{array[1][nameIndex]}")


def undo(no):
    maintain = addressBuilder(regSplit(readLast("/Users/mac/Downloads/sorting_log.txt", no)))
    undoMove(maintain)















def main():
    pass


while __name__ == '__main__':
    main()
