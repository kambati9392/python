# str1=input("Enter the list of words:::").split()
# print(set(str1))

str1=input("Enter the list of words::").split()
word_list = [word.strip() for word in str1]
print(word_list)
uniqe_words=set(word_list)
print(uniqe_words)
sorted_words_list=sorted(uniqe_words)
print(sorted_words_list)