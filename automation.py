import subprocess
def open_editor():
    subprocess.run('code', shell=True)
open_editor()
def github_push():
    subprocess.run('git add', shell=True)
    subprocess.run('git commit -m "Automated commit"', shell=True)
    subprocess.run('git push', shell=True)
print('Automation Started')