from flask import render_template, escape
from app import app
from app.models import Game, Node

@app.route('/')
def index():
	games = Game.query.all()
	return render_template('index.html', title='owl_cave', games=games)
	
@app.route('/<game_id>')
def game(game_id):
	game = Game.query.filter_by(name=escape(game_id)).first()
	return render_template('game.html', game=game)