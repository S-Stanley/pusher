import sys
from modules import Commit

if len(sys.argv) == 1:
	message = "PUSH made by pusher https://github.com/S-Stanley/pusher.git"
if len(sys.argv) == 2:
	message = sys.argv[1]
if len(sys.argv) > 2:
	print('Erreur, vous avez indiquer trop d\'argument, essayez avec des apostrophes "')
	sys.exit()

# if '.git' not in files:
# 	os.popen('git init').read()
# all_branch = os.popen('git branch').read().split('\n')
# for br in all_branch:
# 	if '*' in br:
# 		branch = br.replace('*', '').replace(' ', '')
# 		break
# files = os.popen('ls -a').read().split('\n')
# if 'origin' not in os.popen('git remote').read().split('\n'):
# 	origin = input('Add git origin url: ')
# 	os.popen(f'git remote add origin {origin}').read()
# os.popen(f'git add . && git commit -m "{message}" && git pull origin {branch}').read()
# os.popen(f'git push origin {branch}').read()

push = Commit(message)
push.check_repo()
push.get_remote()
push.get_branch()
push.send()

print('Done!')