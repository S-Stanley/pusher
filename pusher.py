from modules import Commit
import sys

if len(sys.argv) == 1:
	message = "PUSH made by pusher https://github.com/S-Stanley/pusher.git"
if len(sys.argv) == 2:
	message = sys.argv[1]
if len(sys.argv) > 2:
	print('Erreur, vous avez indiquer trop d\'argument, essayez avec des apostrophes "')
	sys.exit()

push = Commit(message)
push.check_repo()
push.get_remote()
push.get_branch()
push.send()

print('Done!')