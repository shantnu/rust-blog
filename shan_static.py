import markdown
import sys
import re
import jinja2
import pdb

filein = sys.argv[1]
with open(filein, 'r') as f:
    md_text = f.read()

html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])

with open('template.jinja') as file_:
    template = jinja2.Template(file_.read())

title = re.findall('Title: ([\w :]*)', html)[0]
print(title)
# pdb.set_trace()
html2 = re.sub('Title: [\w :]*','', html)
print(html2[:20])

outfile = template.render(title = title, body=html2)


with open('outfile.html', 'w') as f:
    f.write(outfile)