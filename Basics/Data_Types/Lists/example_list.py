#   A Python list uses the syntax of sqare brackets enclosing the
# elements of the list separated by commas.
#   A list can contain differing data types and even complex items 
# like other lists.

# demonstrate the variety possible in a list.
potpourri = [ 1 , 1.01 , 1+2j , 1e32 , 'a astring' , [1,2,3]]
for item in potpourri:
    print(item , '-->' , type(item))

print()
# demonstrate how to access the list via its offset
# offsets start at 0 (zero).
for i in range(len(potpourri)):
    print("Offset =" , i , "-->" , potpourri[i])