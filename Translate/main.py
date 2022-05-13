#!/usr/bin/env python
import sys
import module.translate as translate

arg = sys.argv

print(translate.rendering(arg[1], arg[2]))
