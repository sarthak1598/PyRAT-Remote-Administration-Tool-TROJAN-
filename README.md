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
2. privelage escalation 
3. executable payload generation  for windows like operating system to bind the payload with the normal system binaries. 
4. Scheduled Screen capturing . 
5. keylogging feature . 
6. fetching  system information .

