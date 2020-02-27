from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, MutationType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

s_Id = 0
c_Id = 0
students ={}
classes = {}

type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
mutation = MutationType()

@mutation.field("addStudent")
def store_student_details(_, info, name):
    global s_Id
    s_Id += 1
    students[s_Id] ={"id":s_Id,"name": name}
    return students[s_Id]

@query.field("students")
def get_Student(_, info,id):
    if id in students:
        return students[id]

@mutation.field("addClass")
def store_class_details(_, info, name):
    global c_Id
    c_Id += 1
    classes[c_Id] ={"id":c_Id,"name": name,"students":[]}
    return classes[c_Id]

@query.field("classes")
def get_Class(_, info,id):
    if id in classes:
        return classes[id]

@mutation.field("addStudentToClass")
def add_student_to_class(_, info, studentId,classId):
    if classId in classes:
        if studentId in students:
            classes[classId]["students"].append(students[studentId])
        return classes[classId]

schema = make_executable_schema(type_defs,query,mutation)

app = Flask(__name__)


@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200
    
@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug = True)