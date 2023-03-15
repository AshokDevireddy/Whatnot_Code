from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return 'No file uploaded', 400
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        # do some data processing here
        output = df.to_html()
        return output
    else:
        return 'Invalid file format', 400

if __name__ == '__main__':
    app.run(debug=True)
