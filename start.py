import os
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

django_framework = 'Django_framework'
flask_framework = '../Flask_framework'
pyramid_framework = '../Pyramid_framework'
compare_py_web_frameworks = '../ComparePyWebFrameworks'

#Build django_framework image 
os.chdir(django_framework)
os.system('docker build -t=django_framework .')

#Build flask_framework image
os.chdir(flask_framework)
os.system('docker build -t=flask_framework .')

#Build pyramid_framework image
os.chdir(pyramid_framework)
os.system('docker build -t=pyramid_framework .')

#Build main service
os.chdir(compare_py_web_frameworks)
os.system('sudo chown -R 472 grafana/')
os.system('docker-compose up -d --build')