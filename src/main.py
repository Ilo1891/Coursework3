# Вызываем импорты
from src.utils import load_operations, get_last_five_operations
from src.operation_class import Operation

#Cписок всех операций клиента
operations_list = load_operations()

# Создаем список из 5 последних выполненных (EXECUTED) клиентом операций
last_five_operations = get_last_five_operations(operations_list)

# Перебираем список и для каждой операции выводим данные в соответствии с тз
for element in last_five_operations:
    operation = Operation(element)
    print(f"""\n{operation.date()} {operation.description()}
{operation.hide_number(operation.account_from())} -> {operation.hide_number(operation.account_to())}
{operation.amount()}""")