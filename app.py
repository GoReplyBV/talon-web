from talon import quotations

from flask import Flask, Response, request

quotations.register_xpath_extensions()

app = Flask(__name__)


@app.route('/reply/extract_from_html', methods=['POST'])
def extract_from_html():
    html = request.get_data(as_text=True)
    return quotations.extract_from_html(html)


@app.route('/health')
def health():
    return Response('OK', status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
