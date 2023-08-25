"""
Stores terms that are used in many different places
"""
from talon import Context, Module


mod = Module()
ctx = Context()

mod.list(
    "cursorless_homophone",
    "Various alternative pronunciations of 'cursorless' to improve accuracy",
)

ctx.lists["user.cursorless_homophone"] = [
    "cursorless",
    "cursor less",
    "cursor list",
    "chrysalis",
]


SELECT = "take"
TELEPORT = "go"
OPERATOR = "make"
DELETE = "chuck"
FIND = "search"
SHOW_LIST = "list"


@mod.capture(rule=SELECT)
def select(m) -> str:
    """Term for select"""
    return str(m)


@mod.capture(rule=TELEPORT)
def teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    return str(m)


@mod.capture(rule=OPERATOR)
def operator(m) -> str:
    """Prefix for operators"""
    return str(m)


@mod.capture(rule=DELETE)
def delete(m) -> str:
    """Verb to use for commands that delete things"""
    return str(m)


@mod.capture(rule=FIND)
def find(m) -> str:
    """Verb to use for commands that find things"""
    return str(m)


@mod.capture(rule=SHOW_LIST)
def show_list(m) -> str:
    """Verb to use for commands that show lists"""
    return str(m)
