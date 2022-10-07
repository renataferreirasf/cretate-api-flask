from flask import Flask
from flask_restplus import Api, Resource
from server.instance import Server

app = Server.app
api = Server.api



books_db = {
    {'id': 0, 
    'tiltle': 'Amor nas redes'
    },
    {'id': 1, 
    'tiltle': 'Picolé de Limão'
    },

}
@api.route('/books')
class BookList(Resource):
    def get(self,):
        return books_db