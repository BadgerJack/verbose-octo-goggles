# -*- coding: utf-8 -*-
import main
from bottle import *
import random
import argparse
t_dict = {'randnum': 0, 'voter': '', 'ballot': '', 'height': ''}
a_dict = {'address': '', 'port': 0}


#route holds the address being accessed, eg. localhost:8081/filename
#these functions return static files, eg. stylesheets, images
@route('/<filename>')
def send_static(filename):
    return static_file(filename, root='./static/')


@route('/docs/<filename>')
def send_docs(filename):
    return static_file(filename, root='../documentation/')


@route('/docs/_static/<filename>')
def send_doc_static(filename):
    return static_file(filename, root='../documentation/_static/')


@route('/')
def index():
    redirect('/login')


#shortcut for '@route(type=get)'
#function generates voterID while authentication unimplemented
@get('/login')
def login():
    randint = random.randrange(10000, 99999)
    t_dict['randnum'] = randint
    return template('login', **t_dict)


#shortcut for '@route(type=post)'
@post('/login')
def do_login():
    redirect('/vote')


@route('/contact')
def contact():
    return template('contact')


@route('/about')
def about():
    return template('about')


@get('/vote')
def vote():
    return template('form', **t_dict)


#takes vote data from form and processes through main file
@post('/vote')
def do_vote():
    voterID = request.forms.get('voterID')
    choice = request.forms.get('ballot')
    print("Vote data received")

    t_dict['voter'] = voterID
    t_dict['ballot'] = choice
    t_dict['height'] = ''

    x = main.makeBlock(choice, voterID)
    main.main(x, a_dict['address'], a_dict['port'])
    t_dict['height'] = x.height
    return template('return', **t_dict)


if __name__ == '__main__':
    #regular execution parameters
    #command line arguments
    parser = argparse.ArgumentParser(description='Voting with Blockchains')

    parser.add_argument('-a', '--address',
    help='Target IP address of next machine', required=True)

    parser.add_argument('-p', '--port',
    help='Target port on next machine',
    type=int, nargs='?', const=1, default=9999)

    args = parser.parse_args()

    a_dict['address'] = args.address
    a_dict['port'] = args.port

    run(server='paste', port=8081, debug=True)
