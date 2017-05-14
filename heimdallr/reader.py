# -*- coding: utf-8 -*-

import os.path
currpath = os.getcwd()
path = os.path.join(os.path.dirname(os.getcwd()), "resources")


if __name__ == '__main__':
    x = input("Choose a block: ")
    filename = path + '/' + str(x) + '.blk'
    target = open(filename, 'r')

    print("Ballot: ", target.readline())
    print("VoterID: ", target.readline())
    print("Hash: ", target.readline())
    print("Previous Hash: ", target.readline())
    print("Height: ", target.readline())
    print("Nonce: ", target.readline())

    target.close()
    print("End of File")
