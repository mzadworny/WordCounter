import operator

words = '''
I've been watchin' you for some time
Can't stop starin' at those ocean eyes
Burning cities and napalm skies
Fifteen flares inside those ocean eyes
Your ocean eyes
No fair
You really know how to make me cry
When you gimme those ocean eyes
I'm scared
I've never fallen from quite this high
Fallin' into your ocean eyes
Those ocean eyes
I've been walkin' through a world gone blind
Can't stop thinkin' of your diamond mind
Careful creature made friends with time
He left her lonely with a diamond mind
And those ocean eyes
No fair
You really know how to make me cry
When you gimme those ocean eyes
I'm scared
I've never fallen from quite this high…
'''
remove_these = [',', '.', '…']
for thing in remove_these:
  words = words.replace(thing,"")
words = words.lower()

word_list = words.split()
word_count = {}

for word in word_list:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1),reverse=True)

print(f'There are {len(sorted_count)} unique words in this.')

for word_tuple in sorted_count:
  print(f'{word_tuple[0]} - {word_tuple[1]}')


