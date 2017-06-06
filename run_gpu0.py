import glob
import subprocess

if __name__ == '__main__':
    wildcard = '*winterfell*gpu0*.py'
    gpu0_scripts = sorted(glob.glob(wildcard))
    for script in gpu0_scripts:
        command = "python -u " + script + '> ' + script.split('.')[0] + '.log'
        print('='*100)
        print("Now running:{}".format(command))
        print('='*100)
        subprocess.call("which python", shell=True)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print(process.returncode)
