# cs4238-challenge-creation

## How to provision the game
First install ansible on your machine. Refer to the docs:

http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Once installed, to provision the game on your local machine (`localhost`), execute the `ansible-playbook` command.

```sh
ansible-playbook -i inventory provision-game.yml --become
```

## Provision on Ubuntu-ansible Docker container (for testing)

From this git working directory

```sh
docker run --rm -v `pwd`:/challenge -it williamyeh/ansible:ubuntu16.04 bash
root@abb8c77b53e4:/# cd challenge/
root@abb8c77b53e4:/challenge# ansible-playbook -i inventory provision-game.yml --become
```

Output should look something like that:

```
PLAY [localhost] ******************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************
ok: [localhost]

TASK [create user] ****************************************************************************************************************************************************************************
changed: [localhost]

TASK [set homedir permissions] ****************************************************************************************************************************************************************
changed: [localhost]

TASK [copy instructions, hints and solution] **************************************************************************************************************************************************
changed: [localhost]

TASK [present instructions when logging into level] *******************************************************************************************************************************************
changed: [localhost] => (item=cd "/home/level00")
changed: [localhost] => (item=clear)
changed: [localhost] => (item=cat "/home/level00/docs/instructions")

TASK [put --help in homedir] ******************************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP ************************************************************************************************************************************************************************************
localhost                  : ok=6    changed=5    unreachable=0    failed=0
```

+ level0 - orientation - introduce the workflow of the game.
