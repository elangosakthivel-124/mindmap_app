from flask import Flask, render_template, request
from models import db, MindMap
from nlp_engine import extract_keywords
from graph_engine import create_mindmap

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():

    image = None

    if request.method == "POST":

        topic = request.form["topic"]

        keywords = extract_keywords(topic)

        image = create_mindmap(topic, keywords)

        record = MindMap(
            topic=topic,
            keywords=",".join(keywords)
        )

        db.session.add(record)
        db.session.commit()

    maps = MindMap.query.all()

    return render_template("index.html", image=image, maps=maps)

if __name__ == "__main__":
    app.run(debug=True)
