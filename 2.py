adress=input('please enter your mail adress')
while '@' and '.' not in adress:
    if '@' not in adress:
        adress=input('please rewrite your mail adress with an @ sign')
    elif '.' not in adress:
        adress=input('please rewrite your mail adress with a dot(.)')

if '@' and '.' in adress:
    print('your email adress is correct')
