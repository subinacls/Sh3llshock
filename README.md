# Sh3llshock is a tool to extract shellcode from the binary file
 ____  _     _____ _ _     _                _     
/ ___|| |_  |___ /| | |___| |__   ___   ___| | __  
\___ \| '_ \  |_ \| | / __| '_ \ / _ \ / __| |/ / 
 ___) | | | |___) | | \__ \ | | | (_) | (__|   <  
|____/|_| |_|____/|_|_|___/_| |_|\___/ \___|_|\_\  

           <<<<<<Coded by T3jv1l>>>>>>>>       
      <<<<<<Contact for bug t3jv1l@gmail.com>>>>>> 
  
            Usage:  [argument] [file] [argument]:
      -f    --file     The ASM code filename
      -s    --show     Show shellcode
      -i    --intel    Syntax


## Install
```
chmod +x Sh3llshock.py
./Sh3llshock or python Sh3llshock.py

##Example Usage:
/Sh3llshock.py -f '/home/T3jv1l/Desktop/Python_scoala/hello.o' -s
[+] Shellcode =
\xba\x0e\x00\x00\x00\xb9\x00\x00
\x00\x00\xbb\x01\x00\x00\x00\xb8
\x04\x00\x00\x00\xcd\x80\xb8\x01
\x00\x00\x00\xcd\x8

[+] We have a shellcode

```
