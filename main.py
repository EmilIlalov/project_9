from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_number = input("Введите номер карты:\n")
mask_count = input("Введите номер счета:\n")

result_get_card_number = get_mask_card_number(card_number)
result_get_mask_account = get_mask_account(mask_count)
result_mask_account = mask_account_card('Visa Platinum 7000792289606361')
result_get_date = get_date("2024-03-11T02:26:18.671407")
result_filter_by_state = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                                          ])
result_sort_by_date = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                                    ])

print(result_get_mask_account)
print(result_get_card_number)
print(result_mask_account)
print(result_get_date)
print(result_filter_by_state)
print(result_sort_by_date)
