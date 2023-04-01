### ssh bandit0@bandit.labs.overthewire.org -p 2220 (bandit0)
cat readme\
Output: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL


### ssh bandit1@bandit.labs.overthewire.org -p 2220 (NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL)
bandit1@bandit:~$ cat ./-   \
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi


### ssh bandit2@bandit.labs.overthewire.org -p 2220 (rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi)
bandit2@bandit:~$ ls \
spaces in this filename   \
bandit2@bandit:~$ cat * \
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG


### ssh bandit3@bandit.labs.overthewire.org -p 2220 (aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG)
bandit3@bandit:~$ ls \
inhere \
bandit3@bandit:~$ cd inhere/  \
bandit3@bandit:~/inhere$ ls -la \
total 12 \
drwxr-xr-x 2 root    root    4096 Sep  1 06:30 .  \
drwxr-xr-x 3 root    root    4096 Sep  1 06:30 ..  \
-rw-r----- 1 bandit4 bandit3   33 Sep  1 06:30 .hidden \
bandit3@bandit:~/inhere$ cat .hidden  \
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe


### ssh bandit4@bandit.labs.overthewire.org -p 2220 (2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe)
bandit4@bandit:~/inhere$ ls \
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09 \
bandit4@bandit:~/inhere$ cat -- -file07 \
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR


### ssh bandit5@bandit.labs.overthewire.org -p 2220 (lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR)
bandit5@bandit:~/inhere$ ls -la * | grep 1033 \
-rw-r-----  1 root bandit5 1033 Sep  1 06:30 .file2 \
Directori 07 - amb awk \
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU 


### ssh bandit6@bandit.labs.overthewire.org -p 2220 (P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU)
bandit6@bandit:/$ ls -lisa * */* | grep bandit7 | grep bandit6 \
76678  12 -rw-------  1 bandit6  bandit6   12288 Sep  7 05:00 bandit7.password.swp \
find / -name bandit7.password.swp \
cat /var/tmp/bandit7.password.swp \
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S


### ssh bandit7@bandit.labs.overthewire.org -p 2220 (z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S)
bandit7@bandit:~$ cat data.txt | grep millionth  \
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP 


### ssh bandit8@bandit.labs.overthewire.org -p 2220 (TESKZC0XvTetK0S9xNwm25STk5iWrBvP)
bandit8@bandit:~$ cat data.txt | sort | uniq -u \
EN632PlfYiZbn3PhVK3XOGSlNInNE00t


### ssh bandit9@bandit.labs.overthewire.org -p 2220 (EN632PlfYiZbn3PhVK3XOGSlNInNE00t)
bandit9@bandit:~$ strings data.txt | grep = \
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s


### ssh bandit10@bandit.labs.overthewire.org -p 2220 (G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s)
bandit10@bandit:~$ base64 -d data.txt \
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM


### ssh bandit11@bandit.labs.overthewire.org -p 2220 (6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM)
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'  \
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


### ssh bandit12@bandit.labs.overthewire.org -p 2220 (JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv)









