# -*- coding: utf-8 -*-

import block
import hashlib
import socket
import ssl
import pickle
import os
import argparse
currpath = os.getcwd()
#path = os.path.dirname(os.getcwd()) + "/resources"
path = os.path.join(os.path.dirname(os.getcwd()), "resources")
#needs chain analysis
a_dict = {'address':'','port':0}

# Finds the latest block in the chain by analysing the height of blocks
def getPreviousBlock():
    h = 0
    # Cycles through files in current directory that match filetype
    # Needs error checking
    for fname in os.listdir(path=path):
        if fname.endswith(".blk"):
            #fo = open(path + "/" + fname)
            fo = open(os.path.join(path, fname))
            # Skip the first 4 lines, as Height is on the fifth
            for skipline in range(0, 4):
                fo.readline()
            line = fo.readline()
            fo.close()
        if int(line) > h:
            h = int(line)
    return str(h)


def makeBlock(ballot, voterID):
    print("getPreviousBlock(): ")
    prevx = block.Block()
    prevx.load(getPreviousBlock())

    x = block.Block()
    x.generate(ballot, voterID)
    #    Height
    #    Hash
    #    Hash of Previous
    #    VoterID
    #    Ballot
    x.hash = "Error"
    x.previousHash = prevx.hash
    x.height = prevx.height + 1
    print (x.ballot)
    return x


def hashBlockData(block):
    hdata = str(block.ballot) + str(block.voterID) + str(block.height)
    computedHash = hashlib.md5(hdata.encode('utf-8')).hexdigest()
    print("Block hash written as: ")
    print(computedHash)
    return computedHash


def addBlockToChain(block):
    #Open previous block file to locate hash
    #block.previousHash = ""
    #Save file to blockchain directory
    filename = path + '/' + str(block.height).strip() + '.blk'
    target = open(filename, 'w')

    target.write(str(block.ballot))
    target.write('\n')
    target.write(str(block.voterID))
    target.write('\n')
    target.write(str(block.hash))
    target.write('\n')
    target.write(str(block.previousHash))
    # target.write('\n')
    target.write(str(block.height))
    target.write('\n')
    target.write(str(block.nonceValue))
    print(block)
    block.write()

    target.close()

    print ("Block file written")


def clearBlocks():
    #only used when updating chain
    t_height = getPreviousBlock()
    print(t_height)
    print(path)
    for fname in os.listdir(path=path):
        if fname.endswith(".blk"):
            if fname != "0.blk":
                fpath = path + '/' + fname
                os.remove(fpath)


def transmit(b, b_dict):
#create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    sslContext.set_ciphers("ADH-AES256-SHA")
    sslContext.load_dh_params("dhparam.pem")
    s = sslContext.wrap_socket(sock)
    # s = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")

    #get local machine name
    #host = socket.gethostname()  # for local testing
    # host = '192.168.0.17'       #works
    # port = 9999

    host = b_dict['address']
    port = b_dict['port']

    #connection to hostname on port
    s.connect((host, port))
    # s.send(b.ballot.encode('ascii'))
    # s.send(b.voterID.encode('ascii'))
    # s.send(b.hash.encode('ascii'))
    # s.send(b.previousHash.encode('ascii'))
    # s.send(str(b.height).encode('ascii'))

    msg_pickle = {
    'ballot':b.ballot.encode('ascii'),
    'voterID':b.voterID.encode('ascii'),
    'hash':b.hash.encode('ascii'),
    'pHash':b.previousHash.encode('ascii'),
    'height':str(b.height).encode('ascii')
    }

    s.send(pickle.dumps(msg_pickle))
    s.close()
    print("Message sent")


def verifyBlock(vblock):
    #Read block height
    prevx = block.Block()
    prevx.load(getPreviousBlock())
    currentHeight = int(prevx.height)
    vheight = int(vblock.height)

    #If same as current, check hash
        #If same as current, chain is up to date, throw out block
        #Update voter info
    #0 == verified
    #1 == needs update
    #2 == source needs update (unused)
    #3 == chain reached completion
    #4 == file error; kill application
    if currentHeight == vheight:
        if str(prevx.hash).strip() == str(vblock.hash).strip(): # restore for testing
        #if str(prevx.hash) == str(vblock.hash):
            print ('Up to date')
            return 3
        else:
            print ('Inconsistent hash data')
            print ('Hash expected: %s' % prevx.hash)
            print ('Hash received: %s' % vblock.hash)
            return 1

    #If height is lower, reject block, return current chain
    elif currentHeight > vheight:
        print ('Height too low; source requires update')
        return 2

    #If height is higher, check block.previous == chain.hash
        #If equal, accept block and add to chain
        #If not, throw out block
    elif currentHeight < vheight:
        if str(prevx.hash).strip() == str(vblock.previousHash).strip():
            print ('Data verified')
            return 0
        else:
            print ('Requesting update from host')
            print(prevx.hash)
            return 1

    else:
        print ('Could not verify data')
        return 4


def updateVoter(voter):
    #When blockchain has been verified, update voter
    #Change voterID to prevent revoting
    #Must call voter to regenerate ID
    pass


def receiveVote(self, vote):
    #Listening on application port
    #Takes voterID + ballot [list]
    #After vote, call updateVoter

    #performed through listn.py
    pass


def verifyVoter(self, voter):
    #Disregard below. Use vID in symmetric encryption?
    #Function should allow sign in

    #voter includes voterID, generated from email + timestamp
    #this is used to generate public/private key pair

    #Public key in email provides voter link to sign in
    #Decrypted with stored private key to reveal voterID, allow access if same

    #Function needs to take key, vID, email
    #    Decrypt key using
    pass


def startService(self):
    #Begin listening on given port
    #performed through listen.py
    pass


def endService(self):
    #Close service
    self.exit


def main(block, r_ad, r_po):
    #executes main command chain of program
    a_dict['address'] = r_ad
    a_dict['port'] = r_po

    block.hash = hashBlockData(block)
    addBlockToChain(block)
    transmit(block, a_dict)



if __name__ == '__main__':
    # execute only if run as a script
    #parse arguments from command line
    parser = argparse.ArgumentParser(description='Voting with Blockchains')
    parser.add_argument('-a', '--address', help='Target IP address of next machine', required = True)
    parser.add_argument('-p', '--port', help='Target port on next machine', type=int, required=True, default=9999)
    args = parser.parse_args()

    print("Running from CLI in ", os.getcwd())
    x = makeBlock(input("Enter your vote: "), input("Enter voter ID: "))
    main(x, args.address, args.port)
    print(path)
