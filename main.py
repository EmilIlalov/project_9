from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

card_number = input()
mask_count = input()

result_get_card_number = get_mask_card_number(card_number)
result_get_mask_account = get_mask_account(mask_count)
result_mask_account = mask_account_card('Visa Platinum 7000792289606361')
result_get_date = get_date("2024-03-11T02:26:18.671407")

print(result_get_mask_account)
print(result_get_card_number)
print(result_mask_account)
print(result_get_date)
