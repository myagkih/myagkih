# Проект "Калькулятор для математического анализа"

## Описание проекта

Крайне полезный инструмент для решения задач математического анализа. Проект предоставляет функционал для **работы с производными** (включая высшего порядка и частные), **вычисления определенных и неопределенных интегралов**, а также **визуализации функций через построение графиков**.

## Инструкция по установке

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

## Возможности проекта

1. Вычисление производных n-ого порядка
2. Вычисление частных производных
3. Вычисление неопределенных интегралов
4. Вычисление определенных интегралов
5. Потроение графика функции
