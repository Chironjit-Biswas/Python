import random 
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbole="(){}[]@!&^$#"

result=lower_case+upper_case+number+symbole

length=9
password="".join(random.sample(result, length))
print(password)