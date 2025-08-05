from flask import Flask, render_template, request
from parser.extract import parse_resume
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    profile_data = None
    if request.method == 'POST':
        resume = request.files['resume']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
        resume.save(file_path)

        profile_data = parse_resume(file_path)

    return render_template("index.html", profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True)

