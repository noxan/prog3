# -*- coding: utf-8 -*-
"""
Created on Sun Nov  18 19:45:10 2012

@author: Stefan Durner
"""


class ConfigManager(object):

# ließt und schreibt config file

    def __init__(self, config):
        self.config = config

    def getConfig(self, name):

# holt den wert aus dem file

        with open(self.config) as configfile:
            for line in configfile:
                line = line.strip()
                wort = line.split(" = ")
                if wort[0] == name:
                    return wort[1]

    def setConfig(self, name, value):

# schreibt einen neuen wert ins file

        oldValue = self.getConfig(name)
        config = open("config.txt")
        file = ""
        for line in config:
            file = file + line
        config.close
#        print file
        oldline = name + " = " + str(oldValue)
        newline = name + " = " + str(value)
        file = file.replace(oldline, newline)
#        print file
        writeConfig = open("config.txt", "w")
        writeConfig.write(file)
        writeConfig.close
