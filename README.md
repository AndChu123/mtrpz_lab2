# ArrayList та LinkedList (Лабораторна робота)

## Опис застосунку
Застосунок демонструє роботу з типізованим списком символів (Character) з двома реалізаціями:
- **ArrayList** — на базі вбудованого масиву
- **LinkedList** — двобічно зв'язаний список

Кожен клас підтримує такі методи: length, append, insert, delete, deleteAll, get, clone, reverse, findFirst, findLast, clear, extend.

## Варіант
- Початкова реалізація списку — список на базі вбудованих масивів/списків
- Друга реалізація списку — двобічно зв'язаний список

## Інструкція запуску

1. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустіть тести для обох реалізацій:
   ```bash
   python -m unittest discover tests
   ```
   або з перевіркою покриття:
   ```bash
   coverage run -m unittest discover tests
   coverage report
   ```
3. Запустіть демонстрацію для обох реалізацій:
   ```bash
   python demo.py
   ```
   Ви побачите приклади роботи з ArrayList та LinkedList.

## CI
- Для автоматичного запуску тестів використовується GitHub Actions.

## Посилання на "падаючий" коміт
- [https://github.com/AndChu123/mtrpz_lab2/commit/99e783aec66b9bdfd16985380daac45f90db5375]

## Висновки
- Здобув навички для покриття коду проекта unit тестами