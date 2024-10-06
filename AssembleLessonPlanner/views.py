from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import (
    LessonPlan, InventoryItem, InventoryTransaction, MaterialPreparation, TeamMember
)
from .forms import (
    LessonPlanForm, InventoryItemForm, InventoryTransactionForm, MaterialPreparationFormSet
)
from django.contrib import messages

# Index view
def index(request):
    return render(request, 'index.html')

# Help page view
def help(request):
    return render(request, 'help.html')

# Lesson Plan Views
class LessonPlanListView(ListView):
    model = LessonPlan
    template_name = 'lessonplan_list.html'
    context_object_name = 'lessonplans'

class LessonPlanDetailView(DetailView):
    model = LessonPlan
    template_name = 'lessonplan_detail.html'
    context_object_name = 'lessonplan'

class LessonPlanCreateView(View):
    def get(self, request):
        form = LessonPlanForm()
        material_formset = MaterialPreparationFormSet()
        return render(request, 'lessonplan_form.html', {'form': form, 'material_formset': material_formset})

    def post(self, request):
        form = LessonPlanForm(request.POST)
        material_formset = MaterialPreparationFormSet(request.POST)
        if form.is_valid() and material_formset.is_valid():
            lesson_plan = form.save()
            material_formset.instance = lesson_plan
            material_formset.save()
            messages.success(request, 'Lesson plan created successfully.')
            return redirect('lessonplan_list')
        return render(request, 'lessonplan_form.html', {'form': form, 'material_formset': material_formset})

class LessonPlanUpdateView(View):
    def get(self, request, pk):
        lesson_plan = get_object_or_404(LessonPlan, pk=pk)
        form = LessonPlanForm(instance=lesson_plan)
        material_formset = MaterialPreparationFormSet(instance=lesson_plan)
        return render(request, 'lessonplan_form.html', {'form': form, 'material_formset': material_formset})

    def post(self, request, pk):
        lesson_plan = get_object_or_404(LessonPlan, pk=pk)
        form = LessonPlanForm(request.POST, instance=lesson_plan)
        material_formset = MaterialPreparationFormSet(request.POST, instance=lesson_plan)
        if form.is_valid() and material_formset.is_valid():
            lesson_plan = form.save()
            material_formset.instance = lesson_plan
            material_formset.save()
            messages.success(request, 'Lesson plan updated successfully.')
            return redirect('lessonplan_detail', pk=pk)
        return render(request, 'lessonplan_form.html', {'form': form, 'material_formset': material_formset})

class LessonPlanDeleteView(DeleteView):
    model = LessonPlan
    template_name = 'lessonplan_confirm_delete.html'
    success_url = reverse_lazy('lessonplan_list')

# Inventory Item Views
class InventoryItemListView(ListView):
    model = InventoryItem
    template_name = 'inventoryitem_list.html'
    context_object_name = 'inventoryitems'

class InventoryItemDetailView(DetailView):
    model = InventoryItem
    template_name = 'inventoryitem_detail.html'
    context_object_name = 'inventoryitem'

class InventoryItemCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventoryitem_form.html'
    success_url = reverse_lazy('inventoryitem_list')

class InventoryItemUpdateView(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventoryitem_form.html'
    success_url = reverse_lazy('inventoryitem_list')

class InventoryItemDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventoryitem_confirm_delete.html'
    success_url = reverse_lazy('inventoryitem_list')

# Inventory Transaction Views
def add_stock(request, item_id):
    inventory_item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        form = InventoryTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.inventory_item = inventory_item
            transaction.transaction_type = 'Added'
            transaction.save()
            messages.success(request, 'Stock added successfully.')
            return redirect('inventoryitem_detail', pk=item_id)
    else:
        form = InventoryTransactionForm()
    context = {'form': form, 'inventory_item': inventory_item}
    return render(request, 'add_stock.html', context)

def remove_stock(request, item_id):
    inventory_item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        form = InventoryTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.inventory_item = inventory_item
            transaction.transaction_type = 'Removed'
            transaction.save()
            messages.success(request, 'Stock removed successfully.')
            return redirect('inventoryitem_detail', pk=item_id)
    else:
        form = InventoryTransactionForm()
    context = {'form': form, 'inventory_item': inventory_item}
    return render(request, 'remove_stock.html', context)
