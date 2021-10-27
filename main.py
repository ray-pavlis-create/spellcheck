# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    menu = True
    for i in range(len(aliceWords)):
      aliceWords[i] = aliceWords[i].lower()

    while menu:
        print("MAIN MENU")
        print("1. Spell Check a Word (Linear Search)")
        print("2. Spell Check a Word (Binary Search)")
        print("3. Spell Check Alice in Wonderland (Linear Search)")
        print("4. Spell Check Alice in Wonderland (Binary Search)")
        print("5. Exit")
        selection = input("Enter menu selection (1-5): ")

        if selection == "1":
            linSearch = input("Please enter a word: ")
            linSearch = linSearch.lower()
            start = time.time()
            position = linearSearch(dictionary, linSearch)
            if position >= 0:
              end = time.time()
              totalTime = end - start
              print(linSearch + " was found at position " + str(linearSearch(dictionary, linSearch)))
              print("Time:", totalTime)
            else:
              print(linSearch + " was not found.")
            
        elif selection == "2":
            binSearch = input("Please enter a word: ")
            binSearch = binSearch.lower()
            start = time.time()
            position = binarySearch(dictionary, binSearch)
            if position >= 0:
              end = time.time()
              totalTime = end - start
              print(binSearch + " was found at position " + str(binarySearch(dictionary, binSearch)))
              print("Time:", totalTime)
            else:
              print(binSearch + " was not found.")
            
        elif selection == "3":
          notFound = 0
          start = time.time()
          for i in range(len(aliceWords)):
            if (linearSearch(dictionary, aliceWords[i])) == -1:
              notFound += 1
          end = time.time()
          totalTime = end - start
          print(notFound, "words were not found in the dictionary.")
          print("Time:", totalTime)

        elif selection == "4":
          notFound = 0
          start = time.time()
          for i in range(len(aliceWords)):
            if (binarySearch(dictionary, aliceWords[i])) == -1:
              notFound += 1
          end = time.time()
          totalTime = end - start
          print(notFound, "words were not found in the dictionary.")
          print("Time:", totalTime)

        else:
            menu = False
            print("goodbye")
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSearch(anArray, item):
  for i in range(len(anArray)):
    if anArray[i] == item:
      return i
    
  return -1

def binarySearch(anArray, item):
  lowerIndex = 0
  upperIndex = len(anArray) - 1

  while lowerIndex <= upperIndex:
    middleIndex = (lowerIndex + upperIndex) // 2

    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      upperIndex = middleIndex - 1
    else:
      lowerIndex = middleIndex + 1

  return -1

# Call main() to begin program
main()
