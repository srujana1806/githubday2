a=7,'p',9
print(type(a))

# try to find out vowel from sentence

a='hello,how are you?'
str='aeiouAEIOU'

for i in a:
    if i in str:
        print(i)  


sentence='hello,how are you?'
a=[i for i in sentence if i in 'aeiouAEIOU']
a
             