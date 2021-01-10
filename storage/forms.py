from django import forms
from .models import Storage, storage_Valid, type_of_Storage, storage_Number, Company


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('company', 'Storage_Number', "Type_of_Storage", "Storage_Valid", "Remark", "Material_Seggregation",
                  "Barrication_in_Place",
                  "Seggregation_of_non_Valid_and_Damaged_Tools", "Housekeeping_issues", "SDS_in_Place",
                  "Materials_Stacked_Properly", "Water_Pounding_on_Floor", "canvas_cover_Without_Rain_Water",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Storage_Valid'].queryset = storage_Valid.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Type_of_Storage'].queryset = type_of_Storage.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Storage_Number'].queryset = storage_Number.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.none()
