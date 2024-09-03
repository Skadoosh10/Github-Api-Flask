from flask import Flask,render_template,request,flash
import requests

app = Flask(__name__)

base_url = "https://api.github.com/users/"

@app.route("/",methods =["GET","POST"])
def index():
    if request.method == "POST":
        githubname = request.form.get("githubname")
        response = requests.get(base_url + githubname)
        if response:
            user_info = response.json()
            repos_url = user_info["repos_url"]
            response_repos_url = requests.get(repos_url)
            repos_info = response_repos_url.json()
            return render_template("index.html",profile = user_info,repos = repos_info)
        else:
            flash("User not Found")
            return render_template("index.html",)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
