from stories import Story

madlibs = [
    Story(
        "Once upon a time...",
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a large
        {adjective} {noun}. It loved to {verb} {plural_noun}."""
    ),
    Story(
        "My noun is adj",
        ["noun", "adjective"],
        """My {noun} is {adjective}."""
    ),
]

def get_madlibs():
    return madlibs

def get_madlib_by_id(id):
    for madlib in madlibs:
        if id == madlib.id:
            return madlib
    return None