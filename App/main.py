from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)
app.secret_key = 'NER_PROJECT'


@app.route('/', methods=['GET', 'POST'])
def scanner():
    if request.method == 'POST':
        fileObj = request.files['image_name']
        upload_image_path = save_upload_image(fileObj)
        print(upload_image_path)
        return render_template('scanner.html')
    return render_template('scanner.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
