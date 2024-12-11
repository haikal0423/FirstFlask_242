from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Parsing parameter dari form
        input_data = request.form.get('input_data')
        result = f'Hasil input: {input_data}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
