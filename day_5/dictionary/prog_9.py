# # Sample dictionary
my_dict = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}

# Print header
print(f"{'Key':<10}{'Value'}")
print("-" * 20)

# Print the dictionary in table format
for key, value in my_dict.items():
    print(f"{key:<10}{value}")
