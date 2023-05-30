from git import Repo

repo = Repo('/home/pi/ut_real')
repo.git.add('data.json')
repo.index.commit('data.json upload')
origin = repo.remote(name='origin')
origin.push()

