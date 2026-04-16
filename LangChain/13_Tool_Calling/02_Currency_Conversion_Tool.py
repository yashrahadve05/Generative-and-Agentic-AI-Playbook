# 02_Currency_Conversion_Tool.py



from langchain_core.tools  import tool
from langchain_core.tools import InjectedToolArg
from typing import Annotated
import requests as req

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This tool (function) fetches the currency conversion factor between a given base currency and a target currency"""

    url = f"https://v6.exchangerate-api.com/v6/df7b99ee90534d821c6e8c79/pair/{base_currency}/{target_currency}"
    response = req.get(url)
    data = response.json()
    
    return data

@tool
def convert_currency(base_currency_value: int, conversion_rate: float) -> float:
    """Given a currency conversion rate this function calculates the target currency value from a given base currency value"""

    return base_currency_value * conversion_rate


print(get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency': 'INR'}))


print(convert_currency.invoke({'base_currency_value': 20, 'conversion_rate': 93.26}))