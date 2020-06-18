from app import app, db
from app.models import User, Post
import os

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=8888)
    #app.run