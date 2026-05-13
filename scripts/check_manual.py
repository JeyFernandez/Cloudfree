from docs.models import Manual
import markdown, textwrap
slug = 'instalacion-de-docker-en-ubuntu-2404'
m = Manual.objects.filter(slug=slug).first()
if not m:
    print('NOT FOUND for slug:', slug)
else:
    print('FOUND')
    print('TITLE:', m.title)
    html = markdown.markdown(m.content or '', extensions=['fenced_code','codehilite'])
    print('HTML length:', len(html))
    print('HTML snippet:\n', textwrap.shorten(html.replace('\n',' '), width=400))
