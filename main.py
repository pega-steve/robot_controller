from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from fastapi import FastAPI

app = FastAPI(title="Task API",
                servers=[
                {"url": "https://robot-controller.onrender.com", "description": "test environment"}]
                )


class Point(BaseModel):
    x: float
    y: float

class Points(BaseModel):
    points: List[Point]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/")
async def status():
    return {"result": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/move_to_dispense_glue", summary="glue dispensing task", description="This endpoint allows you to control robot movement and glue dispensing")
async def move_to_dispense_glue(points: Points, enable_dispenser: bool = False, continue_dispensing: bool = False):
    """
    Points: The robot and glue dispenser will move sequentially along the points defined in the list.
    enable_dispenser: Determines whether to activate the glue dispenser. When the robot only needs to move, this can be set to false to deactivate the dispenser.
    continue_ Dispensing: Whether to continuously dispense glue or only dispense glue at intermediate points.
    """
    print("Move waypoints:", enable_dispenser, continue_dispensing)
    for p in points.points:
        print(p)
    return {"result": "done", "task": points, "continue_dispensing": continue_dispensing}
