import json
from flask import request
from app.create_app import db, app
from app.models import User

@app.route("/users", methods=['GET', 'POST'])
def work_user():
    if request.method == 'GET':
        result = []

        for user in db.session.query(User).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            mimetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json
        db.session.add(
            User(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            mimetype="application/json",
            status=200
        )


if __name__ == '__main__':
    app.run("localhost", port=8080)
