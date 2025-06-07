from enum import Enum

class RequirementType(str, Enum):
    FUNCTIONAL = 'functional'
    NON_FUNCTIONAL = 'non_functional'
    USER_INTERFACE = 'user_interface'

class PreferedTechStack(str, Enum):
    MERN_JS = 'mern - mongodb, expressjs, reactjs,nodejs using javascript'
    MEAN_JS = 'marn - mongodb, expressjs, angularjs,nodejs using javascript'
    MERN_TS = 'mern - mongodb, expressjs, reactjs,nodejs using typescript'
    MEAN_TS = 'marn - mongodb, expressjs, angularjs,nodejs using typescript'
    SPRING_BOOT = 'Java Spring Boot, Angular Js'

class ProjectDomain(str, Enum):
    FINTECH = 'fintech'
    EDTECH = 'edtech'
    HEALTHCARE = 'healthcare'
    ECOMMERCE = 'ecommerce'
    SOCIAL_MEDIA = 'social_media'
    PRODUCTIVITY = 'productivity'
    OTHER = 'other'

class RequirementPriority(str, Enum):
    CRITICAL = 'critical'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    NICE_TO_HAVE = 'nice_to_have'