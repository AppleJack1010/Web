from main.models import Category
def base_template(request):
    is_htmx = request.headers.get("HX-Request") == "true"
    is_history_restore = request.headers.get("HX-History-Restore-Request") == "true"
    return {
       "base_template": "main/partial.html" if is_htmx and not is_history_restore else "main/base.html"
    }

from main.models import Category  # поправь импорт под свою модель

def categories(request):
    return {"categories": Category.objects.all()}