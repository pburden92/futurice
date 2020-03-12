# futurice
This app is a flask app built in python 3. It is running on nginix and uwsgi. At the time of writing this it is deployed at 54.154.24.216

Some unit tests are included in the tests folder.

Deployment:

  upload files to server with git.
      
      git clone https://github.com/pburden92/futurice.git
  
  install python3
  
      sudo apt-get install python3
  
  install pip3
  
      sudo apt-get install pip3
  
  pip install flask and uwsgi (also stored in requirements.txt)
  
      pip install flask uwsgi
  
  copy futureice.service to /lib/systemd/system/futurice.service
  
      cp futureice.service /lib/systemd/system/futurice.service
  
  create a symlink to /lib/systemd/system/futurice.service at /etc/systemd/system/multi-user.target.wants/futurice.service
  
      ln -s /lib/systemd/system/futurice.service /etc/systemd/system/multi-user.target.wants/futurice.service
  
  copy futurice.config to /etc/nginx/sites-available/futurice
  
      cp futurice.config /etc/nginx/sites-available/futurice
  
  run sudo service nginix start
  
      sudo service nginix start
  
  run sudo service futurice start
  
      sudo service futurice start
