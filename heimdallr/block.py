# -*- coding: utf-8 -*-

import os.path
currpath = os.getcwd()
path = os.path.join(os.path.dirname(os.getcwd()), "resources")


class Block:

    def __init__(self):
        self.ballot = ""
        self.voterID = ""
        self.hash = ""
        self.previousHash = ""
        self.height = 0
        self.nonceValue = 0

    def generate(self, ballot, voterID):
        self.ballot = ballot
        self.voterID = voterID
        self.nonceValue = int(voterID)

    def load(self, fname):
        fo = open(path + '/' + fname + ".blk")

        self.ballot = fo.readline()
        self.voterID = fo.readline()
        self.hash = fo.readline()
        self.previousHash = fo.readline()
        self.height = int(fo.readline())
        self.nonceValue = int(fo.readline())

        fo.close()

    # for debugging functions only
    def write(self):
        print(self.ballot)
        print(self.voterID)
        print(self.hash)
        print(self.previousHash)
        print(self.height)
        print(self.nonceValue)
