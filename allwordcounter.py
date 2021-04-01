import operator

words = '''
The Kombucha mushroom people
Sitting around all day
Who can believe you
Who can believe you
Let your mother pray (sugar)
I'm not there all the time you know
Some people, some people, some people
Call it insane, yeah they call it insane (sugar)
I play Russian roulette everyday, a man's sport
With a bullet called life, yeah, mama, called life(sugar)
You know that every time I try to go
Where I really want to be
It's already where I am
'Cause I'm already there
The Kombucha mushroom people
Sitting around all day
Who can believe you
Who can believe you
Let your mother pray (sugar)
I got a gun the other day from Sako
It's cute, small, fits right in my pocket
Yeah, right in my pocket, (sugar)
My girl, you know, she lashes out at me sometimes
And I just fucking kick her
'''

word_list = words.split()
word_count = {}

for word in word_list:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_count)


