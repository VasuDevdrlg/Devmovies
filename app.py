from flask import Flask, render_template, request
import requests


def movieinfo(mvtitle):
    api = "a08e67c4"

    url = f"http://www.omdbapi.com/?t={mvtitle}/&apikey={api}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            details = dict(response.json())
            name = details["Title"]
            dir = details["Director"]
            rel = details["Released"]
            gen = details["Genre"]
            rate = details["Ratings"]
            box = details["BoxOffice"]
            pos = details["Poster"]
            plot = details["Plot"]
            cast=details["Actors"]
            det = {"Title": name, "Plot": plot, "Director": dir, "Release_Year": rel, "Genre": gen, "Rating": rate,
                   "Box_Office": box, "Poster": pos,"Cast":cast}
            return det
        except:
            print("movie not found")


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')
@app.route('/base')
def homme():
    return render_template('base.html')



@app.route('/results', methods=["POST", "GET"])
def results():
    name = ''
    m = {}
    if request.method == "POST":
        name = request.form["srch"]
        m = movieinfo(name)
    return render_template("results.html", k=m)


if __name__ == '__main__':
    app.run(debug=True)
