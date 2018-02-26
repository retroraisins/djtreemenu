from django.shortcuts import render
from treemenu.models import MenuItem
from django.http import HttpResponse


def index(request):
    # template = 'treemenu/index.html'
    # treemenu = {'menu': MenuItem.get_menu_from(ROOT_MENU_ID)}

    def render_item(menu_item):
        child_menu = ''
        if menu_item['children']:
            for item in menu_item['children']:
                child_menu += render_item(item)
        return ''.join('<li><a href="{}">{}</a><ul>{}</ul></li>'.format(menu_item['url'], menu_item['title'], child_menu))

    ROOT_MENU_ID = 5
    ul_items = ''
    for menu_item in MenuItem.get_menu_from(ROOT_MENU_ID):
        ul_items += render_item(menu_item)
    ul = ''.join(['<ul>', ul_items, '</ul>'])
    return HttpResponse(ul)
    # return render(request, template, context=treemenu)


def navigate(request):
    template = 'treemenu/blank_page.html'

    requested_url = request.get_full_path()[1:]
    if MenuItem.objects.filter(url=requested_url).exists():
        page = MenuItem.objects.get(url=requested_url)
        requested_page_title = page.title
        return render(request, template, context={'title': requested_page_title})
    return index(request)
