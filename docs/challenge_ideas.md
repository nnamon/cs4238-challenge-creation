# Challenge Ideas

## General Notes

* Avoid turning off ASLR.
* Disallow the user from reading sensitive information.

```
mount -o remount,hidepid=2 /proc  # No process information
sysctl -w kernel.dmesg_restrict=1  # No dmesg information
chmod 1733 /tmp /var/tmp /dev/shm  # Prevent leaking user solutions
```

## Exploitation


* Simple buffer overflow of struct to overwrite function pointers.
* Format string bug to leak flag in memory.
* Integer overflow/underflow.
* strcmp return code.
* Shellcode copied to skipping indexes (jmp relative short).

## Cryptography

* Length extension attacks.
* CBC manipulation.
* Predictable seed to random number generator.

## Forensics

* PCAP Analysis - Evidence of a backdoor and its password in one of the running
  services.

## Network

* Scanning of the VM to identify entry points.
* Spoofed UDP packets trigger some behaviour

## Linux

* Not specifying the full path when evoking a program.

## Web

* MD5 hash and unsafe interpretation as number in PHP

