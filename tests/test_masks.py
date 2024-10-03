import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_mask_card(card_number, mask_number):
    assert get_mask_card_number(card_number) == mask_number


@pytest.mark.parametrize(
    "acc_number, mask_bank_account",
    [
        ("73654108430135874305", "**430"),
        ("64686473678894779589", "**958"),
        ("35383033474447895560", "**556"),
        ("73654108430135874305", "**305"),
    ],
)
def test_mask_account(acc_number, mask_bank_account):
    assert get_mask_account(acc_number) == mask_bank_account
