def my_favourite_keyword(day):
    result = "Hello world"
    if day == "Monday":
        result = "Nothing is favourite on monday"
    elif day == "Tuesday":
        result = "Waiting for friday"
    else:
        result = "No clue"
    return result

def my_favourite_colour(day, slept_well:bool=True):
    if day == "Monday" and slept_well:
        return "Pink"
    if day == "Tuesday" and not slept_well:
        return "Dark black"
    return "Blue"

def favourite_colours(day, *persons):
    colours = {}
    for person in persons:
        if day == "Monday":
            colours[person] = "Pink"
        else:
            colours[person] = "White"
    return colours

def favourite_drinks(time="1 pm", name="Andre", **circumstances):
    drink = "Beer"
    circumstances_string = ""
    for key, value in circumstances.items():
        circumstances_string += f"{key} is {value}"

    return f"{name} likes {drink} at this time {time}, "\
           f"considering the circumstances: {circumstances_string}"

def my_keyword_only_named_args(*, arg1, arg2):
    return f"{arg1} - {arg2}"


def keyword_multi_return():
    a = "hello"
    b = "world"
    return a, b
