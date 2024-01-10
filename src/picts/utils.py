mainmenu = [
    {'button_name':'Main page', 'url_name':'main_page'},
    {'button_name':'Add picture', 'url_name':'pict_add'},
]

class DataMixin:
    page_header = None
    extra_context = {'mainmenu':mainmenu}

    def __init__(self):
        if self.page_header:
            self.extra_context['page_header'] = self.page_header

    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context
