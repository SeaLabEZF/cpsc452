Language:
Python 3

Collaborator (Last, First):
Hillenbrand, Sean
Moynihan, Chase
Tran, Kenny
Wulwick, Sean

Email:
seanhillenbrand@csu.fullerton.edu
chasemoy@csu.fullerton.edu
hikennytran@csu.fullerton.edu
sean.wulwick@csu.fullerton.edu

How to Run:
run this in terminal.
python main.py <CIPHER> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>

Additonal Information:
The way we implemented playfair originally caused issues with the '\n'
based on our rework of it it would delete the last element of the string
if no '\n' was present, to fix this we did a check and this can append
blanks to the cipher text that are seen upon printing, however when
decrypted the blanks will not be seen but will still exist at the end
of the string.

We assumed only lowercase input for the key and files.