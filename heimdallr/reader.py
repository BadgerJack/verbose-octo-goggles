# -*- coding: utf-8 -*-

import os.path
currpath = os.getcwd()
path = os.path.join(os.path.dirname(os.getcwd()), "resources")

def process(target):
    print("Ballot: ", target.readline())
    print("VoterID: ", target.readline())
    print("Hash: ", target.readline())
    print("Previous Hash: ", target.readline())
    print("Height: ", target.readline())
    print("Nonce: ", target.readline())


if __name__ == '__main__':
    x = input("Choose a block: ")

    if x == "all":
        print("Processing all files...")
        for fname in os.listdir(path=path):
            if fname.endswith(".blk"):
                fname = path + '/' + str(fname)
                target = open(fname, 'r')
                print("Processing %s" % fname)
                process(target)
                target.close()
        print("...done!")

    else:
        filename = path + '/' + str(x) + '.blk'
        target = open(filename, 'r')
        process(target)
        target.close()
        print("End of File")
