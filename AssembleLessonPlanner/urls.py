from django.urls import path
from . import views

urlpatterns = [
    # Index/Home page
    path('', views.index, name='index'),

    # Help page URL
    path('help/', views.help, name='help'),

    # Lesson Plan URLs
    path('lessonplans/', views.LessonPlanListView.as_view(), name='lessonplan_list'),
    path('lessonplans/create/', views.LessonPlanCreateView.as_view(), name='lessonplan_create'),
    path('lessonplans/<int:pk>/', views.LessonPlanDetailView.as_view(), name='lessonplan_detail'),
    path('lessonplans/<int:pk>/update/', views.LessonPlanUpdateView.as_view(), name='lessonplan_update'),
    path('lessonplans/<int:pk>/delete/', views.LessonPlanDeleteView.as_view(), name='lessonplan_delete'),

    # Inventory Item URLs
    path('inventoryitems/', views.InventoryItemListView.as_view(), name='inventoryitem_list'),
    path('inventoryitems/create/', views.InventoryItemCreateView.as_view(), name='inventoryitem_create'),
    path('inventoryitems/<int:pk>/', views.InventoryItemDetailView.as_view(), name='inventoryitem_detail'),
    path('inventoryitems/<int:pk>/update/', views.InventoryItemUpdateView.as_view(), name='inventoryitem_update'),
    path('inventoryitems/<int:pk>/delete/', views.InventoryItemDeleteView.as_view(), name='inventoryitem_delete'),

    # Additional URLs (e.g., for transactions)
    path('inventoryitems/<int:item_id>/add_stock/', views.add_stock, name='add_stock'),
    path('inventoryitems/<int:item_id>/remove_stock/', views.remove_stock, name='remove_stock'),
]