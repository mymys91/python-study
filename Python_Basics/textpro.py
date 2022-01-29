from cmath import phase


def sentence_maker(phrase):
    interrogative = ('how', 'what', 'why')
    phrase = phrase.capitalize()
    if phrase.lower().startswith(interrogative):
        return '{}?'.format(phrase)
    else:
        return phrase + '.'

#print(sentence_maker('how are you'))
#print(sentence_maker('i am fine'))

results = []
while True:
    user_input = input('Say something: ')
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

#for item in results:
#   print(item)    

print("\n".join(results))