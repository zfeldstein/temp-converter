import argparse

VALID_UNITS = ['k', 'f', 'c', 'r']

# Returns value in requested units from fareneheit.


def from_farenheit(temp, target):
    # Farenheit to Celcius
    if target == 'c':
        converted_temp = (temp - 32) / 1.8
    # Farenheit to Kelvin
    if target == 'k':
        converted_temp = (temp + 459.67) / 1.8
    # Farenheit to Rankine
    if target == 'r':
        converted_temp = temp + 459.67
    return converted_temp

# Returns value in requested units from Celcius.


def from_celcius(temp, target):
    if target == 'f':
        c_temp = temp * 1.8 + 32
    if target == 'k':
        c_temp = temp + 273.15
    if target == 'r':
        c_temp = temp * 1.8 + 32 + 459.67
    return c_temp

# Returns value in requested units from Kelvin


def from_kelvin(temp, target):
    if target == 'c':
        c_temp = temp - 273.15
    if target == 'f':
        c_temp = temp * 1.8 - 459.67
    if target == 'r':
        c_temp = temp * 1.8
    return c_temp

# Return Values in requested units from Rankine


def from_rankine(temp, target):
    if target == 'c':
        c_temp = (temp - 32 - 459.67) / 1.8
    if target == 'f':
        c_temp = temp - 459.67
    if target == 'k':
        c_temp = temp / 1.8
    return c_temp


parser = argparse.ArgumentParser()

parser.add_argument(
    "-s", "--source", dest="source_unit",  required=True,
    help="Source unit to convert from (i.e. c=Celcisus,"
         "k= Kelvin, F=Farenheit, r=Rankine"
)

parser.add_argument(
    "-t", "--target", dest="target_unit",  required=True,
    help="Target unit to convert to (i.e. c=Celcisus,"
         "k= Kelvin, F=Farenheit, r=Rankine"
)

parser.add_argument(
    "-a", "--answer", dest="student_answer",  required=True,
    help="Students answer to conversion,"
)


parser.add_argument("temperature",
                    help="Temperature value (i.e. 85) ")

args = parser.parse_args()

source_unit = args.source_unit.lower()
target_unit = args.target_unit.lower()

# If user specifies string for input or answer temp
# will fail with "invalid"
try:
    temp = float(args.temperature)
    s_answer = float(args.student_answer)
except ValueError:
    print("invalid")
    exit(1)

# Verify user can only supply valid units we support conversions for
if source_unit and target_unit not in VALID_UNITS:
    exit("Please specify valid source measurement unit: k, f, c, r ")

new_temp = None
if source_unit == 'f':
    new_temp = from_farenheit(temp, target_unit)
if source_unit == 'c':
    new_temp = from_celcius(temp, target_unit)
if source_unit == 'k':
    new_temp = from_kelvin(temp, target_unit)
if source_unit == 'r':
    new_temp = from_rankine(temp, target_unit)

# After performing conversion, round student answer and conversion to
# The one's place and validate equality.
if round(new_temp) == round(s_answer):
    print("Correct")
    exit(0)
else:
    print("Incorrect")
    exit(1)
