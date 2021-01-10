from django.contrib import admin
from .models import Storage
from .models import Company
from .models import storage_Number
from .models import type_of_Storage
from .models import storage_Valid

# Register your models here.
admin.site.register(Company)
admin.site.register(storage_Number)
admin.site.register(type_of_Storage)
admin.site.register(storage_Valid)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('company', 'Storage_Number', "Type_of_Storage", "Storage_Valid", "Remark", "Material_Seggregation",
                    "Barrication_in_Place",
                    "Seggregation_of_non_Valid_and_Damaged_Tools", "Housekeeping_issues", "SDS_in_Place",
                    "Materials_Stacked_Properly", "Water_Pounding_on_Floor", "canvas_cover_Without_Rain_Water", "date")
