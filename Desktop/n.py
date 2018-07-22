from pythainlp.tokenize import word_tokenize
text='ผมรักคุณนะครับโอเคบ่พวกเราเป็นคนไทยรักภาษาไทยภาษาบ้านเกิด'
a=word_tokenize(text,engine='icu') 
b=word_tokenize(text,engine='dict') 
c=word_tokenize(text,engine='mm') 
print(a);