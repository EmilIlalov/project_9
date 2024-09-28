from src.masks import get_mask_account, get_mask_card_number

card_number = input()
mask_count = input()

result_card_number = get_mask_card_number(card_number)
result_mask_count = get_mask_account(mask_count)
print(result_card_number)
print(result_mask_count)
