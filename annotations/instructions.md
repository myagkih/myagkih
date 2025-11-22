# Инструкция по установке

*Быстрая установка и запуск:*
В терминале или Git Bash:

- На Linux и Mac:

`git clone https://github.com/myagkih/myagkih.git && cd myagkih && python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && python3 src/main.py`

- На Windows:

`git clone https://github.com/myagkih/myagkih.git && cd myagkih && python -m venv venv && pip install --upgrade pip && python -m pip install -r requirements.txt && winpty python src/main.py`

### *Поэтапная установка:*

*На Linux и Mac*:

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/myagkih/myagkih.git
   ```

2. **Переход в директорию проекта**
   ```bash
   cd myagkih
   ```

3. **Создание виртуального окружения**
   ```bash
   python3 -m venv venv
   ```

4. **Активация виртуального окружения**
   ```bash
   source venv/bin/activate
   ```

5. **Обновление pip**
   ```bash
   pip install --upgrade pip
   ```

6. **Установка зависимостей**
   ```bash
   pip install -r requirements.txt
   ```

7. **Запуск проекта**
   ```bash
   python3 src/main.py
   ```

*На Windows*:

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/myagkih/myagkih.git
   ```

2. **Переход в директорию проекта**
   ```bash
   cd myagkih
   ```

3. **Создание виртуального окружения**
   ```bash
   python -m venv venv
   ```

4. **Обновление pip**
   ```bash
   pip install --upgrade pip
   ```

5. **Установка зависимостей**
   ```bash
   python -m pip install -r requirements.txt
   ```

6. **Запуск проекта**
   ```bash
   winpty python src/main.py
   ```
### Необходимые технические требования:

- Python 3.8
- [requirements.txt](../requirements.txt)
- git bash *на Windows*
- git *на Linux и MacOS*

