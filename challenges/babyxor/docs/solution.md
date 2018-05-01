# SOLUTION

The encrypted file uses a single byte XOR scheme with 0x42 as the key. To
decrypt it, one can iterate through all the possible keys.

```python
for key in range(256):
    print "".join([chr(ord(i)^key) for i in file("encrypted").read()])
```

The decrypted password can be seen in the middle of the attempts:

```
Vjkq"kq"vjg"fgap{rvgf"rcqqumpf"vm"vjg"lgzv"ngtgn8"Q3le3g]`{v1]i1{]37]`p1ci6`n1
Wkjp#jp#wkf#gf`qzswfg#sbpptlqg#wl#wkf#mf{w#ofufo9#P2md2f\azw0\h0z\26\aq0bh7ao0
This is the decrypted password to the next level: S1ng1e_byt3_k3y_15_br3ak4bl3

Uihr!hr!uid!edbsxqude!q`rrvnse!un!uid!odyu!mdwdm;!R0of0d^cxu2^j2x^04^cs2`j5cm2

Rnou&ou&rnc&bcetvrcb&vguuqitb&ri&rnc&hc~r&jcpcj<&U7ha7cYdr5Ym5Y73Ydt5gm2dj5
```
