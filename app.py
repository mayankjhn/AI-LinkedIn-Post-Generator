from flask import Flask, render_template, request
from generate_post.py import generate_linkedin_post
from scraper.py import get_trending_topics

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    trending_topics = get_trending_topics()
    generated_post = None
    
    if request.method == "POST":
        topic = request.form["topic"]
        generated_post = generate_linkedin_post(topic)

    return render_template("index.html", topics=trending_topics, generated_post=generated_post)

if __name__ == "__main__":
    app.run(debug=True)
