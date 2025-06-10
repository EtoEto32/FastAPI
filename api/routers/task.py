"""
ルーター定義のための初期化ファイル
""" 
from fastapi import APIRouter,HTTPException
from typing import Dict,List
import api.schemas.tasks as task_schema
from api.schemas.tasks import *

router=APIRouter()

@router.get("/tasks",response_model=List[Task])
async def list_tasks():
    return [Task(id=1, title="1つ目のTODOタスク", done=False)]

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body:task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1,**task_body.dict())


@router.put("/tasks/{task_id}")
async def update_tasks():
    pass

@router.delete("/tasks/{task_id}")
async def delete_tasks():
    pass

