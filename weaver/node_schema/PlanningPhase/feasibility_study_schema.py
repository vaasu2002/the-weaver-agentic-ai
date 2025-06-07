from pydantic import BaseModel, Field
from weaver.node_schema.PlanningPhase.helpers.feasibility_study_helpers \
      import EconomicFeasibility, Recommendations, TechnicalFeasibility

class FeasibilityStudySchema(BaseModel):
    project_title: str = Field(..., description='Title of the project being analyzed')
    technical_feasibility: TechnicalFeasibility = Field(..., description='Technical feasibility analysis')
    economic_feasibility: EconomicFeasibility = Field(..., description='Economic feasibility analysis')
    recommendations: Recommendations = Field(..., description='Final recommendations and approval status')

    class Config:
        use_enum_values = True
        json_schema_extra = {
            'example': {
                'project_title': 'E-commerce Platform for Handmade Goods',
                'technical_feasibility': {
                    'classification': 'feasible',
                    'assessment': {
                        'technology_stack': {
                            'compatibility': 'The MERN stack is widely used and compatible with the project requirements.',
                            'maturity': 'Mature and well-supported technologies.',
                            'expertise': 'The team may need to enhance their skills in specific areas but overall manageable.',
                            'learning_curve': 'Moderate, with potential need for additional training.'
                        },
                        'resource_evaluation': {
                            'team_size': '6-8 developers with expertise in MERN stack.',
                            'skill_sets': 'Backend, frontend, full-stack, and DevOps engineers.',
                            'infrastructure': 'Cloud hosting (AWS, Heroku) with appropriate scaling solutions.',
                            'tools': 'Git, Docker, Jenkins for CI/CD.'
                        },
                        'risk_assessment': {
                            'major_challenges': 'Security, payment integration, scalability.',
                            'complexity': 'Medium to high due to critical requirements.',
                            'integration_complexity': 'Moderate with third-party services.'
                        },
                        'implementation_considerations': {
                            'timeline': '24 weeks is feasible with proper planning.',
                            'testing': 'Critical for performance and functionality.',
                            'deployment': 'Needs careful planning for minimal downtime.'
                        }
                    }
                },
                'economic_feasibility': {
                    'classification': 'viable',
                    'assessment': {
                        'cost_analysis': {
                            'development': '$200,000 (salaries, tools, infrastructure)',
                            'operational': '$450,000 over three years (hosting, maintenance, support)',
                            'contingency': '$40,000 (20% of development costs)'
                        },
                        'revenue_projections': {
                            'year_1': '$1.5 million in gross merchandise value, $150,000 revenue.',
                            'year_2': '$1.8 million GMV, $180,000 revenue.',
                            'year_3': '$2.16 million GMV, $216,000 revenue.'
                        },
                        'financial_metrics': {
                            'roi': '75% by year three.',
                            'break_even': '18 months.',
                            'funding': '$500,000 required.',
                            'profitability': 'Increasing net profit each year.'
                        }
                    }
                },
                'recommendations': {
                    'approval': 'Approved with conditions.',
                    'conditions': [
                        'Secure necessary funding.',
                        'Ensure team training and expertise.',
                        'Monitor timeline and risks closely.'
                    ]
                }
            }
        }