from abc import ABC, abstractmethod
from .context import BonusCalculationContext


class BaseBonusRule(ABC):
    """Интерфейс правил"""

    code: str

    @abstractmethod
    def apply(self, ctx: BonusCalculationContext) -> None:
        pass


