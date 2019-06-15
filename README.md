# Py-RAT

Py-Rat is a AES encrypted reverse shell for exploitation of remote system when injected with its victim_side code coded in Python.
Aes is used to encrypt all the data communication between the remote computer and the attacker.

Then on the same port , once the victime side code is executed in the target machine then , attacker can issue the remote commands to the target system and can compromise the machine .

## Method to run

for testing on localmachine:: 
open 1 terminal : 
run attacker_side_code.py 

open another terminal : 
run the victim_side_code.py :

# Further scope of improvement and features to be added 

1. Remote file transfer capability .
2. privelage escalation Check script to be added into the tool so to directly running the script automate the proccess of detecting the  possible vulnerbilities in the system , most specifically in the operating system which can be exploited to gain the shell Privileges . 

3. executable payload generation  for windows like operating system to bind the payload with the normal system binaries. 
4. Scheduled Screen capturing . 
5. Scheduled keylogging feature . 
6. fetching  system information so giving it a complete featchers of the trojan like software . 

# Exploitation with ICMP Tunneling to deliver the malicious payload with hiding in the harmless lookinig icmp protocol bypassing the firewalls 

1. ICMP_Server file.
2. ICMP_Client file 
3. It does'n require the port coVfiguration, As icmp workes on Layer 3/of the TCP/IP model .
4. ICMP is generally not locked on networks and specially on medium to large enterprise networks .
5. Due to trouleshooting purposes . 
6. Works same as of reverse shell ised to write In Py-RAT aove. 
7. server should executed on attacker 's machine  , while client should e on client machine . 
8. Don't missuse the script. ;) . 

