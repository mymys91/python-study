temps = [221, 390, -973, 425]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

new_temps_con = [temp / 10 for temp in temps if temp > 0]
print(new_temps_con)

new_temps_con2 = [temp / 10 if temp > 0 else 0 for temp in temps]
print(new_temps_con2)

#arbitrary number of non-keyword arguments
def mean(*args):
    return sum(args)

print(mean(2,4,5,3))    

def sortStr(*args):
    new_list = [v.upper() for v in args]
    new_list.sort()
    return new_list

print(sortStr('bbb','vvv','aaaa'))  

#arbitrary number of keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=5,b=4))