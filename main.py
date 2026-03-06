from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    completed: bool = False

app = FastAPI()

todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "todo": todo}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id >= len(todos) or todo_id < 0:
        return {"error": "Todo not found"}
    deleted = todos.pop(todo_id)
    return {"message": "Deleted", "todo": deleted}