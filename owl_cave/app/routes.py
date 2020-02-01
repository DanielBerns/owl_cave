from flask import render_template, escape, redirect, url_for, request
from app import app
from app.models import Game, Node
from app.forms import SelectNodeForm

@app.route('/')
def index():
	games = Game.query.all()
	return render_template('index.html', title='owl_cave', games=games)
	
@app.route('/<game_id>', methods=['GET', 'POST'])
def game(game_id):
	game = Game.query.filter_by(name=escape(game_id)).first()
	node_form = SelectNodeForm()
	n_node = game.get_head
	if request.method == "POST":
		n_node = Node.query.filter_by(trigger=escape(request.form['next_node'])).first()
	return render_template('game.html', game=game, form=node_form, current_node=n_node)
	