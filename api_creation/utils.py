"""
    File containing all the Utility functions
"""

from collections import Counter
from typing import List


price_list = {'001': 100, '002': 80, '004': 30, '003': 50} 

def price_calc(item_list:List[str]):
    """
    Function to Calculate the price for selected watches

    Parameters
    ---------
    item_list : ist[str]
        List of selected watches 
    
    Returns
    --------
    int 
        Price of the cart
    """
    price = 0
    count_dict = Counter(item_list)
    for watch_id in count_dict:
        if watch_id == "001":
            # Rolex Watches
            if count_dict[watch_id] % 3 == 0:
                # When number of watches are multiple of 3 then discounted price is applied
                price += (count_dict[watch_id]/3) * 200
            else:
                price += count_dict[watch_id] * price_list[watch_id]
        elif watch_id == "002":
            # Michael Kors Watches
            if count_dict[watch_id] % 2 == 0:
                # When number of watches are multiple of 3 then discounted price is applied
                price += (count_dict[watch_id]/2) * 120
            else:
                price += count_dict[watch_id] * price_list[watch_id]
        else:
            price += count_dict[watch_id] * price_list[watch_id] 
    return price