from holidays import RU


class BaseCondition:
    
    """
    Этот класс определяет базовый класс BaseCondition
    
    __init__: Инициализирует объект условия
    check: Проверяет условие
    """
    
    def __init__(self, config):
        pass
    
    def check(self, ctx):
        raise NotImplementedError


class AlwaysCondition(BaseCondition):
    
    """
    __init__(self, config): Инициализирует экземпляр класса AlwaysCondition
    check(self, ctx): Всегда возвращает True, указывая, что условие всегда выполнено, независимо от контекста ctx
    """
    
    def __init__(self, config):
        pass
    
    def check(self, ctx):
        return True


class WeekendOrHolidayCondition(BaseCondition):
    
    """
    __init__(self, config): Инициализирует экземпляр класса
    check(self, ctx): Проверяет, является ли заданная дата выходным днем или праздником,
    и возвращает True, если это так, и False в противном случае.
    """
    
    def __init__(self, config):
        pass
    def check(self, ctx):
        date = ctx.timestamp.date()
        return ctx.timestamp.weekday() >= 5 or date in RU()


class CustomerStatusCondition(BaseCondition):
    """
    __init__(self, config: dict): Инициализирует экземпляр класса с помощью словаря конфигурации
    и извлекает статус клиента из него
    
    check(self, ctx): Проверяет, совпадает ли статус клиента в предоставленном контексте ctx со статусом, 
    хранящимся в переменной экземпляра self.status.
    Возвращает True, если они совпадают, и False в противном случае.
    
    """
    
    def __init__(self, config: dict):
        self.status = config.get("status")

    def check(self, ctx):
        return ctx.customer_status == self.status
