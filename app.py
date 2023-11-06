from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        query=request.form.get("qery")
        print(query)
        return redirect("https://www.youtube.com/results?search_query=" + '+'.join(query.split(' ')))
    return render_template("search_bar.html")
