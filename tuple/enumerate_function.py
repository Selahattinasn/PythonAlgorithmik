# enumerate function returns a tuple with to elements,
# first the index of the element, second the element self. 

winners=["Ali", "Veli","Hamza"]
for index,person in enumerate(winners):
    print("{} - {}".format(index+1,person) )