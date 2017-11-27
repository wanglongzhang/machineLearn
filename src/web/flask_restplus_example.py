#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)

@app.route('/foo/<int:id>')
def index(id):
    print("id", id, "heelo", request.url_rule)
    return request.base_url

api = Api(app, version="1.0", title="configuration API",
          description="",
)

ns = api.namespace("todos", description="TODO operations")

todo = api.model("Todo", {
    "id": fields.Integer(readOnly=True, description="The task unique identifier"),
    "task": fields.String(required=True, description="The task details")
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo["id"] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo["id"] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({"task": "Build an API"})
DAO.create({"task": "?????"})
DAO.create({"task": "profit!"})

def api_key_required(permission, type="permission"):
    def deco(func):
        def func_wrapper(*args, **kwargs):
            api_key = request.headers.get("Authentication")
            if api_key != permission:
                return api.abort(403)
            return func(*args, **kwargs)
        return func_wrapper
    return deco


@ns.route("/")
@api.header("Authentication", "authentication header", required=True)
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""
    @ns.doc("list_todos")
    @api_key_required("todolist:get")
    def get(self):
        """List all tasks"""
        return DAO.todos

    @ns.doc("create_todo")
    @ns.expect(todo)
    @api_key_required("todolist:create")
    def post(self):
        """Create a new task"""
        return DAO.create(api.payload), 201


@ns.route("/<int:id>")
@ns.response(404, "Todo not found")
@ns.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class Todo(Resource):
    """Show a single todo item and lets you delete them"""
    @ns.doc("get_todo")
    def get(self, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @ns.doc("delete_todo")
    @ns.response(204, "Todo deleted")
    def delete(self, id):
        """Delete a task given its identifier"""
        DAO.delete(id)
        return "", 204

    @ns.expect(todo)
    def put(self, id):
        """Update a task given its identifier"""
        return DAO.update(id, api.payload)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)