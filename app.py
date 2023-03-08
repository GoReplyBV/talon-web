from talon import quotations

from flask import Flask, request

app = Flask(__name__)


@app.route('/reply/extract_from_html', methods=['POST'])
def extract_from_html():
    html = request.get_data(as_text=True)
    return quotations.extract_from_html(html)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
