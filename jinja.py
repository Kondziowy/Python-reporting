#!/Python27/python
import os
from jinja2 import Environment, FileSystemLoader

tpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tpl")

j2_env = Environment(loader=FileSystemLoader(tpl_dir),
                     trim_blocks=True, extensions=["jinja2.ext.do", ])


content = {
    "movies" : [
    ["Matrix", 1998],
    ["Minions", 2015]
    ]
}

html = j2_env.get_template('template.html').render(**content)

with open("raporcik.html","w") as f:
    f.write(html)
