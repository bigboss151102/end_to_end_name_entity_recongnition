from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'NER_PROJECT'


@app.route('/')
def scanner():
    return render_template('scanner.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
