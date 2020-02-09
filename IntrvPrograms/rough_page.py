import sys
import re


test_string = "12	23		123"

Regex_Pattern = r"^(\S{2,3}\s?)(\S{2}\s+)(\S{2,3}\s?)$"	# Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())