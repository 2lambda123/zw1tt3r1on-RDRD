# Recursive Docker Registry Downloader

I created this script to be able to recursively download docker registry files and to be able to easily investigate them.

# Requirements

RDRD only works in python 3 and has just 3 dependencies
```
pyfiglet==1.0.2
Requests==2.31.0
wget==3.2
```

To install these dependencies, just run
```
python3 -r requirements.txt
```

# Usage

Using rdrd is very simple, just run
```
python3 rdrd.py
```

and it should show this and just enter the target URL together with its version
```
'########::'########::'########::'########::
 ##.... ##: ##.... ##: ##.... ##: ##.... ##:
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##:
 ########:: ##:::: ##: ########:: ##:::: ##:
 ##.. ##::: ##:::: ##: ##.. ##::: ##:::: ##:
 ##::. ##:: ##:::: ##: ##::. ##:: ##:::: ##:
 ##:::. ##: ########:: ##:::. ##: ########::
..:::::..::........:::..:::::..::........:::

-=-=Recursive Docker Registry Downloader=-=-
-=-=-=-=-=-=-Made by zw1tt3r1on-=-=-=-=-=-=-
============================================
Enter Target URL: http://localhost:3000/v3
```

### Support my projects 
![](https://github.com/zw1tt3r1on/RDRD/assets/64955404/8ebb3761-a320-4343-8f63-7e0d1a3eb964)
https://www.buymeacoffee.com/zw1tt3r1on
