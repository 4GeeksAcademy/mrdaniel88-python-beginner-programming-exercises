# Your code here!!
def sing() :
    let_it_be = ""
    for i in range (1,13):
        if (i == 5):
           let_it_be += "whisper words of wisdom, "
        elif (i == 11):
            let_it_be += "there will be an answer, "
        elif (i==12):
            let_it_be += "let it be"
        else:
            let_it_be += "let it be, "
    return let_it_be

print(sing())