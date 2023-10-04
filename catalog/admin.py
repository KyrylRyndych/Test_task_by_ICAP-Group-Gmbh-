from django.contrib import admin
from .models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["name", "photo", "category", "top_sel_month", "in_stock", "self_delivery", "description", "price"]
    list_editable = ["photo", "category", "top_sel_month", "in_stock", "self_delivery", "price"]
    list_filter = ["category", "top_sel_month", "in_stock", "self_delivery"]

    @admin.display(ordering=["description1", "description2"])
    def description(self, obj: Goods):
        return f"#{obj.description1} #{obj.description2}"
