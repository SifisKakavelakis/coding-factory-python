# set -> {}

bag = {"eggs", "apples", "milk", "bananas"}
print(f"Initial bag: {bag}")

bag.add("oranges")
bag.add("oranges")
bag.add("oranges")
print(f"Bag after adding oranges: {bag}")

print()
# iterate with enhanced for
for item in bag:
    print(item, end=', ')
print()

# remove from sets
item_to_remove = "eggs"
bag.remove(item_to_remove)
print(f"Bag after removing {item_to_remove}: {bag}")

