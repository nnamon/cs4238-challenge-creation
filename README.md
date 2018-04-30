# cs4238-challenge-creation

## How to provision the game
First install ansible on your machine. Refer to the docs:

http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Once installed, to provision the game on your local machine (`localhost`), execute the `ansible-playbook` command.

```sh
ansible-playbook -i inventory provision-game.yml --become
```

+ level0 - orientation - introduce the workflow of the game.
