# Pusher
commit and push with one command

### What does it do ?
1. One command to commit and push
2. Check if you are in a git folder
3. Check if you have a remote url
4. Always pull before a push and always commit before a pull

Install:
```shell
cd ~ && git clone https://github.com/S-Stanley/pusher.git .pusher && alias push="python3 ~/.pusher/pusher.py"
```

Run:
```shell
push "MY MESSAGE"
```