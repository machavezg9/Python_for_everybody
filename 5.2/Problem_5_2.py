largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        n= int(num)
        largest = num if largest<num or largest == None else largest
        smallest = num if smallest>num or smallest == None else smallest
    except:
        print ("Invalid input")
    

print("Maximum", largest)
print ("Minimum", smallest)
