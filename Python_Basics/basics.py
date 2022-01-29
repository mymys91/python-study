from email import message


day_hours = 24
week_days = 7

week_hours = day_hours * week_days
print(week_hours)

def mean(my_list):
    if type(my_list) == dict:
        the_mean = sum(my_list.values()) / len(my_list)
    else:
        the_mean=sum(my_list)/len(my_list)
    return the_mean

print(mean([1,2,3]))
print(type(mean), type(sum))
print(mean({"A":34,"B":3}))

#print('Hi ' + input("Enter your name:"))

#user_input = input("Enter yourname again: ")
#message = "Hello %s, %s" % (user_input,user_input) 
#message = f"Hello {user_input}"
#print(message)

monday_temperature = [9.9,8.7,3.4]
for temperature in monday_temperature:
    print(round(temperature))
    print('Done')

for letter in 'Hello':
    print(letter)

colors = ['aa', 11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)