from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='/app/messages.log', level=logging.DEBUG)

@app.route('/')
def index():
    print("Received GET request")

    if request.method == 'GET':
        logging.info(f"Successful GET request: {request.url}")

    return "Successful GET request!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
