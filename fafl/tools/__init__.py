import codecs

# for timeouts
import subprocess, threading

# to run a process with timeout
class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout*3)
        if thread.is_alive():
            flash('Process is taking too long and will be terminated!', 'error')
            self.process.terminate()
            thread.join()

def write_file(path, contents):
    UTF8Writer = codecs.getwriter('utf8')
    with open(path, 'w') as dest_file:
        dest_file.write(contents) #.encode('utf8'))

import subprocess
import os

