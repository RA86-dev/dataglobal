import subprocess
import requests
import threading
import os
from webbrowser import open_new
class fetch:
    def __init__(self, url,finalFileName):
        self.url = url
        self.fName = finalFileName

    def run_safety(self):
        r = self.url
        requestAD = requests.get(str(r))
        if requestAD.status_code == 200:
            with open(f'{os.getcwd()}/{self.fName}', 'w') as c:
                c.write(str(requestAD.text))
            process = subprocess.Popen(f"bandit {os.getcwd()}/{self.fName}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            print(f"{stdout.decode()}")

    def run(self):
        def x():
            r = self.url
            requestAD = requests.get(str(r))
            if requestAD.status_code == 200:
                with open(f'{os.getcwd()}/{self.fName}', 'w') as c:
                    c.write(str(requestAD.text))
                process = subprocess.Popen(f"bandit {os.getcwd()}/{self.fName}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                print(f"{stdout.decode()}")
                print('Do you want to delete or keep the program?')
                iTC = input(' (Y: Delete, N: Dont Delete) y/n :')
                if iTC.upper() == "Y":
                    os.system(f'rm {self.fName}')
                else:
                    print('OK!')

                    
        
        
        # Run directly
        x()
# Example usage:

if __name__ == "__main__":
    print('In order to create a class, find a document on github repository. Copy the raw URL for the code, and put it in here:')
    iX = input('Input: ')
    iC = input('Output filename: ')
    fetchRef = fetch(iX,iC)
    while True:
        print('=' * 50)
        print('1. View security malicious')
        print('2. Run download')
        print('=' * 50)
        i = int(input(''))
        if i == 1:
            fetchRef.run_safety()
        elif i == 2:
            fetchRef.run()
