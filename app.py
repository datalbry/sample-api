from typing import List, Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ObjectA(BaseModel):
    id: str
    value: str


class ObjectB(BaseModel):
    id: str
    aId: str
    value: str


class ObjectC(BaseModel):
    id: str
    aId: str
    value: str
    anotherValue: str


class ObjectX(BaseModel):
    id: str
    value: str


class ObjectY(BaseModel):
    id: str
    xId: str
    value: str


objects_a = [
    ObjectA(id="first", value="first_value"),
    ObjectA(id="second", value="second_value")
]

objects_b = [
    ObjectB(id="aa", aId="first", value="a"),
    ObjectB(id="ab", aId="first", value="b"),
    ObjectB(id="ac", aId="first", value="b"),
    ObjectB(id="bc", aId="second", value="foobar_second"),
]

objects_c = [
    ObjectC(id="ca", aId="first", value="a", anotherValue="another_a"),
    ObjectC(id="cb", aId="first", value="b", anotherValue="another_b"),
    ObjectC(id="cc", aId="first", value="b", anotherValue="foobar"),
    ObjectC(id="cd", aId="second", value="c", anotherValue="test"),
]

objects_x = [
    ObjectX(id="x1", value="first_x"),
    ObjectX(id="x2", value="second_x"),
    ObjectX(id="x3", value="third_x"),
]

objects_y = [
    ObjectY(id="1", xId="x1", value="hello"),
    ObjectY(id="2", xId="x2", value="world"),
    ObjectY(id="3", xId="x2", value="asdf"),
    ObjectY(id="4", xId="x3", value="foo"),
    ObjectY(id="5", xId="x3", value="bar"),
    ObjectY(id="6", xId="x3", value="test"),
]

app = FastAPI()


@app.get("/api/v1/objectAs", response_model=List[ObjectA])
def read_objects_a():
    return objects_a


@app.get("/api/v1/objectA/{a_id}", response_model=Optional[ObjectA])
def read_object_a_by_id(a_id: str):
    for obj_a in objects_a:
        if obj_a.id == a_id:
            return obj_a

    return JSONResponse(status_code=404, content={"message": "Not Found"})


@app.get("/api/v1/objectA/{a_id}/objectBs", response_model=List[ObjectB])
def read_objects_bs(a_id: str):
    return [obj_b for obj_b in objects_b if obj_b.aId == a_id]


@app.get("/api/v1/objectA/{a_id}/objectB/{b_id}", response_model=Optional[ObjectB])
def read_object_b_by_id_of_a(a_id: str, b_id: str):
    for obj_b in objects_b:
        if (obj_b.aId == a_id) and (obj_b.id == b_id):
            return obj_b

    return JSONResponse(status_code=404, content={"message": "Not Found"})


@app.get("/api/v1/objectA/{a_id}/objectCs", response_model=List[ObjectC])
def read_object_c_by_id_of_a(a_id: str):
    return [obj_c for obj_c in objects_c if obj_c.aId == a_id]


@app.get("/api/v1/objectXs", response_model=List[ObjectX])
def read_objects_x():
    return objects_x


@app.get("/api/v1/objectX/{x_id}/objectYs", response_model=List[ObjectY])
def read_objects_y_by_id_of_ax(x_id: str):
    return [obj_y for obj_y in objects_y if obj_y.xId == x_id]


@app.get("/api/v1/objectX/{x_id}/objectY/{y_id}", response_model=Optional[ObjectY])
def read_object_b_by_id_of_a(x_id: str, y_id: str):
    for obj_y in objects_y:
        if (obj_y.xId == x_id) and (obj_y.id == y_id):
            return obj_y

    return JSONResponse(status_code=404, content={"message": "Not Found"})
