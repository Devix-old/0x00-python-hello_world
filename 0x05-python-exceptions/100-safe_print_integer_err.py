import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError) as erreur:
        print("Exception: {}".format(erreur), file=sys.stderr)
        return (False)
