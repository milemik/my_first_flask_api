from flask import Flask, request, render_templates
import os
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def foo():
    return render_templates('home.html', 'nesto' = os.getcwd())

'''
@app.route("/answer", methods=['POST'])
def answer():
    text = request.form.get("nesto")
    return "Uneli ste {} slova".format(len(text))
'''
if __name__ == '__main__':
    app.run(debug=True)
