khana = ['Dal', 'Chawal', 'Roti', 'Sabzi']

for item in khana:
    print(item)

else:
    print("\nIteration of the List was successful")

for item in khana:
    if(item == 'Rotis'):
        break
else:
    print("Item not found")