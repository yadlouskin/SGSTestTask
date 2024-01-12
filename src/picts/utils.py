from colorthief import ColorThief
from PIL import Image


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


class AutofillMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        pict = obj.pict
        color_thief = ColorThief(pict.file)
        dominant_color = color_thief.get_color(quality=1)
        palette = color_thief.get_palette(color_count=8, quality=1)
        img = Image.open(pict.file)
        img = img.convert("RGB")
        img = img.resize((1, 1), resample=0)
        average_color = img.getpixel((0, 0))

        def hex_color(r, g, b): return f'#{r:0>2x}{g:0>2x}{b:0>2x}'
        obj.size = f'({pict.width}, {pict.height})'
        obj.average_color = hex_color(*average_color)
        obj.main_color = hex_color(*dominant_color)
        obj.color_palette = '(' + \
            ', '.join([hex_color(*rbg) for rbg in palette]) + ')'
        obj.author = self.request.user
        return super().form_valid(form)
