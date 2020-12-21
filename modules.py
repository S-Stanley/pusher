import os

class Commit():
	def __init__(self, message: str = 'PUSH made by pusher https://github.com/S-Stanley/pusher.git'):
		self.message = message

	@staticmethod
	def check_repo():
		files = os.popen('ls -a').read().split('\n')
		if '.git' not in files:
			os.popen('git init').read()

	@staticmethod
	def get_remote():
		if 'origin' not in os.popen('git remote').read().split('\n'):
			origin = input('Add git origin url: ')
			os.popen(f'git remote add origin {origin}').read()

	def get_branch(self):
		all_branch = os.popen('git branch').read().split('\n')
		for br in all_branch:
			if '*' in br:
				self.branch = br.replace('*', '').replace(' ', '')
				break

	def send(self):
		os.popen(f'git add . && git commit -m "{self.message}" && git pull origin {self.branch}').read()
		os.popen(f'git push origin {self.branch}').read()