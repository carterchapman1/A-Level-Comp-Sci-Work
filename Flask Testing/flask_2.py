from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/whoareyou')
def get_name():     
    return render_template('hello_submit_form.html')

@app.route('/greet', methods = ['POST'])
def greet(name=''):
    typed_name = request.form['name']
    return render_template('hello.html', name=typed_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
