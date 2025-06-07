from pydantic import BaseModel, Field
from typing import List
from weaver.node_schema.PlanningPhase.enums.feasibility_study_enum import EconomicFeasibilityEnum, TechnicalFeasibilityEnum

class TechnologyStackAssessment(BaseModel):
    compatibility: str = Field(..., description='Assessment of technology stack compatibility with project requirements')
    maturity: str = Field(..., description='Evaluation of technology maturity and support')
    expertise: str = Field(..., description='Assessment of team expertise and skill level')
    learning_curve: str = Field(..., description='Evaluation of learning curve and training requirements')

class ResourceEvaluation(BaseModel):
    team_size: str = Field(..., description='Required team size and composition')
    skill_sets: str = Field(..., description='Required skill sets and roles')
    infrastructure: str = Field(..., description='Infrastructure and hosting requirements')
    tools: str = Field(..., description='Development tools and environment needs')

class RiskAssessment(BaseModel):
    major_challenges: str = Field(..., description='Major technical challenges and obstacles')
    complexity: str = Field(..., description='Overall project complexity assessment')
    integration_complexity: str = Field(..., description='Complexity of system integrations')

class ImplementationConsiderations(BaseModel):
    timeline: str = Field(..., description='Timeline feasibility assessment')
    testing: str = Field(..., description='Testing and quality assurance requirements')
    deployment: str = Field(..., description='Deployment and maintenance considerations')

class TechnicalAssessment(BaseModel):
    technology_stack: TechnologyStackAssessment = Field(..., description='Technology stack analysis')
    resource_evaluation: ResourceEvaluation = Field(..., description='Resource requirements evaluation')
    risk_assessment: RiskAssessment = Field(..., description='Risk and challenge assessment')
    implementation_considerations: ImplementationConsiderations = Field(..., description='Implementation planning considerations')

class TechnicalFeasibility(BaseModel):
    classification: TechnicalFeasibilityEnum = Field(..., description='Technical feasibility classification')
    assessment: TechnicalAssessment = Field(..., description='Detailed technical assessment')

class CostAnalysis(BaseModel):
    development: str = Field(..., description='Development costs breakdown')
    operational: str = Field(..., description='Operational costs over project lifecycle')
    contingency: str = Field(..., description='Contingency budget allocation')

class RevenueProjections(BaseModel):
    year_1: str = Field(..., description='Year 1 revenue and GMV projections')
    year_2: str = Field(..., description='Year 2 revenue and GMV projections')
    year_3: str = Field(..., description='Year 3 revenue and GMV projections')

class FinancialMetrics(BaseModel):
    roi: str = Field(..., description='Return on Investment projections')
    break_even: str = Field(..., description='Break-even timeline')
    funding: str = Field(..., description='Funding requirements')
    profitability: str = Field(..., description='Profitability trends and outlook')

class EconomicAssessment(BaseModel):
    cost_analysis: CostAnalysis = Field(..., description='Comprehensive cost analysis')
    revenue_projections: RevenueProjections = Field(..., description='Revenue and growth projections')
    financial_metrics: FinancialMetrics = Field(..., description='Key financial metrics and KPIs')

class EconomicFeasibility(BaseModel):
    classification: EconomicFeasibilityEnum = Field(..., description='Economic feasibility classification')
    assessment: EconomicAssessment = Field(..., description='Detailed economic assessment')

class Recommendations(BaseModel):
    approval: str = Field(..., description='Overall approval recommendation')
    conditions: List[str] = Field(..., description='List of conditions for approval')