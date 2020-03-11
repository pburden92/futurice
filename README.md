# futurice
This app is a flask app built in python 3. It is running on nginix and uwsgi. At the time of writing this it is deployed at 54.154.24.216

Deployment:

  upload files to server with git.
  
  install python3
  
  install pip3
  
  pip install flask and uwsgi (also stored in requirements.txt)
  
  copy futureice.service to /lib/systemd/system/futurice.service
  
  create a symlink to /lib/systemd/system/futurice.service at /etc/systemd/system/multi-user.target.wants/futurice.service
  
  copy futurice.config to /etc/nginx/sites-available/futurice
  
  run sudo service nginix start
  
  run sudo service futurice start
