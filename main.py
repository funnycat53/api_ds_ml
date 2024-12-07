
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()
    atbilde = requests.get("https://api.chucknorris.io/jokes/categories")
    kategorijas = atbilde.json()
    if request.method == "POST" :
        kategorija = request.form.get("kat")
        atbilde = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorija}")
        joks = atbilde.json()

    return render_template("index.html", joks = joks["value"], bilde = joks["icon_url"], kategorijas = kategorijas)

@app.route("/izvelies_tekstu", methods=["POST", "GET"])
def teksta_izvele():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joki = atbilde.json()
    
    if request.method == "POST":
        search_text = request.form.get("izvelies_tekstu")
        if search_text:  
            atbilde = requests.get(f"https://api.chucknorris.io/jokes/search?query={search_text}")
            joki = atbilde.json()
            pirmais = joki["result"][0]["value"]

        return pirmais

    return render_template("izvelies_tekstu.html", joki=joki.get("value", "No joke found"), bilde=joki.get("icon_url", ""))

@app.route("/uni")
def uni():
    atbilde = requests.get("http://universities.hipolabs.com/search?country=latvia")
    visas = atbilde.json()
    print(visas[3]["web_pages"][0])
    nosaukumi = []
    for elements in visas:
        pieliekamais = {
            "nosaukums" : elements["name"],
            "majaslapas" : elements["web_pages"]
        }
        nosaukumi.append(pieliekamais)

    return render_template("universitates.html", uni=nosaukumi)

banned_lietotaji = []

@app.route("/jschats")
def chats():
    return render_template("chats.html")

@app.route("/jschats/suutiit", methods = ["POST"])
def suutiit():
    sanemtais = request.json
    lietotajs = sanemtais["vards"]
    saturs = sanemtais["saturs"]

    if lietotajs in banned_lietotaji:
        return jsonify("Jums ir aizliegts sūtīt ziņas"), 403

    if saturs.startswith("/ban "):
        banned_lietotajs = saturs.split(" ", 1)[1].strip()
        if banned_lietotajs not in banned_lietotaji:
            banned_lietotaji.append(banned_lietotajs)
        return jsonify(f"Lietotājam {banned_lietotajs} ir aizliegts sūtīt ziņas")

    if sanemtais["saturs"] == "/clear":
        with open("chataZinas.txt", "w") as f:
            f.write("")
        return "Izdzēsts"

    with open("chataZinas.txt", "a") as f:
        f.write(sanemtais["vards"])
        f.write("----")
        f.write(sanemtais["saturs"])
        f.write('\n')
    return jsonify("OK")

@app.route("/jschats/lasiit")
def lasit():
    saturs = []
    with open("chataZinas.txt", "r") as f:
        saturs = f.readlines()
    return jsonify(saturs)



if __name__ == '__main__':
    app.run(debug=True, port = 5000)
