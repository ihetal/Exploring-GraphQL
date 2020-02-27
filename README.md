# Lab 3

## Pre-requisites

* Install _Pipenv_

```
pip install pipenv
```

* Install _[Flask](https://palletsprojects.com/p/flask/)_

```
pipenv install flask==1.1.1
```
* Install _[Ariadne](https://ariadnegraphql.org/docs/flask-integration.html)_ for handling GraphQL schema and binding.

```
pipenv install ariadne==0.10.0
```



* Run your Hello World Flask application from a shell/terminal.

```sh
pipenv shell
$ env FLASK_APP=app.py flask run
```

* Open [this URL](http://127.0.0.1:5000/) in a web browser or run this CLI to see the output.

```
curl -i http://127.0.0.1:5000/
```


### Domain Model

```
|-------|               |---------|
| Class |* ---------- * | Student |
|-------|               |---------|
```

### GraphQL operations implemented.

* Mutate a new student

_Request_
```
mutation {
	addStudent(name: "Bob Smith") {
    name
    id
  }
}
```

_Response_
```
{
  "data": {
    "addStudent": {
      "id": "1",
      "name": "Bob Smith"
    }
  }
}

```
* Query an existing student

_Request_

```
{
  students(id:1) {
    name
  }
}
```

_Response_

```
{
  "data": {
    "students": {
      "name": "Bob Smith"
    }
  }
}
```

* Mutate a class

_Request_
```
mutation{
  addClass(name:"CMPE-273"){
    id
    name
    students{
      id
      name
    }
  }
}
```

_Response_

```
{
  "data": {
    "addClass": {
      "id": "1",
      "name": "CMPE-273",
      "students": []
    }
  }
}
```

* Query a class

_Request_
```
{
  classes(id:1) {
    name
    students{
      id
      name
    }
  }
}
```

_Response_

```
{
  "data": {
    "classes": {
      "name": "CMPE-273",
      "students": []
    }
  }
}

```

* Add students to a class

_Request_
```
  mutation  {
    addStudentToClass(studentId: 1, classId: 1) {
      id
      name
      students{
        name
        id
      }
    }
  }
```

_Response_

```
{
  "data": {
    "addStudentToClass": {
      "id": "1",
      "name": "CMPE-273",
      "students": [
        {
          "id": "1",
          "name": "Bob Smith"
        }
      ]
    }
  }
}
```



