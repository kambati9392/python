def display_formatted_text(text, width=90):
    # Use f-string formatting to adjust the text width
    print(f"{text:^{width}}")  # Center the text, width 50 characters

# Example usage
text = "Welcome to Python Programming!"
display_formatted_text(text)

# def display_left_aligned(text, width=50):
#     print(text.ljust(width))

# text = "Welcome to Python Programming!"
# display_left_aligned(text)

# def display_right_aligned(text, width=50):
#     print(text.rjust(width))

# text = "Welcome to Python Programming!"
# display_right_aligned(text)

