
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

# Print when we ran out of pastrami.
#removing all instances of pastrami orders.
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Removing all instances of pastrami orders.
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

#display the new orders without pastrami.

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")