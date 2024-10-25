from django_components import Component, register # type: ignore


@register("footer")
class footer(Component):
    template_name = "footer.html"
    
    def get_context_data(self, year):
        return {
            "year": year,
        }

    # class Media:
    #     css = "style.css"
    #     js = "script.js"