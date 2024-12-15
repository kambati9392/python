
data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}
]
success_count = 0
for item in data:
    if item.get('success') == True:
        success_count += 1

print("Count of how many dictionaries have success as True:", success_count)
