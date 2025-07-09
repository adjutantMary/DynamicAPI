# Сервис расчёта бонусов

API-сервис на Django + DRF для расчёта бонусных баллов по гибким правилам.

Правила хранятся в базе и легко меняются через админку. Логика расчёта построена на движке, который применяет правила в заданном порядке.

## Что умеет

- Начисляет бонусы по сумме покупки
- Учитывает статус клиента (обычный / VIP)
- Удваивает бонусы в выходные и праздники
- Поддерживает расширение правил без изменений в коде

## Запуск

```bash
git clone <репозиторий>
cd <папка проекта>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Пример запроса

POST /api/calculate-bonus/

```json
{
  "transaction_amount": 150,
  "timestamp": "2025-03-08T14:30:00Z",
  "customer_status": "vip"
}
```

## Пример ответа

```json
{
  "total_bonus": "42.00",
  "applied_rules": [
    {"rule": "base_rate", "bonus": "15.00"},
    {"rule": "holiday_bonus", "bonus": "15.00"},
    {"rule": "vip_boost", "bonus": "12.00"}
  ]
}
```

## Как добавить правило

1. Перейти в админку: http://localhost:8000/admin/
2. Открыть раздел Bonus Rules
3. Создать правило с нужными полями:
   - condition_type: например, always, is_weekend_or_holiday, customer_status
   - operation_type: base, multiply, percent_add
   - priority: чем меньше — тем раньше применяется

Примеры operation_value:

```json
{"per_amount": 10}        // base
{"factor": 2}             // multiply
{"value": 40}             // percent_add
```

## Зависимости

- Python 3.10+
- Django 4+
- Django REST Framework
- holidays (для проверки праздников)

## Структура проекта

- bonus/models.py — правила расчёта
- bonus/views.py — API
- bonus/factory.py — движок создания правил (RuleFactory)
- bonus/serializers.py — валидация входа и формирование ответа
- bonus/admin.py — удобное редактирование правил
- core/ - engine по интерфейсам
- rules/ - основная логика создания правил
- service/ - логика обработки бонусов
  
