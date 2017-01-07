#Ji Won Chung 
#Final Part I: Longest Words in a Text File
#Program reads words from text, prints out all the tied-for-longest words in text

def importText():
    '''Asks user for text file and turns into lower case
    '''
    filename = input("Enter Filename: ")
    text = open(filename)
    text = text.read()
    text = text.lower()
    
    return text, filename 


def RemPunct(text):
    '''Removes punctuation from text
    '''
    punct = ''',.?!"'-:;()/'''
    for word in text:
        if word in punct:
            text = text.replace(word, '')
            
    return text


def ConcordList(words):
    '''Creates a list of each words
    ''' 
    Lconcord = [] 
    for word in words:
        Lconcord.append(word)

    return Lconcord
    

def FindLongest(Lconcord):
    '''function that find & returns length of the longest word in Lconcord
    '''
    longest = ''
    
    for word in Lconcord:
        if len(word) >= len(longest):
            longest = word 

    return len(longest)
        
def Longest(Lconcord, length):
    '''function that returns a list of the longest words
    '''
    LongWords = []
    for word in Lconcord:
        if len(word) == length:
            LongWords.append(word)

    return LongWords

def main():
    '''function that takes text, transforms it, and prints output 
    '''

    #Take input text and its name 
    text, filename = importText()

    #Transform text to a list of wors
    text = RemPunct(text)
    words = text.split() 
    Lconcord = ConcordList(words)

    #finds the word with the longest length 
    longestlength = FindLongest(Lconcord)

    #makes a list with the longest length
    LongWords = Longest(Lconcord, longestlength)

    #alphebatize words in order
    LongWords.sort()
    
    #Statements 
    Statement1 = 'The Longest words in the text have'
    Statement1end = 'letters'
    Statement2 = 'Here are all the words of length'
    S2Length = len(str(longestlength)) + len(Statement2) + 1
     
    #Print Statements
    print(Statement1, longestlength, Statement1end)
    print(Statement2, longestlength)
    print(S2Length * '-')
    for word in LongWords:
        print(word)
    
    
main()
