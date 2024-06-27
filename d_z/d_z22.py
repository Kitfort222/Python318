from jinja2 import Template

mist = [
    {'href': '/index', 'title': 'Главная'},
    {'href': '/news', 'title': 'Новости'},
    {'href': '/about', 'title': 'О компании'},
    {'href': '/shop', 'title': 'Магазин'},
    {'href': '/contacts', 'title': 'Контакты'},
]

link = """<ul>
{% for m in mist -%}
    # {% if m.href[1] %}
    # <li value="{{ m['href'] class="active" }}">{{ m['title'] }}</li>
    # {% else %}
     <li value="{{ m['href'] }}">{{ m['title'] }}</li> 
    # {% endif -%} 
{% endfor -%}
</ul>"""

tm = Template(link)
msg = tm.render(mist=mist)

print(msg)
