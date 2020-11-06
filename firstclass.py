# Comment
input_text = input("Enter some text: ")

print("You inputted: \n" + input_text)
char_count = 0
word_count = 1
for ch in input_text:
    if(ch == ' '):
        word_count += 1
    else:
        char_count += 1


print("No of Characters = " + str(char_count))
print("No of Words = " + str(word_count))
