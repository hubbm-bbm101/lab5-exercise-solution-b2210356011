import random
rand_num=random.randint(-1000,1000)
user_selection=int(input('please enter a number between 1000 and -1000 '))
def is_equal(user_selection):
    while rand_num!=user_selection:
        if rand_num>=user_selection:
            user_selection=int(input('increase your number '))
        else:
            user_selection=int(input('decrease your  number '))
    if rand_num==user_selection:
        print('you have correctly found')
    
    
if rand_num==user_selection:
    print('well done!')
elif rand_num>=user_selection:
    is_equal(user_selection)
else:
    is_equal(user_selection)
