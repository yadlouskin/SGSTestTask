mainmenu = [
    {'button_name': 'Main page', 'url_name': 'main_page'},
    {'button_name': 'Add picture', 'url_name': 'pict_add'},
]
forsinglemenu = [
    {'button_name': 'Picture details', 'url_name': 'pict'},
    {'button_name': 'Edit picture', 'url_name': 'pict_edit'},
    {'button_name': 'Delete picture', 'url_name': 'pict_delete'},
]


class DataMixin:
    page_header = None
    single_element = False
    extra_context = {'mainmenu': mainmenu, 'forsinglemenu': forsinglemenu}

    def __init__(self):
        if self.page_header:
            self.extra_context['page_header'] = self.page_header

        self.extra_context['single_element'] = self.single_element

    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context
