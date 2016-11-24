#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListFileReader:

    """ A FileListReader """

    def readIntoArray(self,capatialize=False):
        """ Returns an array containing all the data """
        if capatialize:
            with open(self.txtFileName) as textFile:
                array = textFile.read().upper().splitlines()
        else:
            with open(self.txtFileName) as textFile:
                array = textFile.read().splitlines()
        return array
    
    def contains(self,value):
        """ Returns  True or False depending on the contents"""
        if self.indexOf(value)!=-1:
            return True
        else:
            return False

    def indexOf(self,value): 
        """ Returns  the position of the word starting from 0 and -1 if it doesn't have the value"""  
        try:
            return self.array.index(value)
        except ValueError:
            return -1
    def getPart(self, start, end):
        """ Returns an array containing all the data between start and end """
        return self.array[start:end]
    def containsAllOf(self, array):
        """ Returns true if the File has all the data provided in the array """
        for i in array:
            if(self.contains(i)):
                continue
            else:
                return False
        return True

    def getValuesThatHave(self,value,anycase=False):
        """ (String Operation) Returns all the Values of array that contains given value """
        array=[]
        if anycase:
            for v in self.array:
                if str(value).upper() in v.upper():
                    array.append(v)
            return array
        else:
            for v in self.array:
                if str(value) in v:
                    array.append(v)
            return array
    def __init__(self, txtFileName):
        self.txtFileName = txtFileName
        self.array = self.readIntoArray()









			