from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import socket
app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

# Модель для користувача
class User(db.Model):
    __tablename__ = 'users'  # Зміна назви таблиці
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
def get_server_ip():
    return socket.gethostbyname(socket.gethostname())

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html', server_ip=get_server_ip())


# Сторінка реєстрації
@app.route('/register', methods=['POST'])



def register():
    username = request.form.get('username')
    if username:
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return "Error: Username cannot be empty!"

if __name__ == '__main__':
    db.create_all()  # створює таблиці в базі даних
    app.run(debug=True)