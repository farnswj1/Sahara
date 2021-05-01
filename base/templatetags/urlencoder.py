from django.template import Library

register = Library()

@register.simple_tag
def search_url(field_name, value, urlencode=None):
    url = f"{field_name}={value}"

    # If a querystring has been provided, extend the URL
    if urlencode:
        # Remove the field name and its value from the query string
        query_string = "&".join(filter(lambda x: x.split("=")[0] != field_name, urlencode.split("&")))

        # This only runs if anything besides the field name was in the URL encode
        if query_string:
            url = query_string + "&" + url
    
    # Prepend the ? since it's a query URL
    return "?" + url