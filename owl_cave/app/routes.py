from flask import render_template
from app import app
from app.models import Game, GameNode

@app.route('/')
def index():
	return render_template('index.html', title='owl_cave')
	
@app.route('/<game_id>')
def game(game_id):
	game = Game
	return render_template('game_html')