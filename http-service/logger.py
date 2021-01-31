import sys
import os

class logging:
    def __init__(self, fileLocation, infoFile, debugFile):
        self.location = fileLocation
        self.infoFile = infoFile
        self.debugFile = debugFile
        
        #self.firstStart()

    def firstStart(self):
        os.system(f'rm {self.location}{self.infoFile}')
        os.system(f'rm {self.location}{self.debugFile}')

    def info(self, msg):
        os.system(f'echo "{msg}" >> {self.location}{self.infoFile}')

    def debug(self, msg):
        os.system(f'echo "{msg}" >> {self.location}{self.debugFile}')