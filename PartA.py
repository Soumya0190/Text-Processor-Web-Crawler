import sys
import os
'''
Author : Soumya Sharma
Student ID: 16463723

Time complexity of collecting words from file into wordLst is O(n)
Time complexity of filtering alphanumeric words into alphanumLst is O(n)
Time complexity of filtering tokens (sequence of >=2 characters) is O(n)
'''
def tokenize(TextFilePath):
        
        wordLst = [word for word in open(TextFilePath, 'r').read().split()]
        alphanumLst = [i.lower() for i in wordLst if i.lower().isalnum()]
        return [token for token in alphanumLst if len(token) >= 2]




'''
Time complexity of calulating frequency of each token from file is O(n)
'''
def computeWordFrequencies(tokenList):
        freqMap = {} #MAP OF TOKEN AND FREQUENCIES
        for token in tokenList: #READ EACH TOKEN IN LIST
                if token in freqMap.keys(): #CHECK TOKEN IN DICTIONARY
                        freqMap[token] = freqMap[token] + 1 #INCREMENT FREQUENCY OF TOKEN
                else: #CHECK TOKEN NOT IN DICTIONARY
                        freqMap[token] = 1 #SET TOKEN FREQUENCY TO 1
        return freqMap #RETURN MAP


'''
Time complexity of sorting dictionary by values (frequency of token) is O(n log n)
Time complexity of printing each token with frequency is O(n)
'''
def printFreq(frequencies):
        sortedFrequencies = dict(sorted(frequencies.items(), key = lambda item: item[1], reverse = True)) #SORT MAP DESCENDING ORDER OF FREQUENCIES
        for item in sortedFrequencies.items(): #FOR EACH ITEM IN MAP
                print("{}\t{}".format(item[0], item[1])) #PRINT TOKEN-FREQUENCY

		    
if __name__ == "__main__":
        check = True
        if (len(sys.argv) < 2): #CHECK COMMAND LINE HAS 2 ARGUMENTS "python PartA.py TextFileName"
                print("File Name Not Found") #ERROR MESSAGE
        file = sys.argv[1] #GET FILE NAME
        if not os.path.isfile(file): #CHECK FILE PATH EXISTS
                print("File Not Found") #ERROR MESSAGE
        else:
                lst = tokenize(file) #TOKENIZE FILE
                freqDict = computeWordFrequencies(lst) #COMPUTE TOKEN FREQUENCIES
                printFreq(freqDict) #PRINT TOKENS WITH FREQUENCIES
    
    
