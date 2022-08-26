input_str=input("Enter a string: ")
input_str=input_str.casefold()
count={x:sum([1 for char in input_str if char == x]) for x in 'aeiou'}
dict={'a':1,'e':5,'i':9,'o':15,'u':22}
sum=sum(count[k]*dict[k] for k in count)
print(sum)
print(count)



