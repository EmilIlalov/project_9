from typing import List, Dict


def filter_by_state(info: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает список состояний банковских операций."""
    new_list_data = []
    for item in info:
        if item.get("state") == state:
            new_list_data.append(item)

    return new_list_data


def sort_by_date(list_dict: List[Dict], sort_data: bool = True) -> List[Dict]:
    """Функция возвращает отсортированный список по дате"""
    return sorted(list_dict, key=lambda item: item["date"], reverse=sort_data)
