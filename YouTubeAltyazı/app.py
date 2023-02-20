from flask import Flask, render_template, request, redirect, url_for
from main import SubTitle

app = Flask(__name__, static_folder="static")

def formatter(lst):
    lyrics = []
    current_lyric = ""

    for item in lst:
        if item != "":
            current_lyric += item + " "
        else:
            lyrics.append(current_lyric.strip())
            current_lyric = ""
            
    return lyrics
            
            
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/url", methods=["GET","POST"])
def url():
    
    if request.method == "POST":
        __url = request.form.get("url")
        try:
            urlId = str(__url).split("=")[1]
        except IndexError:
            return redirect(url_for("index"))
        
        sub = SubTitle(urlId)
        content = str(sub).split("\n")
        lyr = formatter(lst=content)
        with open(f"{urlId}.txt", mode="w", encoding="utf-8") as file:
            for i in lyr:
                file.write(str(i)+"\n")
                

        return render_template("index.html",status=True, Id=urlId)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)