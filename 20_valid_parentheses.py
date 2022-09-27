import sys

s = "(]"

while True:
    if '()' in s:
        s = s.replace('()', '')
    
    elif '{}' in s:
        s = s.replace('{}', '')
    
    elif '[]' in s:
        s = s.replace('[]', '')

    else:
        if s == '':
            print('true')
            break
        else:
            print('false')
            break