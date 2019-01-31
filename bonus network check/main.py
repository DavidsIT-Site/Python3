import subprocess
from shutil import copyfile
from timeit import default_timer as timer

network_test_list = ['10.10.10.14', '10.10.10.18', '10.10.10.1', '10.10.10.2', 'www.google.com']
network_test_list = [ 'www.google.com']

upload_tmp_dir = "S:\\software\\FW_tests\\temp"


name = input("what is this test called? ")
output = []

for item in network_test_list:
    p = subprocess.Popen(['ping.exe', item], stdout=subprocess.PIPE)
    response = (p.communicate()[0])
    #print(response)
    output.append(response)

# clean temp folder


# temp folder speedtests
import os
import glob

files = glob.glob('S:\\software\\FW_tests\\temp\\*')
for f in files:
    os.remove(f)


start = timer()
copyfile("S:\\software\\FW_tests\\10mb.bin", "S:\\software\\FW_tests\\temp\\10mb.bin")
end = timer()
time = (end - start)
speed = 50/time
output.append("\n10MB test speed:{} Time:{}".format(speed, time))
with open('S:\\software\\FW_tests\\{}.txt'.format(name), 'wt') as f:
    for item in output:
        print(item, file=f)