from flask import Flask, render_template, request
from main import XMLValidator

app = Flask(__name__, template_folder='.')

validator = XMLValidator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform():
    xml_file = request.files['xmlFile']
    xslt_file = request.files['xsltFile']

    xml_file.save('document.xml')
    xslt_file.save('validator.xml')

    result = validator.process(document_path='document.xml', validations_document_path='validator.xml')

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
