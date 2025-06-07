from typing import List, Optional
from pydantic import BaseModel, Field
from weaver.node_schema.PlanningPhase.enums.project_requirments_enum \
    import RequirementPriority,RequirementType,ProjectDomain,PreferedTechStack


class RequirementDesc(BaseModel):
    requirement: str = Field(..., description='Description of requirement')
    priority: RequirementPriority = Field(..., description='Priority level of the requirement')
    type:RequirementType = Field(...,description='Type of the requirement')



class ProjectRequirmentsSchema(BaseModel):

    title: str = Field(
        ..., min_length=3, max_length=200, description='The title of the project'
    )

    description: str = Field(
        ..., min_length=100, description='Detailed description of the project'
    )

    project_duration_in_weeks:Optional[int] = Field(
        ..., min=1,max=52,description='Duration of project'
    )

    requirements: List[RequirementDesc] = Field(
        ..., 
        description='The list of requirements with their priority levels and type'
    )    

    domain: ProjectDomain = Field(..., description='Domain or category (e.g., fintech, edtech) this project belongs to')
    
    prefered_techstack: PreferedTechStack = Field(...,description='Prefered tech stack of this project')