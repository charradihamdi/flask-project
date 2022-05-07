from http import client
from multiprocessing.connection import Client
from flask import current_app,jsonify,request
from app import create_app,db
from models import Articles,articles_schema,article_schema

# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles

@app.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

	articles = Articles.query.all()
	results = articles_schema.dump(articles)

	return jsonify(results)


@app.route("/add", methods=["POST"], strict_slashes=False)
def add_client():
	title = request.json['title']
	body = request.json['body']

	client = Client(
		title=title,
		body=body
		)

	db.session.add(article)
	db.session.commit()

	return article_schema.jsonify(article)



if __name__ == "__main__":
    app.run(port=4000, debug=True)