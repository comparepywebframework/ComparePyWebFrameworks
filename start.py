import os
from pathlib import Path

os.system('git clone https://github.com/comparepywebframework/Django_framework.git ..')
os.system('git clone https://github.com/comparepywebframework/Flask_framework.git ..')
os.system('git clone https://github.com/comparepywebframework/Pyramid_framework.git ..')

django_framework = Path('../Django_framework')
flask_framework = Path('../Flask_framework')
pyramid_framework = Path('../Pyramid_framework')

#Build main service
os.system('docker-compose up -d')

#Build Django_framework service
os.chdir(str(django_framework))
os.system('docker-compose up -d')

#Build Flask_framework service
os.chdir(str(flask_framework))
os.system('docker-compose up -d')

#Build Pyramid_framework service
os.chdir(str(pyramid_framework))
os.system('docker-compose up -d')