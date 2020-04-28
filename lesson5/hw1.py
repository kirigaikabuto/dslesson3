st ="HeLlo My Dear Friend"
words=st.split()
# H e L l o
# H E L L O

counter=0
for word in words:
    n = len(word)
    upper_word = word.upper()
    for i in range(n):
        if upper_word[i]==word[i]:
            counter = counter+1

print(counter)