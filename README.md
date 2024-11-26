#Конфигурационное управление

Домашнее задание №3

## Содержание

- [Задача](#задача)
- [Установка](#установка)
- [Использование](#использование)
- [Демонстрация](#демонстрация)
- [Тестирование](#тестирование)

---
## Задача

Вариант №23

Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.
Входной текст на языке toml принимается из файла, путь к которому задан
ключом командной строки. Выходной текст на учебном конфигурационном
языке попадает в стандартный вывод.

Однострочные комментарии:
```
// Это однострочный комментарий
```

Массивы:
```
list( значение, значение, значение, ... )
```

Имена:
```
[a-z][a-z0-9_]*
```

Значения:
• Числа.
• Массивы.

Объявление константы на этапе трансляции:
имя = значение

Вычисление константного выражения на этапе трансляции (инфиксная форма), пример:
?{имя + 1}
Результатом вычисления константного выражения является значение.

Для константных вычислений определены операции и функции:

1. Сложение.
2. Вычитание.
3. Умножение.
4. Деление.
5. sort().
6. max().

Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3
примера описания конфигураций из разных предметных областей.
---

## Установка

Для работы с проектом выполните следующие шаги:

1. Убедитесь, что у вас установлен Python версии 3.8 или выше. Проверьте это командой:

   ```bash
   python --version
   ```

2. Склонируйте репозиторий или создайте локальную папку с файлами проекта:

   ```
   converter.py
   test_converter.py
   config1.toml
   config2.toml
   config3.toml
   ```

3. Создайте виртуальное окружение и активируйте его:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate     # Для Windows
   ```

4. Установите библиотеку `toml`, если она еще не установлена:

   ```bash
   pip install toml
   ```

---

## Использование

1. Убедитесь, что у вас есть входной TOML-файл. Например: `config.toml`.

2. Запустите скрипт `converter.py`, указав путь к вашему TOML-файлу:

   ```bash
   python converter.py config1.toml
   ```

 ```bash
   python converter.py config2toml
   ```

 ```bash
   python converter.py config3.toml
   ```

3. Программа выведет преобразованный конфиг в стандартный вывод (терминал). Например, для входного файла:

```config1.toml
# web_app_config.toml
server_host = "localhost"
server_port = 8080
static_files_dir = "/var/www/static"
database_url = "postgresql://user:password@localhost/dbname"
debug_mode = true
max_connections = 100
session_timeout = 3600
allowed_origins = ["http://localhost:3000", "https://example.com"]
```

   Вы получите следующий результат:

```
server_host = localhost
server_port = 8080
static_files_dir = /var/www/static
database_url = postgresql://user:password@localhost/dbname
debug_mode = True
max_connections = 100
session_timeout = 3600
allowed_origins = list(http://localhost:3000, https://example.com)
```

---

## Демонстрация

### Входной файл (`config1.toml`)

```toml
# web_app
server_host = "localhost"
server_port = 8080
static_files_dir = "/var/www/static"
database_url = "postgresql://user:password@localhost/dbname"
debug_mode = true
max_connections = 100
session_timeout = 3600
allowed_origins = ["http://localhost:3000", "https://example.com"]
```

```toml
# monitoring
monitoring_interval = 60
alert_threshold = 90
log_file = "/var/log/monitoring.log"
email_notifications = true
notification_email = "admin@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_user = "monitoring@example.com"
smtp_password = "securepassword"
```


```toml
# task_manager
task_queue = "redis://localhost:6379/0"
worker_count = 4
max_task_retries = 3
task_timeout = 300
result_backend = "db+postgresql://user:password@localhost/dbname"
log_level = "INFO"
log_file = "/var/log/task_manager.log"
```


### Команда запуска

```bash
python converter.py config1.toml
```

```bash
python converter.py config2.toml
```

```bash
python converter.py config3.toml
```

### Результат в терминале

![art](https://github.com/Klombik/HM3KU/blob/9439648a5911e16beda7fe60d8e7dde850903b4f/p3.png)


![art](https://github.com/Klombik/HM3KU/blob/2fad633e1524f068fdf4a97fce8695a9740deef7/p32.png)


```config3.toml
task_queue = redis://localhost:6379/0
worker_count = 4
max_task_retries = 3
task_timeout = 300
result_backend = db+postgresql://user:password@localhost/dbname
log_level = INFO
log_file = /var/log/task_manager.log
```

---

## Тестирование

Проект включает тесты, написанные с использованием модуля `unittest`. Чтобы запустить тесты, выполните:

```bash
python -m unittest test_converter.py
```

### Пример результата успешного тестирования

```
C:\Users\smart\convertHMKU3>python -m unittest test_converter.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
```

### Описание тестов

- **`test_convert_value`**: Проверяет корректность преобразования значений (целые числа, строки, списки, булевы значения).
- **`test_validate_name`**: Проверяет валидацию имен ключей.
- **`test_generate_config`**: Проверяет генерацию итогового конфига на основе входных данных.
- **`test_evaluate_expression`**: Проверяет вычисление выражений в строках.
- **`test_generate_config_with_expressions`**: Проверяет обработку TOML-файлов с выражениями.

---


