from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class storage_Number(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class type_of_Storage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Storage_Number = models.ForeignKey(storage_Number, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class storage_Valid(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Storage_Number = models.ForeignKey(storage_Number, on_delete=models.CASCADE)
    Type_of_Storage = models.ForeignKey(type_of_Storage, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Storage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    Storage_Number = models.ForeignKey(storage_Number, on_delete=models.SET_NULL, null=True)
    Type_of_Storage = models.ForeignKey(type_of_Storage, on_delete=models.SET_NULL, null=True)
    Storage_Valid = models.ForeignKey(storage_Valid, on_delete=models.SET_NULL, null=True)
    Remark = models.TextField(max_length=100, blank=True)
    Material_Seggregation = models.BooleanField(null=True)
    Barrication_in_Place = models.BooleanField(null=True)
    Seggregation_of_non_Valid_and_Damaged_Tools = models.BooleanField(null=True)
    Housekeeping_issues = models.BooleanField(null=True)
    SDS_in_Place = models.BooleanField(null=True)
    Materials_Stacked_Properly = models.BooleanField(null=True)
    Water_Pounding_on_Floor = models.BooleanField(null=True)
    canvas_cover_Without_Rain_Water = models.BooleanField(null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.company
