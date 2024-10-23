from django_components import Component, register # type: ignore

@register("footer")
class footer(Component):
    template_name = "footer.html"

    # def get_context_data(self, date):
    #     return {
    #         "date": date,
    #     }

    # class Media:
    #     css = "style.css"
    #     js = "script.js"