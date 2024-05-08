from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'  # SQLite database file
db = SQLAlchemy(app)
api = Api(app)

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Todo(task='{self.task}', summary='{self.summary}')"



class ToDoList(Resource):
    def get(self):
        todos = TodoModel.query.all()
        result = {}
        for todo in todos:
            result[todo.id] = {"task": todo.task, "summary": todo.summary}
        return result

class ToDo(Resource):
    def get(self, todo_id):
        todo = TodoModel.query.get(todo_id)
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        return {"task": todo.task, "summary": todo.summary}

    def post(self, todo_id):
        args = request.get_json()
        if 'task' not in args or 'summary' not in args:
            abort(400, message="Both 'task' and 'summary' are required")
        todo = TodoModel.query.get(todo_id)
        if todo:
            abort(409, message="Task ID already taken")
        new_todo = TodoModel(id=todo_id, task=args["task"], summary=args["summary"])
        db.session.add(new_todo)
        db.session.commit()
        return {"task": new_todo.task, "summary": new_todo.summary}, 201

    def put(self, todo_id):
        args = request.get_json()
        todo = TodoModel.query.get(todo_id)
        if not todo:
            abort(404, message="Task doesn't exist, cannot update")
        if 'task' in args:
            todo.task = args["task"]
        if 'summary' in args:
            todo.summary = args["summary"]
        db.session.commit()
        return {"task": todo.task, "summary": todo.summary}

    def delete(self, todo_id):
        todo = TodoModel.query.get(todo_id)
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        db.session.delete(todo)
        db.session.commit()
        return {}, 204

api.add_resource(ToDoList, '/todos')
api.add_resource(ToDo, '/todos/<int:todo_id>')

if __name__ == '__main__':
    # Create database tables within application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
