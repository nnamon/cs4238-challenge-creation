# Wargame
## Improve your cybersecurity skills on Linux
---

## Skip the docs and get playing

From a command terminal, execute the following command.

```sh
$ ssh introduction@10.3.13.37
```
> Password: `wargame`

## List of Challenges

+ introduction - introduces the game.
+ introstrings - using basic linux tools for string extraction.
+ introtempdir - demonstrates the use of the temporary directories.
+ introexfil - introduces how to get files off the system for local analysis
+ intronc - introduces the use of netcat
+ intropwntools - demonstrates the use of pwntools for exploit development
+ babyxor - simple single byte xor cryptography challenge
+ babyre - simple crackme involving dictionaries
+ babyrsa - basic RSA challenge
+ babypwn - simple exploitation challenge
+ babyweb - simple local file inclusion PHP web challenge
+ fourbytewrite - GOT overwrite pwnable
+ blackbeauty - overwrite global variables to get shell
+ dragrace - bypass constraints and jump to shellcode
+ angelica - python pickle challenge

## How to provision the game

### ...on local machine

First install ansible on your machine. Refer to the docs:

http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Once installed, to provision the game on your local machine (`localhost`), execute the `ansible-playbook` command.

```sh
ansible-playbook -c local provision-game.yml --become -vv
```

### ...in a Vagrant Development Environment

To bring up a local development environment, do the following:

```shell
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'ubuntu/xenial64'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'ubuntu/xenial64' is up to date...
==> default: Setting the name of the VM: cs4238-challenge-creation_default_1525167254976_91331
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
...
==> default: Running provisioner: ansible...
    default: Running ansible-playbook...
PYTHONUNBUFFERED=1 ANSIBLE_FORCE_COLOR=true ANSIBLE_HOST_KEY_CHECKING=false ANSIBLE_SSH_ARGS='-o UserKnownHostsFile=/dev/null -o IdentitiesOnly=yes -o ControlMaster=auto -o ControlPersist=60s' ansible-playbook --connection=ssh --timeout=30 --limit="default" --inventory-file=/Users/amon/school/cs4238-challenge-creation/.vagrant/provisioners/ansible/inventory -v provision-game.yml
Using /Users/amon/school/cs4238-challenge-creation/ansible.cfg as config file

PLAY [all] *********************************************************************

TASK [install python2] *********************************************************
...
```

To login as a sudoer:
```
$ vagrant ssh
vagrant ssh
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-122-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


Last login: Tue May  1 09:36:22 2018 from 10.0.2.2
vagrant@ubuntu-xenial:~$
```

To access services on the vagrant box from the host system, you may use the IP
address `10.3.13.37`. For instance,

```shell
nc 10.3.13.37 31337
What fell on Issac Newton's head?
```

### ...on a remote SSH box

To run the playbook against an SSH server you have root access to:

```shell
ansible-playbook -i 206.189.43.131, provision-game.yml -u root -vv
```
