direction = ['north', 'south', 'east', 'west']
verb = ['go', 'kill', 'eat', 'smack', 'open']
stop = ['the', 'in', 'of', 'and']
noun = ['bear', 'princess', 'nose', 'door']

def to_number(word):
    try:
        number = int(word)
        return number
    except ValueError:
        raise ValueError('Word is not a number')

def scan(sentence):
    tokens = []
    words = sentence.split()
    for word in words:
        tword = word.lower()
        if tword in direction:
            tokens.append(('direction', word))
        elif tword in verb:
            tokens.append(('verb', word))
        elif tword in stop:
            tokens.append(('stop', word))
        elif tword in noun:
            tokens.append(('noun', word))
        else:
            try:
                number = to_number(tword)
                tokens.append(('number', number))
            except ValueError:
                tokens.append(('error', word))
    return tokens
