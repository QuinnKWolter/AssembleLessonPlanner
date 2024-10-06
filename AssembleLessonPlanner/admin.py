from django.contrib import admin
from .models import (
    Program, AudienceGrade, ClassSize, Task, TeamMember, Partner,
    SubjectArea, InstructionalMethod, AssessmentMethod, Theme, Location,
    Supplier, Category, InventoryItem, LessonPlan, MaterialPreparation,
    InventoryTransaction
)

# Inline for MaterialPreparation in LessonPlanAdmin
class MaterialPreparationInline(admin.TabularInline):
    model = MaterialPreparation
    extra = 1

# LessonPlan Admin
@admin.register(LessonPlan)
class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'program', 'date_time')
    list_filter = ('program', 'date_time')
    search_fields = ('title',)
    inlines = [MaterialPreparationInline]

# InventoryItem Admin
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity_in_stock', 'category', 'supplier')
    list_filter = ('category', 'supplier')
    search_fields = ('name', 'inventory_id')

# Registering other models
admin.site.register(Program)
admin.site.register(AudienceGrade)
admin.site.register(ClassSize)
admin.site.register(Task)
admin.site.register(TeamMember)
admin.site.register(Partner)
admin.site.register(SubjectArea)
admin.site.register(InstructionalMethod)
admin.site.register(AssessmentMethod)
admin.site.register(Theme)
admin.site.register(Location)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(MaterialPreparation)
admin.site.register(InventoryTransaction)
