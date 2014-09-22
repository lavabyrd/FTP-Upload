import os
from ftplib import FTP
 
os.chdir('c:\\temp')
 
## allows reset of file names, only used for testing
 
def reset():
    dub = '12345678.sps'
    snn = '34567890.sps'
    ork = '98765432.sps'
    toplion41940 = '41940123.sps'
    sportsfac80790 = '80790345.sps'
    ibm = 'temp111.dat'
    for file in os.listdir('c:\\temp'):
        if file.endswith('12345678.sps'):
            os.rename(file, dub)
        elif file.endswith('34567890.sps'):
            os.rename(file, snn)
        elif file.endswith('98765432.sps'):
            os.rename(file, ork)
        elif file.endswith('41940123.sps'):
            os.rename(file, toplion41940)
        elif file.endswith('80790345.sps'):
            os.rename(file, sportsfac80790)
        elif file.endswith('ibmfile.sps'):
            os.rename(file, ibm)
 
## standard file rename function which renames all files in a folder but also asks for station name should file not be recognised
 
def main():
    for file in os.listdir('c:\\temp'):
        dub = 'DUB0000000109SPS' + file
        ork = 'DUB0000000502SPS' + file
        snn = 'DUB0000000510SPS' + file
        toplion41940 = 'DUB0000000435SPS' + file
        sportsfac80790 = 'DUB0000000435SPS' + file
        ibm = 'ibmfile.sps'
        if file.startswith('41940'):
            os.rename(file, toplion41940)
        elif file.startswith('80790'):
            os.rename(file, sportsfac80790)
        elif file.endswith('.dat'):
            os.rename(file, ibm)
        elif file.endswith('.sps'):
            station = raw_input('What station do you want to upload to? (choose dub, ork or snn)')
            if station.lower() == 'dub':
                os.rename(file, dub)
            elif station.lower() == 'ork':
                os.rename(file, ork)
            elif station.lower() == 'snn':
                os.rename(file, snn)
 
## ftp upload script
 
def dcs_upload():
    ftp = FTP('1')
    username = '111'
    password = '111'
    ftp.login(username, password)
    ftp.cwd('/in/work_test')
    for file in os.listdir('c:\\temp'):
        stored = 'proc/' + file
        myfile = open(file, 'r')
        ftp.storlines('STOR ' + file, myfile)
        myfile.close()
    ftp.quit()
 
def file_move():
    for file in os.listdir('c:\\temp'):
        stored = 'proc/' + file
        if file.endswith('.sps'):
            os.renames(file, stored)
 
 
main()
dcs_upload()
# file_move()
# reset()
