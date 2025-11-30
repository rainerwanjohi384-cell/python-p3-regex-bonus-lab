import re

my_pattern = r"[A-Z][a-z\s,']*today['s]?[a-z\s,.'?!]*[.?]"
my_regex = re.compile(my_pattern)

