import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    """
    Розбирає рядок логу і повертає словник з компонентами:
    дата, час, рівень, повідомлення
    """
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return None  # рядок не відповідає формату
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> List[dict]:
    """
    Завантажує всі рядки логу з файлу і повертає список словників.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Повертає список логів, що відповідають заданому рівню.
    """
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
    return {lvl: sum(1 for log in logs if log["level"] == lvl) for lvl in levels}


def display_log_counts(counts: Dict[str, int]):
    """
    Виводить підрахунок логів у вигляді таблиці.
    """
    print(f"{'Рівень логування':<16} | {'Кількість':<8}")
    print('-'*25 + '|'+ '-'*8)
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів рівня '{level_filter.upper()}' не знайдено.")


if __name__ == "__main__":
    main()