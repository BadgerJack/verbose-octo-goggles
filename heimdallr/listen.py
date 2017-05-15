# -*- coding: utf-8 -*-

import socket
import ssl
import main
import block
import pickle
import argparse
import os.path

path = os.path.join(os.path.dirname(os.getcwd()), "resources")


# decision making logic for receiving connections
def listen(args):
    #create socket object
    unwrapped = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    sslContext.set_ciphers("ADH-AES256-SHA")
    sslContext.load_dh_params("dhparam.pem")
    serversocket = sslContext.wrap_socket(unwrapped)

    #host = socket.gethostname() for local connection testing
    port = args.port

    #bind to port
    serversocket.bind(('', port))  # replace with host for testing

    #queue up to 5 requests
    serversocket.listen(5)

    while True:
        print("Listening for %s:%d" % (args.address, args.port))
        print("Updates %s" % args.updates)
        #establish connection
        clientsocket, addr = serversocket.accept()

        print("got connection from %s" % str(addr))

        #msg = 'Thank you for connecting' + "\r\n"

        #regular connection to receive block
        if addr[0] == args.address:
            print("Got connection from listening address: %s" % args.address)
            x = block.Block()

            msg_dict = pickle.loads(clientsocket.recv(5000))
            print("Received file from client")

            x.ballot = msg_dict['ballot'].decode('ascii')
            x.voterID = msg_dict['voterID'].decode('ascii')
            x.hash = msg_dict['hash'].decode('ascii')
            x.previousHash = msg_dict['pHash'].decode('ascii')
            x.height = msg_dict['height'].decode('ascii')

            #Verification successful, add to chain
            if main.verifyBlock(x) == 0:
                main.addBlockToChain(x)
                a_dict = {'address': args.updates, 'port': args.port}
                print("Transmitting to: %s" % args.updates)
                main.transmit(x, a_dict)
            #Chain is already up to date
            elif main.verifyBlock(x) == 3:
                print("Update success confirmed")
            #Error codes: Only accounts for error 1, currently
            else:
                #update request, to be sent to previous host (arg.updates)
                #'i cannot use this block, please update my files'
                    print("Not verified, getting update from: %s" % args.address)
                    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    slContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                    slContext.set_ciphers("ADH-AES256-SHA")
                    slContext.load_dh_params("dhparam.pem")
                    u = slContext.wrap_socket(sck)

                    host = args.address
                    port = args.port

                    #connection to hostname on port
                    u.connect((host, port))
                    msg_pickle = {'Update': 'Value'}  # Dud value to act as signal for listening device

                    #send update request back
                    u.send(pickle.dumps(msg_pickle))

                    #response comes with height, files
                    msg_dict = pickle.loads(u.recv(5000))
                    print ("Received updated list")

                    main.clearBlocks()

                    #process received files to update chain
                    for value in msg_dict:
                        y = block.Block()

                        y.ballot = msg_dict[value]['ballot'].decode('ascii').strip()
                        y.voterID = msg_dict[value]['voterID'].decode('ascii').strip()
                        y.hash = msg_dict[value]['hash'].decode('ascii').strip()
                        hashN = msg_dict[value]['pHash'].decode('ascii').strip()
                        y.previousHash = hashN + "\n"  # sidesteps weird issue where files were not writing properly
                        y.height = msg_dict[value]['height'].decode('ascii').strip()

                        main.addBlockToChain(y)

                    print("Repository updated")

                    #continues main process after updating
                    a_dict = {'address': args.updates, 'port': args.port}
                    print("Transmitting to: %s" % args.updates)
                    main.transmit(x, a_dict)

                    u.close()
                    print("Message sent")

        #connection from next host indicates update request
        elif addr[0] == args.updates:
            print("Got connection from listening address: %s" % args.updates)
            #received update request, need to send files to next host
            #'the last block i sent was invalid, so i must update their files'
            print("Updating files for: %s" % args.updates)
            f_dict = {}
            i = 0

            #collect chain files to update target
            for fname in os.listdir(path=path):
                m_dict = {'ballot': '', 'voterID': '', 'hash': '', 'phash': '', 'height': '', 'nonce': '0'}
                if fname.endswith(".blk"):
                    if fname != '0.blk':
                        fo = open(os.path.join(path, fname))

                        m_dict['ballot'] = fo.readline().encode('ascii')
                        m_dict['voterID'] = fo.readline().encode('ascii')
                        m_dict['hash'] = fo.readline().encode('ascii')
                        m_dict['pHash'] = fo.readline().encode('ascii')
                        m_dict['height'] = fo.readline().encode('ascii')

                        f_dict[m_dict['height']] = m_dict
                        fo.close()
                        i = i + 1

            print("Sending %d files" % i)
            clientsocket.send(pickle.dumps(f_dict))
            print("Update file sent")
            clientsocket.close()

        #connections from other sources should never be allowed
        else:
            print("Connection from unrecognised host: %s" % args.address)

        #close connection despite the source
        clientsocket.close()

if __name__ == '__main__':
    #command line arguments
    parser = argparse.ArgumentParser(description='Voting with Blockchains')

    parser.add_argument('-a', '--address',
    help='IP address of machine to listen to', required=True)

    parser.add_argument('-u', '--updates',
    help='IP address of machine to send updates to', required=True)

    parser.add_argument('-p', '--port',
    help='Target port of listening devices',
    type=int, const=1, nargs='?', default=9999)

    args = parser.parse_args()

    listen(args)
