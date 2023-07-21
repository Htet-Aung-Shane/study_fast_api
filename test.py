from typing import Union
from typing import Optional

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

def process_items(items: list[str]):
    for item in items:
         print(item)

def process_item(item: Union[int, str]):
    print(item)

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

print(say_hi('Htet Aung'))