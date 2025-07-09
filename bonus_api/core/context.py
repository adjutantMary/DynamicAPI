from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

# Датакласс для контекста расчета бонуса
# Нужен для хранения входных данных 

@dataclass
class BonusCalculationContext:
    
    """"
    Датакласс для контекста расчета бонуса
    Нужен для хранения входных данных 
    """
    
    amount: Decimal
    timestamp: datetime
    customer_status: str
    current_bonus: Decimal = Decimal('0')
