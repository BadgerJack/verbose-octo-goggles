# -*- coding: utf-8 -*-

import block
import hashlib
import socket
import ssl
import pickle
import os
import time
import argparse
currpath = os.getcwd()
#location of chain repository
path = os.path.join(os.path.dirname(os.getcwd()), "resources")
a_dict = {'address': '', 'port': 9999}


# Finds the latest block in the chain by analysing the height of blocks
def getPreviousBlock():
    h = 0
    # Cycles through files in current repository that match filetype
    for fname in os.listdir(path=path):
        if fname.endswith(".blk"):
            fo = open(os.path.join(path, fname))
            # Skip the first 4 lines, as Height is on the fifth
            for skipline in range(0, 4):
                fo.readline()
            line = fo.readline()
            fo.close()
        if int(line) > h:
            h = int(line)
    return str(h)


#generates a block from a given vote
def makeBlock(ballot, voterID):
    print("Generating block from provided data")
    prevx = block.Block()
    prevx.load(getPreviousBlock())

    x = block.Block()
    x.generate(ballot, voterID)
    #    Height
    #    Hash
    #    Hash of Previous
    #    VoterID
    #    Ballot
    x.hash = "Error"  # if hashing fails, this is the default
    x.previousHash = prevx.hash
    x.height = prevx.height + 1
    return x


# generates hash checksum unique to current block
def hashBlockData(block):
    hdata = str(block.ballot) + str(block.voterID) + str(block.height)
    computedHash = hashlib.md5(hdata.encode('utf-8')).hexdigest()
    print("Block hash written as: %s" % computedHash)
    return computedHash


#writes block data to repository
def addBlockToChain(block):
    filename = path + '/' + str(block.height).strip() + '.blk'
    target = open(filename, 'w')

    target.write(str(block.ballot))
    target.write('\n')
    target.write(str(block.voterID))
    target.write('\n')
    target.write(str(block.hash))
    target.write('\n')
    target.write(str(block.previousHash))
    # target.write('\n')  prevents strange error with line gap in files
    target.write(str(block.height))
    target.write('\n')
    target.write(str(block.nonceValue))
    #block.write()  for debugging purposes only

    target.close()

    print ("Block file written")


#clears repository, used in updating chain
def clearBlocks():
    print("Clearing repository for update...")
    for fname in os.listdir(path=path):
        if fname.endswith(".blk"):
            if fname != "0.blk":
                fpath = path + '/' + fname
                os.remove(fpath)

    print("...done!")


#initial send logic, sends a new block created from site
def transmit(b, b_dict):
    #create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    sslContext.set_ciphers("ADH-AES256-SHA")
    sslContext.load_dh_params("dhparam.pem")
    s = sslContext.wrap_socket(sock)

    #get local machine name
    #host = socket.gethostname()  # for local testing
    host = b_dict['address']
    port = b_dict['port']

    #connection to hostname on port
    s.connect((host, port))

    #prepare data for transfer
    msg_pickle = {
    'ballot': b.ballot.encode('ascii'),
    'voterID': b.voterID.encode('ascii'),
    'hash': b.hash.encode('ascii'),
    'pHash': b.previousHash.encode('ascii'),
    'height': str(b.height).encode('ascii')
    }

    s.send(pickle.dumps(msg_pickle))
    s.close()
    print("Message sent")


#verify received block is legitimate
def verifyBlock(vblock):
    #Read block height
    prevx = block.Block()
    prevx.load(getPreviousBlock())
    currentHeight = int(prevx.height)
    vheight = int(vblock.height)

    #error codes
    #0 == verified
    #1 == needs update
    #2 == source needs update (unused)
    #3 == chain reached completion
    #4 == file error; kill application

    #If same as current, check hash
        #If same as current, chain is up to date, throw out block
        #Update voter info
    if currentHeight == vheight:
        if str(prevx.hash).strip() == str(vblock.hash).strip():
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

    #data is either corrupt or forged
    else:
        print ('Could not verify data')
        return 4


#used for authentication, kept for future expansion
def updateVoter(voter):
    #When blockchain has been verified, update voter
    #Change voterID to prevent revoting
    #Must call voter to regenerate ID
    pass


#used for authentication, kept for future expansion
def verifyVoter(self, voter):
    #voter includes voterID, generated from email + timestamp
    #this is used to generate public/private key pair

    #Public key in email provides voter link to sign in
    #Decrypted with stored private key to reveal voterID, allow access if same
    pass


#main process chain, hashes and saves block files
def main(block, r_ad, r_po):
    a_dict['address'] = r_ad
    a_dict['port'] = r_po
    x_t = time.perf_counter()

    block.hash = hashBlockData(block)
    addBlockToChain(block)
    transmit(block, a_dict)
    y_t = time.perf_counter()
    z_t = y_t - x_t
    print("Block created and transmitted in: %f" % z_t)

# execute only if run as a script
if __name__ == '__main__':
    #command line arguments
    parser = argparse.ArgumentParser(description='Voting with Blockchains')

    parser.add_argument('-a', '--address',
    help='Target IP address of next machine', required=True)

    parser.add_argument('-p', '--port',
    help='Target port on next machine', type=int, required=True, default=9999)

    args = parser.parse_args()

    print("Running from CLI in ", os.getcwd())
    x = makeBlock(input("Enter your vote: "), input("Enter voter ID: "))
    main(x, args.address, args.port)
    print(path)
