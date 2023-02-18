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
4.now install the required python packages for this app only in the venv folder

 
  use browser to download zip to your local home https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip 
  or commandline 
$ firefox https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip
$ archive-manager will ask where to extract: I chose /home/jf/JerryGCS-main
$ cd /home/jf/JerryGCS-main
$ python3 -m pip install -r requirements.txt
5.$ python3 mavlink134.py
$ python3 mavlink134.py
 
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
or
in browser 
wget https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip

$ cd JerryGCS/ or JerryGCS-main/
$ python3 -m pip install -r requirements.txt
using local virtual python3
creating new env
python3 -m venv /path/to/new/virtual/environment
$ source ./bin/activate
(env) jf@jf1:~/MAVGCSenv132$ 
(env) jf@jf1:~/MAVGCSenv132$ python3 mavlink134.py
(env) jf@jf1:deactivate
using global python3
$ python3 mavlink134.py 
 
 jf@jf1:~/Downloads$ wget https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip
 
Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/jf/.wget-hsts'. HSTS will be disabled.
--2023-02-16 21:14:06--  https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip
Resolving github.com (github.com)... 140.82.114.3
Connecting to github.com (github.com)|140.82.114.3|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://codeload.github.com/jerryfat/JerryGCS/zip/refs/heads/main [following]
--2023-02-16 21:14:06--  https://codeload.github.com/jerryfat/JerryGCS/zip/refs/heads/main
Resolving codeload.github.com (codeload.github.com)... 140.82.113.9
Connecting to codeload.github.com (codeload.github.com)|140.82.113.9|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [application/zip]
Saving to: ‘main.zip’

main.zip                [  <=>               ]  22.21M  2.99MB/s               ^C



 Github needs a public token if uploading cloning my JerryGCS

Instead of clone command use browser to download zip file and unpack using ubntu archive manager that starts automatically

 1. use browser to download zip to your local home https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip
  or commandline
  $ firefox https://github.com/jerryfat/JerryGCS/archive/refs/heads/main.zip
 2. $ archive-manager will ask where to extract: I chose /home/jf/JerryGCS-main
 3. $ cd /home/jf/JerryGCS-main (where u extracted)
 4. $ python3 -m pip install -r requirements.txt$ python3 mavlink134.py
 5. $ python3 mavlink134.py
# JerryGCS
