from app import db

class Game(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True, unique=True)
	nodes = db.relationship('Node', backref='game', lazy='dynamic')
	
	def __repr__(self):
		return '<Game {}>'.format(self.name)
		
node_rels = db.Table('nodes', \
	db.Column('parent_node_id', db.Integer, db.ForeignKey('node.id')), \
	db.Column('child_node_id', db.Integer, db.ForeignKey('node.id'))
)
	
class Node(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
	
	title = db.Column(db.String(128))
	description = db.Column(db.Text)
	trigger = db.Column(db.String(64))
	
	is_head = db.Column(db.Boolean, unique=True)
	is_tail = db.Column(db.Boolean, unique=True)
	connected_nodes = db.relationship( \
		'Node', secondary=node_rels, \
		primaryjoin=(node_rels.c.parent_node_id == id), \
		secondaryjoin=(node_rels.c.child_node_id == id), \
		backref=db.backref('node_rels', lazy='dynamic'), lazy='dynamic' \
	)
	
	def __repr__(self):
		return '<Node {}>'.format(self.text)