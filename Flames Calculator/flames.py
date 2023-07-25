def operation_RED(length):
    boom = ["F", "L", "A", "M", "E", "S"]
    i = 0
    while len(boom) != 1:
        i = (i + length - 1) % len(boom)
        boom.pop(i)
    return "".join(boom)
    
def ans(word1, word2):
    lis1 = list(word1)
    lis2 = list(word2)
    for i in word1:
        if i in word2:
            word1 = word1.replace(i,"",1)
            word2 = word2.replace(i,"",1)
    length = len(word1+word2)
    return length

if __name__ == "__main__":
    print("==========================================Welcome to FLAMES Calculator==========================================")
    word1 = input("Enter a name: ")
    word2 = input("Enter a name: ")
    done = operation_RED(ans(word1,word2))
    if done == "F":
        print("You will be Friend for him/her")
    elif done == "L":
        print("You will be Lover for him/her")
    elif done == "A":
        print("You will be Affectionate for him/her")
    elif done == "M":
        print("You will Marry him/her")
    elif done == "E":
        print("You will be Enemy for him/her")
    elif done == "S":
        print("You will be Sister/brother for him/her")

