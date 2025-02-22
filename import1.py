import modprac
modprac.fun_name("Siva")

from modprac import add_num,sub_num,mul_num
add_num(3,2)
sub_num(8,2)
mul_num(3,4)

from modprac import add_num as an,sub_num as sn,mul_num as mn
an(3,2)
sn(8,2)
mn(3,4)

from modprac import person
print(person["name"])