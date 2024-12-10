def total_salary(path: str):
    try:
        # Відкриваємо файл з потрібним кодуванням
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            
            for line in file:
                # Видаляємо зайві пробіли та розбиваємо рядок
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # Пропускаємо рядки з помилками
                
                # Додаємо зарплату до списку, якщо це число
                try:
                    salary = int(parts[1])
                    salaries.append(salary)
                except ValueError:
                    continue  # Пропускаємо некоректні дані
            
            # Якщо немає зарплат, повертаємо нулі
            if not salaries:
                return (0, 0)
            
            # Обчислення загальної та середньої зарплати
            total = sum(salaries)
            average = total / len(salaries)
            
            return (total, average)
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Створення тестового файлу
test_path = "salary_file.txt"
with open(test_path, "w", encoding="utf-8") as file:
    file.write("Alex Korp,3000\n")
    file.write("Nikita Borisenko,2000\n")
    file.write("Sitarama Raju,1000\n")

# Виклик функції
total, average = total_salary(test_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
