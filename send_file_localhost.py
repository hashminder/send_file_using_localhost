from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def download():
    return send_file('filename.txt', as_attachment=True)
# replace < filename > with your real file
# if your file is not in the same directory as this script than give the full address

if __name__ == '__main__':
    print("Server is running address = localhost:5000")
    app.run(host='127.0.0.1', port=5000)
