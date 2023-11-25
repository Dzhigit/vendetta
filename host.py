from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import psycopg2


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
connection = psycopg2.connect(
    dbname='vendetta',
    user='dzhigit',
    host='localhost',
    port=5432
)

class VerificationHandler(Resource):
    def get(self):
        code = request.form['code']
        email = request.form['email']


class RegistrationHandler(Resource):
    def get(self):
        with connection.cursor() as cur:
            cur.execute(f"""SELECT * FROM tasks WHERE id={task_id}""")
            task = cur.fetchone()[0]



    def delete(self):
        pass

    def put(self, task_id):
        data = request.form['data']
        with connection.cursor() as cur:
            cur.execute(f"""SELECT * FROM tasks WHERE id={task_id}""")
            task = cur.fetchone()

            if len(task) > 0:
                cur.execute("""UPDATE tasks SET event """)



api.add_resource(TaskHandler, '/verification')


if __name__ == '__main__':
    app.run(debug=True)
