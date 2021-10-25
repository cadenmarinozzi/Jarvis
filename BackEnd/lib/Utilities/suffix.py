numberSuffixes = {
    1: "st",
    2: "nd",
    3: "rd",
    21: "st",
    22: "nd",
    23: "rd",
    31: "st"
};

def suffixNumber(number):
    try:
        numericalSuffix = numberSuffixes[number];
    except KeyError:
        numericalSuffix = "th";

    return numericalSuffix;