# some python libraries we'll be using
import re, string, calendar
from wikipedia import page
from bs4 import BeautifulSoup

from typing import List, Match
from utilities import *

# Assignment 8 Part II


def get_planet_radius(planet_name: str) -> str:
    """Gets the radius of the given planet

    Args:
        planet_name - name of the planet to get radius of

    Returns:
        radius of the given planet
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(planet_name)))
    # TODO: fill this in
    pattern = "REPLACE ME"
    error_text = "Page infobox has no polar radius information"
    match = get_match(infobox_text, pattern, error_text)
    return match.group("radius")


def get_birth_date(name: str) -> str:
    """Gets birth date of the given person

    Args:
        name - name of the person

    Returns:
        birth date of the given person
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
    # TODO: fill this in
    pattern = "REPLACE ME"
    error_text = (
        "Page infobox has no birth information (at least none in xxxx-xx-xx format)"
    )
    match = get_match(infobox_text, pattern, error_text)
    return match.group("birth")


if __name__ == "__main__":
    print("\n<<<<<<<<<<<<<< Testing Planet Radius >>>>>>>>>>>>>>")
    # should be 3,376.2
    print(f'Mars has a polar radius of {get_planet_radius("Mars")}km')
    # should be 6356.752
    print(f'Earth has a polar radius of {get_planet_radius("Earth")}km')
    # should be 66,854
    print(f'Jupiter has a polar radius of {get_planet_radius("Jupiter")}km')
    # should be 54,364
    print(f'Saturn has a polar radius of {get_planet_radius("Saturn")}km')

    # uncomment below lines for tests once you think you're getting the right output
    # print('\n<<<< Running asserts, this might take a sec >>>>')
    # assert get_planet_radius("Mars") == "3376.2", "Incorrect radius for Mars"
    # assert get_planet_radius("Earth") == "6356.752", "Incorrect radius for Earth"
    # assert get_planet_radius("Jupiter") == "66,854", "Incorrect radius for Jupiter"
    # assert get_planet_radius("Saturn") == "54,364", "Incorrect radius for Saturn"
    # print('\n<<<< Planet radius tests passed >>>>')

    print("\n<<<<<<<<<<<<<< Testing Birth Dates >>>>>>>>>>>>>>")
    # should be 1906-12-09
    print(format_birth(get_birth_date("Grace Hopper"), "Grace Hopper"))
    # should be 1912-06-23
    print(format_birth(get_birth_date("Alan Turing"), "Alan Turing"))
    # should be 1955-06-08
    print(format_birth(get_birth_date("Tim Berners-Lee"), "Tim Berners-Lee"))
    # should be 1949-01-17
    print(format_birth(get_birth_date("Anita Borg"), "Anita Borg"))

    # uncomment below lines for tests once you think you're getting the right output
    # print('\n<<<< Running asserts, this might take a sec >>>>')
    # assert get_birth_date("Grace Hopper") == "1906-12-09", "Incorrect birth date for Grace Hopper"
    # assert get_birth_date("Alan Turing") == "1912-06-23", "Incorrect birth date for Alan Turing"
    # assert get_birth_date("Tim Berners-Lee") == "1955-06-08", "Incorrect birth date for Tim Berners-Lee"
    # assert get_birth_date("Anita Borg") == "1949-01-17", "Incorrect birth date for Anita Borg"
    # print('\n<<<< Birth date tests passed >>>>')

    # print('\n<<<< All tests passed! >>>>')
