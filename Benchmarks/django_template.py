"""Test the performance of the Django template system.

This will have Django generate a 150x150-cell HTML table.
"""

from six.moves import xrange

import django.conf
from django.template import Context, Template
import timeit

size = 100


def bench_django_template( size):
    template = Template("""<table>
{% for row in table %}
<tr>{% for col in row %}<td>{{ col|escape }}</td>{% endfor %}</tr>
{% endfor %}
</table>
    """)
    table = [xrange(size) for _ in xrange(size)]
    context = Context({"table": table})

django.conf.settings.configure(TEMPLATES=[{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
}])
django.setup()

def bench():
    bench_django_template(size)

def time():
    t=timeit.timeit(bench,number=30000)
    return t
