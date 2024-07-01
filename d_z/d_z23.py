from jinja2 import Template

html = """
{% macro input_func(type, name, placeholder) -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% endmacro -%}

<p>{{ input_func('text', 'firstname', 'Имя') }}</p>
<p>{{ input_func('text', 'lastname', 'Фамилия') }}</p>
<p>{{ input_func('text', 'address', 'Адрес') }}</p>
<p>{{ input_func('email', 'email', 'Почта') }}</p>
<p>{{ input_func('tel', 'phone', 'Телефон') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)