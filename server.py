from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__, static_url_path='')
app.secret_key = 'why would I tell you my secret key?'
api = Api(app)
tasks = {}


@app.route('/')
def root():
    return app.send_static_file('index.html')


class Task(Resource):
    @staticmethod
    def get(task_id):
        return {task_id: tasks[task_id]}

    @staticmethod
    def put(task_id):
        tasks[task_id] = request.form['data']
        return {task_id: tasks[task_id]}


api.add_resource(Task, '/<string:task_id>')

if __name__ == '__main__':
    app.run(debug=True)