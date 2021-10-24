from flask import Flask, render_template, request
import getKey

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
	return render_template('index.html')

@app.route('/get', methods=['POST'])
def post():
	content = request.form['content']
	text,words,address=getKey.getKeys(content)
	means=getKey.pushMean(words)
	return render_template('got.html',text=text,address=address,words=words,means=means)

if __name__ == '__main__':
	app.run(debug=True)