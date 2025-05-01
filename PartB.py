import sys
import os
import PartA
'''
Author Name: Soumya Sharma
Student ID: 16463723

Time complexity of collecting tokens from file is described in PartA.py
Time complexity of filtering common words from 2 files is, at worst, O(len(file1TokenList)) * O(len(file2TokenList))
O(len(file1TokenList)) * O(len(file2TokenList)) takes less time than O(n^2) as long as 1 file has less words than the other
for which complexity will be O(min(len(file1TokenList), len(file2TokenList))
'''

def findCommonTokens(textFile1, textFile2):
	file1TokenList = PartA.tokenize(textFile1) #CREATE LIST OF TOKENS FOR FILE 1
	file2TokenList = PartA.tokenize(textFile2) #CREATE LIST OF TOKENS FOR FILE 1
	commonTokenLst = list(set(file2TokenList).intersection(file1TokenList))
	print(len(commonTokenLst))
	
	
		    

if __name__ == "__main__":
        check = True
        if (len(sys.argv) != 3): #CHECK COMMAND LINE HAS 3 ARGUMENTS
                check = False
                print("Please enter two file names to compare") #ERROR MESSAGE
        if (check == True):
                file1 = sys.argv[1] #1ST FILE NAME
                file2 = sys.argv[2] #2ND FILE NAME
                if not os.path.isfile(file1): #CHECK FILE PATH EXISTS
                        check = False
                        print("First File Not Found") #ERROR MESSAGE
                if not os.path.isfile(file2): #CHECK FILE PATH EXISTS
                        check = False
                        print("Second File Not Found") #ERROR MESSAGE
                if(check == True):
                        findCommonTokens(file1, file2) #FIND COMMON TOKENS
