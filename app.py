from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("HTML_Corpus.html")     


# Default port:
if __name__ == '__main__':
    app.run(debug=True)