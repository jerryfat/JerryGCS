from subprocess import Popen, PIPE

if __name__ == '__main__':
    #os.system('python3 ./pyG5/pyG5ViewTester.py')
    #
    # add PyG5 window
    process = Popen(['python3', './pyG5/pyG5ViewTester.py'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
