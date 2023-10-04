from flask import Flask, request, jsonify, render_template
from brain import brain
from flask_cors import CORS

app = Flask(__name__, template_folder='template')
CORS(app)

@app.route('/')
def index():
    return render_template(r'index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    # print(request.form)
    # input_text = request.form['message']
    try:
        data = request.get_json()
        input_text = data.get('message', '')

        if not input_text:
            return jsonify({'error': 'No text provided'}), 400

        # Pass the input text through the "brain" function
        processed_text = brain(input_text)

        response_data = {'processed_text': processed_text}
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Add logic to unpickle model
    app.run(debug=True, port=5000)