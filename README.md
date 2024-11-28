# Тестовое задание: Разработка консольного приложения "Менеджер задач" 🚀

## Цель 🎯
Создать приложение для управления списком задач с возможностью добавления, выполнения, удаления и поиска задач.

## Основные возможности ✨

### 1. Просмотр задач 📋
- [ ] Просмотр всех текущих задач
- [ ] Просмотр задач по категориям (например, работа, личное, обучение)

### 2. Добавление задачи ➕
- [ ] Добавление новой задачи с указанием:
  * 📝 названия
  * 📄 описания
  * 🏷️ категории
  * 📅 срока выполнения
  * ⭐ приоритета (низкий, средний, высокий)

### 3. Изменение задачи 🔄
- [ ] Редактирование существующей задачи
- [ ] Отметка задачи как выполненной

### 4. Удаление задачи ❌
- [ ] Удаление задачи по идентификатору или категории

### 5. Поиск задач 🔍
- [ ] Поиск по:
  * ключевым словам
  * категории
  * статусу выполнения

## Требования к программе 📋

### 1. Интерфейс 💻
- [ ] Приложение должно работать через консоль (CLI)
- [ ] Без использования веб или графических интерфейсов
- [ ] Без использования фреймворков (Django, Flask и т.д.)

### 2. Хранение данных 💾
- [ ] Данные должны сохраняться в формате JSON или CSV
- [ ] Каждая задача должна иметь уникальный идентификатор

### 3. Информация о задаче ℹ️
**Поля задачи:**
* 📝 название
* 📄 описание
* 🏷️ категория
* 📅 срок выполнения
* ⭐ приоритет
* ✅ статус (выполнена/не выполнена)

## Дополнительные требования ➕

### 1. Тестирование 🧪
- [ ] Написать тесты с использованием pytest для проверки функций:
  * добавления
  * выполнения
  * поиска
  * удаления задач

### 2. Обработка ошибок ⚠️
- [ ] Программа должна обрабатывать невалидные данные (неправильные даты или пустые поля)

## Оценка 📊

### 1. Архитектура и структура данных 🏗️
- [ ] Правильное использование структур данных (списки, словари)
- [ ] Организация кода по функциям или классам

### 2. Качество кода ⭐
- [ ] Читаемость и стиль кода (соответствие PEP8)
- [ ] Наличие комментариев и типизация

### 3. Объектно-ориентированный подход 🔄
- [ ] Разделение логики на классы (например, Task, TaskManager)

### 4. Покрытие тестами ✅
- [ ] Наличие и качество тестов, покрывающих основные функции

## Пример структуры данных в файле (JSON) 📝
```json
[
  {
    "id": 1,
    "title": "Изучить основы FastAPI",
    "description": "Пройти документацию по FastAPI и создать простой проект",
    "category": "Обучение",
    "due_date": "2024-11-30",
    "priority": "Высокий",
    "status": "Не выполнена"
  }
]
