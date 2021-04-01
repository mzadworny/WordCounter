import operator

words = '''
The Kombucha mushroom people
Sitting around all day
Who can believe you
Who can believe you
'''
words = words.replace(',', '')
words = words.lower()

word_list = words.split()
word_count = {}

for word in word_list:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_count)


