# Neel Nadkarni and Nathan Stalley

from match import match
from a8_part_II import *
from typing import List, Tuple, Callable, Any
import os

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    # Patterns MUST end in "of %"
    (str.split("birthday of %"), get_birth_date),
    (str.split("polar radius of %"), get_planet_radius),
    (str.split("bye"), bye_action),
]

def extract_before_index(lst, index):
    if index < 0 or index >= len(lst):
        return lst
    else:
        return lst[:index + 1]


def search_pa_list(src: List[str], srcs: str) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """

    for i in range(len(pa_list)):
        if(match(pa_list[i][0], src) != None):
            if(pa_list[i][1](match(pa_list[i][0], src)) == []):
                return ["No answers"]
            else:
                return pa_list[i][1](match(pa_list[i][0], src))

def run() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the wikipedia machine!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower()
            answers = search_pa_list(query.split(), query)
            

            if isinstance(answers, list):
                while(True):
                    os.system("clear")
                    print(answers)
                    option = input("\x1b[31m Which one? (Copy and Paste)\n\n \x1b[37m")
                    print("\n")
                    try:
                        first_half = extract_before_index(query.split(), query.split().index("of"))
                        second_half = answers[answers.index(option)].split()
                        print(search_pa_list(first_half + second_half, first_half + second_half))
                        break
                    except:
                        pass
            else:
                print(answers)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

run()