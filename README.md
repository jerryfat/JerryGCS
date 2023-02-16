##############################################################
unpack and install

  #cd to a dir to create new python3 venv dir homedir
1. $ cd ~ (your home dir)

  #download gzip from google drive MAVGCSenvXXX.tar.gz 
  
2. in browser get and download archive https://drive.google.com/file/d/19LrXMyKB2iBbJIoNWBW54-RlgCcncsM7/view?usp=share_link 
  # tar.gz archive is 128mb you will need total unpacked sized of 428 MB user space to run app
  #   unpack archive , a. let archive manager unpack dir MAVGCSenv130 into local virtual env dir MAVGCSenv130 env dir:
  # OR b. manually unpack if not using archive manager for MAVGCSenv130.tar.gz  $ tar -zxvf  MAVGCSenv130.tar.gz MAVGCSenv130
3.$ cd MAVGCSenv130         #unpacking should have 'created MAVGCSenv130 dir'
4.#now install the required python packages for this app only in the venv folder

$ python3 -m pip install -r requirements.txt
5.
  #activate venv environement
$ source ./bin/activate
(env) jf@jf1:~/MAVGCSenv132$ 
(env) jf@jf1:~/MAVGCSenv132$ python3 mavlink134.py
(env) jf@jf1:deactivate
jf@jf1:~/MAVGCSenv132$ 

6.
  #run app:
$ (venv) python3 mavlink130.py

  #deactivate virtual env
$ deactivate 

in ubuntu18,19,20 open a terminal alt-ctl T
$ 
$ git clone git@github.com:jerryfat/JerryGCS.git
$ cd JerryGCS/
$ python3 -m pip install -r requirements.txt
using local virtual python3
$ source ./bin/activate
(env) jf@jf1:~/MAVGCSenv132$ 
(env) jf@jf1:~/MAVGCSenv132$ python3 mavlink134.py
(env) jf@jf1:deactivate
using global python3
$ python3 mavlink134.py 
 
 
# JerryGCS
