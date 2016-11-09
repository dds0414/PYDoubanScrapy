# -*- coding: utf-8 -*-
import re

s = "(224人评价)"
print re.findall(r"(\w+)", s)