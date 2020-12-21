import os
import sys
from time import sleep

if len(sys.argv) == 1:
	print('Erreur! Vous devez indiquer un message')
	sys.exit()
if len(sys.argv) > 2:
	print('Erreur, vous avez indiquer trop d\'argument, essayez avec des apostrophes "')
	sys.exit()

message = sys.argv[1]
files = os.popen('ls -a').read().split('\n')
if '.git' not in files:
	os.popen('git init')
if 'origin' not in os.popen('git remote').read().split('\n'):
	origin = input('Add git origin url: ')
	os.popen(f'git remote add origin {origin}')
os.popen('git add .')
os.popen(f'git commit -m "{message}"')
os.popen('git pull origin master --allow-unrelated-histories')
os.popen('git push -f origin master')
