import os
from pathlib import Path
import shutil

#Make folder for all
os.mkdir('../' 'BenchmarkPyWebFrameworks')

os.chdir('../BenchmarkPyWebFrameworks')

shutil.move('ComparePyWebFrameworks', '.')

os.system('git clone https://github.com/comparepywebframework/Django_framework.git ..')
os.system('git clone https://github.com/comparepywebframework/Flask_framework.git ..')
os.system('git clone https://github.com/comparepywebframework/Pyramid_framework.git ..')

django_framework = Path('BenchmarkPyWebFrameworks/Django_framework')
flask_framework = Path('BenchmarkPyWebFrameworks/Flask_framework')
pyramid_framework = Path('BenchmarkPyWebFrameworks/Pyramid_framework')

#Build main service
os.system('docker-compose up -d --build')

#Build Django_framework service
os.chdir(str(django_framework))
os.system('docker-compose up -d --build')

#Build Flask_framework service
os.chdir(str(flask_framework))
os.system('docker-compose up -d --build')

#Build Pyramid_framework service
os.chdir(str(pyramid_framework))
os.system('docker-compose up -d --build')