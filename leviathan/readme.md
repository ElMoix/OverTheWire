# OVERTHEWIRE GAMES - LEVIATHAN

## Data for the levels can be found in the homedirectories. You can look at /etc/leviathan_pass for the various level passwords.

### ssh leviathan0@leviathan.labs.overthewire.org -p 2223 (leviathan0)
```
> leviathan0@gibson:~/.backup$ cat bookmarks.html | grep "leviathan"
    <DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PPIfmI1qsA" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```
### ssh leviathan1@leviathan.labs.overthewire.org -p 2223 (PPIfmI1qsA)
```
> leviathan1@gibson:~$ ls -lisa
    526580 16 -r-sr-x---  1 leviathan2 leviathan1 15072 Feb 21 22:02 check

> leviathan1@gibson:~$ file check 
    check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=aab009a1eb3940df51c668d1c35dc9cdc1191805, for GNU/Linux 3.2.0, not stripped

> leviathan1@gibson:~$ ./check 
    password: 
    Wrong password, Good Bye ...


```
### ssh leviathan2@leviathan.labs.overthewire.org -p 2223 ()
```

```
### ssh leviathan3@leviathan.labs.overthewire.org -p 2223 ()
```

```
### ssh leviathan4@leviathan.labs.overthewire.org -p 2223 ()
```

```
### ssh leviathan5@leviathan.labs.overthewire.org -p 2223 ()
```

```
### ssh leviathan6@leviathan.labs.overthewire.org -p 2223 ()
```

```
### ssh leviathan7@leviathan.labs.overthewire.org -p 2223 ()
```

```