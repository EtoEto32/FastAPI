"""
ルーター定義のための初期化ファイル
""" 
from fastapi import APIRouter,HTTPException
from typing import Dict,List
import api.schemas.tasks as task_schema

router=APIRouter()

@router.get("/tasks",response_model=List[task_schema.Task])
async def list_tasks():
    return {"tasks": [task_schema.Task(id="1",title="1つ目のTODOタスク")]}

@router.post("/tasks")
async def create_task():
    return {"message": "Task created"}

@router.put("/tasks/{task_id}")
async def update_tasks():
    pass

@router.delete("/tasks/{task_id}")
async def delete_tasks():
    pass
