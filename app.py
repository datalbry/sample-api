from typing import List, Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Person(BaseModel):
    id: str
    name: str


class Computer(BaseModel):
    id: str
    personId: str
    model: str


class ProjectInformation(BaseModel):
    numberCommits: int
    numberCollaborators: int
    hostingPlatform: str


class Project(BaseModel):
    id: str
    personId: str
    projectName: str
    projectInformation: ProjectInformation


class OfficePet(BaseModel):
    id: str
    name: str
    type: str


class PetToy(BaseModel):
    id: str
    petId: str
    description: str


persons = [
    Person(id="first", name="Max Musterman"),
    Person(id="second", name="John Doe"),
]

computers = [
    Computer(id="aaaa", personId="first", model="Notebook 2010"),
    Computer(id="aaab", personId="first", model="Notebook 2014"),
    Computer(id="aaac", personId="first", model="Notebook 2020"),
    Computer(id="bbbc", personId="second", model="Desktop 2021"),
]

projects = [
    Project(
        id="ca",
        personId="first",
        projectName="Super Duper Project",
        projectInformation=ProjectInformation(
            numberCommits=10, numberCollaborators=1, hostingPlatform="github"
        ),
    ),
    Project(
        id="cb",
        personId="first",
        projectName="ML Project",
        projectInformation=ProjectInformation(
            numberCommits=3, numberCollaborators=1, hostingPlatform="gitlab"
        ),
    ),
    Project(
        id="cc",
        personId="first",
        projectName="Connector Project",
        projectInformation=ProjectInformation(
            numberCommits=100, numberCollaborators=3, hostingPlatform="github"
        ),
    ),
    Project(
        id="cd",
        personId="second",
        projectName="Fancy Project",
        projectInformation=ProjectInformation(
            numberCommits=10, numberCollaborators=2, hostingPlatform="github"
        ),
    ),
]

office_pets = [
    OfficePet(id="p1", name="Broccoli", type="dog"),
    OfficePet(id="p2", name="Fury", type="dog"),
    OfficePet(id="p3", name="Donner", type="dog"),
]

pet_toys = [
    PetToy(id="10", petId="p1", description="Ball"),
    PetToy(id="11", petId="p1", description="Frisbee (green)"),
    PetToy(id="20", petId="p2", description="Frisbee (green)"),
    PetToy(id="30", petId="p3", description="Frisbee (red)"),
    PetToy(id="31", petId="p3", description="Plush Teddy"),
]

app = FastAPI()


@app.get("/api/v1/persons", response_model=List[Person])
def read_person():
    return persons


@app.get("/api/v1/person/{person_id}", response_model=Optional[Person])
def read_person_by_id(person_id: str):
    for p in persons:
        if p.id == person_id:
            return p

    return JSONResponse(status_code=404, content={"message": "Not Found"})


@app.get("/api/v1/person/{person_id}/computers", response_model=List[Computer])
def read_computers(person_id: str):
    return [c for c in computers if c.personId == person_id]


@app.get(
    "/api/v1/person/{person_id}/computer/{computer_id}",
    response_model=Optional[Computer],
)
def read_computer_by_id(person_id: str, computer_id: str):
    for c in computers:
        if (c.personId == person_id) and (c.id == computer_id):
            return c

    return JSONResponse(status_code=404, content={"message": "Not Found"})


@app.get("/api/v1/person/{person_id}/projects", response_model=List[Project])
def read_projects_by_id_of_person(person_id: str):
    return [p for p in projects if p.personId == person_id]


@app.get("/api/v1/officePets", response_model=List[OfficePet])
def read_office_pets():
    return office_pets


@app.get("/api/v1/officePet/{pet_id}/petToys", response_model=List[PetToy])
def read_pet_toys_by_id_of_office_pet(pet_id: str):
    return [pt for pt in pet_toys if pt.petId == pet_id]


@app.get("/api/v1/officePet/{pet_id}/petToy/{toy_id}", response_model=Optional[PetToy])
def read_pet_toy_by_id(pet_id: str, toy_id: str):
    for pt in pet_toys:
        if (pt.petId == pet_id) and (pt.id == toy_id):
            return pt

    return JSONResponse(status_code=404, content={"message": "Not Found"})
