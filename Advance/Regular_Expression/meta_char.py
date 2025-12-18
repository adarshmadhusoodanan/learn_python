import re
def multi_char_find(text_message,test_pattern):
    for pat in test_pattern:
        print("Searching for pattern",pat)
        print(re.findall(pat,text_message))
text_message="A@@ Boy## Purchase12 A BulleT#1 345 && ToTake! His123 123 Girlfriend to@+1 a LongRide#$"

test_pattern=['[a-z]+']
# Searching for pattern [a-z]+
# ['oy', 'urchase', 'ulle', 'o', 'ake', 'is', 'irlfriend', 'to', 'a', 'ong', 'ide']

test_pattern=['[A-Z]+']
# Searching for pattern [A-Z]+
# ['A', 'B', 'P', 'A', 'B', 'T', 'T', 'T', 'H', 'G', 'L', 'R']

test_pattern=['[0-9]+']
# Searching for pattern [0-9]+
# ['12', '1', '345', '123', '123', '1']

test_pattern=['\d']
# Searching for pattern \d
# ['1', '2', '1', '3', '4', '5', '1', '2', '3', '1', '2', '3', '1']

test_pattern=['\d+']
# Searching for pattern \d+
# ['12', '1', '345', '123', '123', '1']

test_pattern=['\D+']
# Searching for pattern \D+
# ['A@@ Boy## Purchase', ' A BulleT#', ' ', ' && ToTake! His', ' ', ' Girlfriend to@+', ' a LongRide#$']

test_pattern=['\s+']
# Searching for pattern \s+
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

test_pattern=['\S+']
# Searching for pattern \S+
# ['A@@', 'Boy##', 'Purchase12', 'A', 'BulleT#1', '345', '&&', 'ToTake!', 'His123', '123',
#   'Girlfriend', 'to@+1', 'a', 'LongRide#$']

test_pattern=['\w+']
# Searching for pattern \w+
# ['A', 'Boy', 'Purchase12', 'A', 'BulleT', '1', '345', 'ToTake', 'His123', '123', 'Girlfriend', 'to', '1', 'a', 'LongRide']

test_pattern=['\W+']
# Searching for pattern \W+
# ['@@ ', '## ', ' ', ' ', '#', ' ', ' && ', '! ', ' ', ' ', ' ', '@+', ' ', ' ', '#$']

test_pattern=['[^#@e3E]+']
# Searching for pattern [^#@e3E]+
# ['A', ' Boy', ' Purchas', '12 A Bull', 'T', '1 ', '45 && ToTak', '! His12', ' 12', ' Girlfri', 'nd to', '+1 a LongRid', '$']

multi_char_find(text_message,test_pattern)

data='The most violent man called one man the most violent'
res=re.search(r'\AThe',data)
# Match found
res=re.search(r'lent\Z',data)
# Match found
if res!=None:
    print('Match found')
else:
    print('Match Not found')

data2='I feel a feel a funny feel , a funny feel I feel , If you feel the feel I feel, a funny feel you feel'
res=re.search(r'\bfee',data2)
# Match found
res=re.search(r'eel\b',data2)
# Match found
if res!=None:
    print('Match found')
else:
    print('Match Not found')

data='life is colorfull'
res=re.search('colou?r',data)
# Match found
if res!=None:
    print('Match found')
else:
    print('Match Not found')