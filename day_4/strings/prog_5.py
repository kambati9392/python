str1=input("Enter the list of words").split()
print(str1)
long_word=""
#len(long_word)=0
for word in str1:
    print(word,len(word))
    #long_word=word
    if len(word)>len(long_word):
        long_word=word
print(long_word)


# def longest_word_length(word_list):
#     # Find the longest word using the max() function with key as len
#     longest_word = max(word_list, key=len)
    
#     # Return the length of the longest word
#     return len(longest_word)
    
