from typing import List


def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """
    sind = 0  # current index we are looking at in source list
    pind = 0  # current index we are looking at in pattern list
    result: List[str] = []  # to store substitutions we will return if matched

    while sind < len(source) or pind < len(pattern):
        if pind == len(pattern) and sind < len(source):
            return None
        elif(pattern[pind] == "%"):
            e = True
            try:
                toSearch = pattern[pind + 1]
            except:
                toSearch = ""
            toAdd = ""
            while(e):
                if sind == len(source):
                    break
                elif(source[sind] == toSearch):
                    e = False
                    break
                else:
                    toAdd += source[sind] + " "
                    sind += 1
            pind += 1
            result.append(toAdd[:-1])
        elif sind == len(source) and pind < len(pattern):
            return None
        elif(pattern[pind] == "_"):
            result.append(source[sind])
            pind += 1
            sind += 1
        elif(source[sind] == pattern[pind]):
            pind += 1
            sind += 1
        else:
            return None

    return result