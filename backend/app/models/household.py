from pydantic import BaseModel

class Household(BaseModel):
    id: int
    address: str
    number_of_members: int
    owner: str

class Member(BaseModel):
    id: int
    name: str
    age: int
    relationship_to_head: str

class HouseholdDetails(BaseModel):
    household: Household
    members: List[Member]