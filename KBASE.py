from flask import Flask, jsonify, Response, send_file, render_template, request, flash
import os, create_genome
app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        return render_template('welcome.html')
    else:
        data = request.form["textarea1"]
        here = os.path.dirname(__file__)
        fo = open(here + "/temp_rest_input.txt", "w+")
        fo.write(data)
        fo.close()
        create_genome.genome(here)
        return send_file(here + '/temp_output3.txt')

if __name__ == '__main__':
    app.run()
