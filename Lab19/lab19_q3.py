#(i)(a)
a=[i for i in range(1,51)]
string_a=",".join([str(i) for i in a])
print(string_a)
#(b)
string_b=".".join([str(i) for i in a])
print(string_b)
#(c)
string_c="-".join([str(i) for i in a])
print(string_c)
#(d)
string_d="\n".join([f"{i} {i**2}" for i in a])
print(string_d)

#(ii)
name=["kaumudi mishra","sanjna pillai","mahima shukla","tanishq kokate","manekha verma","mahaprasad nayak","kanishka tyagi","jyoti dubey","shalini kumari","anshika goyal"]
#(a)
upper_case=[i.upper() for i in name]
print(upper_case)
#(b)
swap_name=[" ".join(i.split()[::-1]) for i in name]
print(swap_name)
#(c)
FL=[".".join([(i.title()).split()[0],(i.title()).split()[1]]) for i in name]
print(FL)

#(iii)
s="She sells sea shells that she collects from the sea floor"
longestword=[max([word for word in s.split()], key=len)]
print(longestword)

#(iv)
lower_case=[word.lower() for word in s.split()]
repeated_words=list(set([i for i in lower_case if lower_case.count(i)>1]))
print(repeated_words)

