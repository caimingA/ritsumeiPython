import os
import glob


def get_wiki():
    filenames = list()
    files = glob.glob("../fp2/data/wiki/*.txt")
    files.sort()

    for file in files:
        filename = os.path.basename(file)
        filenames.append(filename)

    return filenames


if __name__ == '__main__':
    f = open('doc_id_name.txt', mode='w', encoding='UTF-8')
    wiki = get_wiki()
    for id in range(len(wiki)):
        line = str(id) + '\t' + wiki[id].replace('.txt', '') + '\n'
        f.write(line)
        print(line)

    f.close()
