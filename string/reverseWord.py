 # Reverse Words in a String
 # Problem Statement: Given a string s, reverse the words of the string.

def reverse_words(s):
    print('after reversing words: ')
    print(s)

    s += " "

    stack = []
    word = ""
    
    for char in s: 
        if char == ' ':
            stack.append(word)
            word = ""
        else:
             word += char


    ans = ""
    while len(stack) > 1:
        ans += stack.pop() + " "

    ans += stack.pop()
    print("after reversing words: ")
    print(ans)

s = "hello my name is sachin sharma"
reverse_words(s)    


