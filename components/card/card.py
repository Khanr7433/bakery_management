from django_components import Component, register # type: ignore

@register("card")
class card(Component):
    template_name = "card.html"

    # def get_context_data(self, date):
    #     return {
    #         "date": date,
    #     }

    # class Media:
    #     css = "style.css"
    #     js = "script.js"