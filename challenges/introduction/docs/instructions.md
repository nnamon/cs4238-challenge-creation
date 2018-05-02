# INSTRUCTIONS

## Level &LEVELNUMBER&: Introduction - Getting to know the game

> Challenge: Find the password to **&NEXTLEVELTITLE&**

> Commands you may need
`cat`

The goal of each level is to find and reveal the password for the next level.
Each level presents a challenge which you need to solve to get to the next level.
Once you have the password, you can switch user to the next level, using `su
&NEXTLEVELTITLE&`.

If you find you can side-step the challenge, great! You've hacked that
level.[^1]

You may use whatever it takes to get the password for the next level! ;)

### Docs
Each level contains a docs directory in `/home/level-name/docs`.
In there, you'll find:
```sh
docs
├── hints
├── instructions
└── solution

0 directories, 3 files
```

#### Hints

Type `hints`.

#### Solution

Type `solution`.

---

[^1]: We want the game to be fun! If you do find a hack which renders a level boring, please submit a fix, pull request or suggestion to https://github.com/nnamon/cs4238-challenge-creation.

