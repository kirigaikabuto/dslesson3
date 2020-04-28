names=["yerassyl","name2","name3"]
phones=[12323213,433343,123213]
name = input()
n = len(names)
for i in range(n):
    if names[i] == name:
        print(phones[i])
        break