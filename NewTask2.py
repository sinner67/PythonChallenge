import sys, codecs

def countLetters(word):
    allLetters = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁёйцукенгшщзхъфывапролджэячсмитьбю'
    count = 0
    for i in word:
        if i in allLetters:
            count += 1
    return count

def toUpperFrstLttr(word):
    result = str(word[0]).upper() + str(word[1:])
    return result

if len(sys.argv) == 2:
    nameFile = sys.argv[1]
    reader = codecs.open(nameFile, 'r', encoding='utf-8')
    text = reader.read()
    reader.close()
    words = str(text).split(' ')
    for i in range(len(words)):
        if countLetters(words[i]) > 6:
            words[i] = toUpperFrstLttr(words[i])
    result = ''
    writer = codecs.open(nameFile, 'w', encoding='utf-8')
    for i in words:
        result += i + ' '
    writer.write(result)
    writer.close()
    print(result)
    
    
