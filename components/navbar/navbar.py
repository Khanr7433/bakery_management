from django_components import Component, register # type: ignore

@register("navbar")
class navbar(Component):
    template_name = "navbar.html"

    # def get_context_data(self, date):
    #     return {
    #         "date": date,
    #     }

    # class Media:
    #     css = "style.css"
    #     js = "script.js"