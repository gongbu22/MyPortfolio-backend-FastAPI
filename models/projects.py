from typing import List
from beanie import Document
from bson import ObjectId

class myportfolio(Document):
    # _id: ObjectId
    num: str
    title: str
    overview: List[str]
    design: List[str]
    tech_stack: List[str]
    expected_outcomes: List[str]
    github: List[str]
    web: List[str]
    features: List[str]

    class Settings:
        collection = "myportfolio"


    