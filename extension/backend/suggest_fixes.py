def SuggestFixes(sentence):
    """Returns suggested fixes to the sentence.

    sentence: A unicode object representing the sentence to be fixed.

    suggestions: Fix suggestions. The suggestions take the form of a list of
                 dictionaries. Each dictionary is of the form:
                    (string to be replaced, offset from sentence beginning):
                    (string to replace it with, reason for replacement)
    """
    suggestions = []

    if "bitch" in sentence:
        key = ("bitch", sentence.find("bitch"))
        val = ("woman", 1)
        suggestions.append({key: val})

    return suggestions