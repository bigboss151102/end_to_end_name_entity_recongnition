from pydoc import doc
from flask import Flask, render_template, request
from utils import *
import predictions as pd
import numpy as np
app = Flask(__name__)
app.secret_key = 'NER_PROJECT'

document_scan = DocumentScanner()


@app.route('/', methods=['GET', 'POST'])
def scanner():
    if request.method == 'POST':
        fileObj = request.files['image_name']
        upload_image_path = save_upload_image(fileObj)
        print(upload_image_path)
        # predict the coordination of the document
        four_points, size = document_scan.document_scanner(upload_image_path)
        print(four_points)
        print(size)
        if four_points is None:
            message = "Point displayed are random"
            points = [
                {'x': 10, 'y': 10},
                {'x': 120, 'y': 10},
                {'x': 120, 'y': 120},
                {'x': 10, 'y': 120},
            ]
            return render_template('scanner.html', fileupload=True, message=message, points=points)
        else:
            points = array_to_json_format(four_points)
            message = 'Located the Coordinates is authenticate'
            return render_template('scanner.html', fileupload=True, message=message, points=points)
    return render_template('scanner.html')


@app.route('/transform', methods=['POST'])
def transform():
    try:
        points = request.json['data']
        array = np.array(points)
        magic_color = document_scan.caculate_to_original_size(array)
        filename = 'magic_color.jpg'
        magic_color_path = settings.join_path(settings.MEDIA_DIR, filename)
        cv2.imwrite(magic_color_path, magic_color)
        return 'success'

    except:
        return 'fail'


@app.route('/prediction')
def prediction():
    wrap_image_filepath = settings.join_path(
        settings.MEDIA_DIR, 'magic_color.jpg')
    image = cv2.imread(wrap_image_filepath)
    image_bb, results = pd.getPredictions(image)
    bb_filename = settings.join_path(settings.MEDIA_DIR, 'bounding_box.jpg')
    cv2.imwrite(bb_filename, image_bb)
    return render_template('predictions.html', results=results)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
