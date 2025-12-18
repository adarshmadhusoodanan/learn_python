import re
data="I AM NOT IN DANGER, I AM THE DANGER, NOW SAY MY NAME"
res=re.search('DANGER',data)
if res is None:
    print("Search Not Found")
else:
    print("Search Found")
# op:
# Search Found

# span:
data="I AM NOT IN DANGER, I AM THE DANGER, NOW SAY MY NAME"
patterns=['DANGER','NAME','SAY','RAHUL']
for pat in patterns:
    print("Searching for pattern ->",pat)
    res=re.search(pat,data)
    if res!=None:
        print("Match found at ->",res.span())
    else:
        print("Match not found")
# op:
# Searching for pattern -> DANGER
# Match found at -> (12, 18)
# Searching for pattern -> NAME
# Match found at -> (48, 52)
# Searching for pattern -> SAY
# Match found at -> (41, 44)
# Searching for pattern -> RAHUL
# Match not found

# findall:
message="dont trouble the trouble , if you trouble the trouble ," \
"trouble troubles you , i am not the trouble , i am the truth"
res=re.findall('trouble',message)
print(res)
# op:
# ['trouble', 'trouble', 'trouble', 'trouble', 'trouble', 'trouble', 'trouble']

message = "dont trouble the trouble , if you trouble the trouble , " \
"trouble troubles you , i am not the trouble , i am the truth"
for match in re.finditer('trouble', message):
    print(match.group(), "at", match.start(),",",match.end())
# trouble at 5 , 12
# trouble at 17 , 24
# trouble at 34 , 41
# trouble at 46 , 53
# trouble at 56 , 63
# trouble at 64 , 71
# trouble at 92 , 99

data2='superCalifragilisticexpialdicious'
res=re.search('supe[a-z]',data2)
# Match found
res=re.search('supe[p-t]',data2)
# Match found
res=re.search('supe[a-m]',data2)
# Match Not found
res=re.search('supe[a-z][A-Z]',data2)
# Match found
res=re.search('supe[a-z][A-Z][0-9]',data2)
# Match Not found
if res!=None:
    print('Match found')
else:
    print('Match Not found')

def multi_char_find(text_message,test_pattern):
    for pat in test_pattern:
        print("Searching for pattern",pat)
        print(re.findall(pat,text_message))
text_message="aaaabbbb...ababababaaabbb...aabbaabb...abababaabaaab"
test_pattern=['a+']
# ['aaaa', 'a', 'a', 'a', 'a', 'aaa', 'aa', 'aa', 'a', 'a', 'a', 'aa', 'aaa']

# It will look for a for one or more occurance 

test_pattern=['a*']
# Searching for pattern a*
# ['aaaa', '', '', '', '', '', '', '', 'a', '', 'a', '', 'a', '', 'a', '', 'aaa'
#  , '', '', '', '', '', '', 'aa', '', '', 'aa', '', '', '', '', '', 'a', '', 'a',
#    '', 'a', '', 'aa', '', 'aaa', '', '']

# It will look for character a for zero or more occurance 

test_pattern=['ab']
# Searching for pattern ab
# ['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']

# It will look for combination of a and b only

test_pattern=['ab+']
# Searching for pattern ab+
# ['abbbb', 'ab', 'ab', 'ab', 'ab', 'abbb', 'abb', 'abb', 'ab', 'ab', 'ab', 'ab', 'ab']

# It will look for the combination of a and b in that a should be present 1 occurance and b for 1 or more occurance

test_pattern=['ab*']
# Searching for pattern ab*
# ['a', 'a', 'a', 'abbbb', 'ab', 'ab', 'ab', 'ab', 'a', 'a', 'abbb', 'a', 'abb', 'a',
#   'abb', 'ab', 'ab', 'ab', 'a', 'ab', 'a', 'a', 'ab']

# It will look for the combination of a and b in that a should be present 1 occurance and b for 0 or more occurance

test_pattern=['[ab]+']
# Searching for pattern [ab]+
# ['aaaabbbb', 'ababababaaabbb', 'aabbaabb', 'abababaabaaab']

# It will look for the combination of a and b in that a and b can present for one or more occurance 

test_pattern=['[ab]*']
# Searching for pattern [ab]*
# ['aaaabbbb', '', '', '', 'ababababaaabbb', '', '', '', 'aabbaabb', '', '', '', 'abababaabaaab', '']

# It will look for the combination of a and b in that a and b can present for zero or more occurance 

multi_char_find(text_message,test_pattern)