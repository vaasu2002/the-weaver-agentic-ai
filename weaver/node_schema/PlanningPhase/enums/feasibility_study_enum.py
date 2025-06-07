from enum import Enum

class TechnicalFeasibilityEnum(str, Enum):
    FEASIBLE = 'feasible'
    NOT_FEASIBLE = 'not_feasible'
    PARTIALLY_FEASIBLE = 'partially_feasible'

class EconomicFeasibilityEnum(str, Enum):
    VIABLE = 'viable'
    NOT_VIABLE = 'not_viable'
    MARGINAL = 'marginal'