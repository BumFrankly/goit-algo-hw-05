import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>\w+)\s+(?P<message>.+)'
    match = re.match(pattern, line)
    match = re.match(pattern, line)
    if match:
        log = match.groupdict()
        log['level'] = log['level'].upper() 
        return log
    return None

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
                else:
                    print(f"Неправильний формат рядка логу: {line.strip()}")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count:<10}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Введіть шлях до файлу логів як аргумент командного рядка.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level.upper())
        display_log_counts(count_logs_by_level(filtered_logs))
        
        # Вивід деталей логів для конкретного рівня
        if level.upper() in ["ERROR", "WARNING", "INFO", "DEBUG"]:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        display_log_counts(count_logs_by_level(logs))
