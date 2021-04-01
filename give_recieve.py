input_text = input("Give me some text. ")
input_word = input("Give me a word and I will tell you how many times it appears in the text! ")

def word_counter(x, y):
  word = 0
  x_list = x.split()
  word = x_list.count(y)
  return word

print(word_counter(input_text, input_word))

