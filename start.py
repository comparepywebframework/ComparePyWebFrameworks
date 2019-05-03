import os
from pathlib import Path
import shutil

#Make folder for all
os.mkdir('../' 'BenchmarkPyWebFrameworks')

shutil.move('start.py', '../BenchmarkPyWebFrameworks')
os.chdir('..')
shutil.move('ComparePyWebFrameworks', 'BenchmarkPyWebFrameworks')

os.chdir('BenchmarkPyWebFrameworks')

os.system('git clone https://github.com/comparepywebframework/Django_framework.git')
os.system('git clone https://github.com/comparepywebframework/Flask_framework.git')
os.system('git clone https://github.com/comparepywebframework/Pyramid_framework.git')

django_framework = Path('../Django_framework')
flask_framework = Path('../Flask_framework')
pyramid_framework = Path('../Pyramid_framework')
compare_py_web_frameworks = Path('ComparePyWebFrameworks')

#Build main service
os.chdir(str(compare_py_web_frameworks))
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