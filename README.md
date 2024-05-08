GET all todos:
  Method: GET
  URL: http://127.0.0.1:5000/todos
  
GET a specific todo by ID:
  Method: GET
  URL: http://127.0.0.1:5000/todos/<todo_id>
  Replace <todo_id> with the ID of the todo you want to retrieve.
  
Create a new todo:
  Method: POST
  URL: http://127.0.0.1:5000/todos/<todo_id>
  Replace <todo_id> with a unique ID for the new todo.
  Body (JSON):
    json
      Copy code
        {
            "task": "Your task here",
            "summary": "Your summary here"
        }

        
Update an existing todo:
  Method: PUT
  URL: http://127.0.0.1:5000/todos/<todo_id>
  Replace <todo_id> with the ID of the todo you want to update.
    Body (JSON):
      json
      Copy code
        {
            "task": "Updated task",
            "summary": "Updated summary"
        }
        
Delete a todo:
  Method: DELETE
  URL: http://127.0.0.1:5000/todos/<todo_id>
  Replace <todo_id> with the ID of the todo you want to delete.
