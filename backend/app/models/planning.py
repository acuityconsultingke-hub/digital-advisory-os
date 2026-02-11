from pydantic import BaseModel

# Model for planning request
define class PlanningRequest(BaseModel):
    title: str
    description: str
    start_date: str  # ISO formatted date
    end_date: str    # ISO formatted date
    allocated_budget: float
    team_members: list[str]

# Model for planning response
define class PlanningResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str  # e.g., 'Pending', 'In Progress', 'Completed'
    start_date: str
    end_date: str
    allocated_budget: float
    team_members: list[str]
    created_at: str  # Timestamp of creation
    updated_at: str  # Timestamp of last update

