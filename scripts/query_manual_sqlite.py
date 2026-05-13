import sqlite3
import markdown
import textwrap

DB = 'db.sqlite3'
SLUG = 'instalacion-de-docker-en-ubuntu-2404'

con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("SELECT id, title, content FROM docs_manual WHERE slug=?", (SLUG,))
row = cur.fetchone()
if not row:
    print('NOT FOUND', SLUG)
else:
    id_, title, content = row
    print('FOUND id=', id_)
    print('TITLE:', title)
    html = markdown.markdown(content or '', extensions=['fenced_code','codehilite'])
    print('HTML len:', len(html))
    print('\nHTML snippet:\n')
    print(textwrap.shorten(html.replace('\n',' '), width=800))
con.close()
