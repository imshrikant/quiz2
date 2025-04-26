from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Employee
from data_generator import generate_employee_data

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P%40sw00rd@localhost:5432/employees'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)

class EmployeeList(Resource):
    def get(self):
        employees = Employee.query.all()
        return jsonify([{
            'id': emp.id,
            'name': emp.name,
            'age': emp.age,
            'department': emp.department,
            'salary': emp.salary
        } for emp in employees])

api.add_resource(EmployeeList, '/employees')

@app.before_request
def create_tables():
    # The following line will remove this handler, making it
    # only run on the first request
    app.before_request_funcs[None].remove(create_tables)

    db.create_all()
    generate_employee_data(100)  # Generate 100 records on first run
    # push context manually to app
 

if __name__ == '__main__':
    app.run(debug=True)