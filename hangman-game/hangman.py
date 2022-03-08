def hangman (word):
    tryword = '_' * len(word)
    lettersUsed = ''
    attempts = 0
    printTryWord(tryword)
    while (attempts < 7 and tryword != word):
        letter = str(input('Write a letter: '))
        if isLetter(letter, word):
            tryword = completeTryWord(letter, word, tryword)
        else:
            lettersUsed += letter + ','
            attempts += 1
            if(attempts == 7):
                print('you lose')
        if(attempts != 7):
            print('====================')
            printAttempts(attempts)
            printTryWord(tryword)
            print('Letters already used:', lettersUsed)

def isLetter(letter, word):
    for letterword in word:
        if letter.lower() == letterword.lower():
            return True
    return False
    
def completeTryWord(letter, word, try_word):
    newTryWord = ''
    for i in range(0, len(word)):
        if letter.lower() == word[i].lower() and try_word[i] == '_':
            newTryWord += word[i]
        elif letter.lower() == word[i].lower() and try_word[i] != '_':
            newTryWord += word[i]
        else:
            newTryWord += try_word[i]
    return newTryWord

def printTryWord(tryword):
    newTryWord = ''
    for letter in tryword:
         newTryWord += letter + ' '
    print(newTryWord + '\n')
    
def printAttempts(attempts):
    if attempts == 0:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |          ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
    if attempts == 1:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |         O ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
    if attempts == 2:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |         O ')
        print('  |         | ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
    if attempts == 3:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |         O ')
        print('  |        /| ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
    if attempts == 4:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |         O ')
        print('  |        /|\ ')
        print('  |          ')
        print('  |          ')
        print('  |          ')
    if attempts == 5:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |         O ')
        print('  |        /|\ ')
        print('  |        / ')
        print('  |          ')
        print('  |          ')
    if attempts == 6:
        print('   _ _ _ _ _ ')
        print('  /         |')
        print('  |         O ')
        print('  |        /|\ ')
        print('  |        / \ ')
        print('  |          ')
        print('  |          ')
    
    
    
    
word = 'Arroz'
hangman(word)