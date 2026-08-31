from flask import Flask,render_template,request,send_file

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods=['POST'])
def upload():

    files = request.files.getlist("File[]")

    from file import pdfconvert

    a = pdfconvert(files)
    a.imgtopdf()

    return send_file('image.pdf',as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)