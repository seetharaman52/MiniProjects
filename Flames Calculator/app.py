from flask import Flask, render_template, request

app = Flask(__name__)

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
    length = len(word1 + word2)
    return length

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        word1 = request.form['word1']
        word2 = request.form['word2']
        length = ans(word1, word2)
        done = operation_RED(length)
        if done == "F":
            result = "You will be Friend for him/her"
        elif done == "L":
            result = "You will be Lover for him/her"
        elif done == "A":
            result = "You will be Affectionate for him/her"
        elif done == "M":
            result = "You will Marry him/her"
        elif done == "E":
            result = "You will be Enemy for him/her"
        elif done == "S":
            result = "You will be Sister/brother for him/her"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
