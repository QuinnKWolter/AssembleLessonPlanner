from django.db import models

PROGRAM_CHOICES = [
    ('After School Program', 'After School Program'),
    ('Summer Camp', 'Summer Camp'),
    ('Day Camp', 'Day Camp'),
    ('Weekend Workshops', 'Weekend Workshops'),
    ('Special Events', 'Special Events'),
    ('Outreach Programs', 'Outreach Programs'),
    ('Virtual Learning Sessions', 'Virtual Learning Sessions'),
    ('Holiday Camps', 'Holiday Camps'),
    ('STEAM Saturdays', 'STEAM Saturdays'),
]

CLASS_TIME_CHOICES = [
    ('Less than 30 minutes', 'Less than 30 minutes'),
    ('30 minutes to 1 hour', '30 minutes to 1 hour'),
    ('1-2 hours', '1-2 hours'),
    ('2-3 hours', '2-3 hours'),
    ('Full Day Session', 'Full Day Session'),
    ('Multi-Day Workshop', 'Multi-Day Workshop'),
]

AUDIENCE_GRADE_CHOICES = [
    ('Kindergarten', 'Kindergarten'),
    ('Grades 1-2', 'Grades 1-2'),
    ('Grades 3-5', 'Grades 3-5'),
    ('Grades 6-8', 'Grades 6-8'),
    ('Grades 9-12', 'Grades 9-12'),
    ('Mixed Grades', 'Mixed Grades'),
    ('Special Needs Groups', 'Special Needs Groups'),
]

CLASS_SIZE_CHOICES = [
    ('1-5 students', '1-5 students'),
    ('6-10 students', '6-10 students'),
    ('11-15 students', '11-15 students'),
    ('16-20 students', '16-20 students'),
    ('21-25 students', '21-25 students'),
    ('26-30 students', '26-30 students'),
    ('31+ students', '31+ students'),
]

USAGE_FREQUENCY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
]

CONDITION_STATUS_CHOICES = [
    ('New', 'New'),
    ('Good', 'Good'),
    ('Fair', 'Fair'),
    ('Needs Repair', 'Needs Repair'),
]

TASK_CHOICES = [
    ('Introduction and Warm-up Activities', 'Introduction and Warm-up Activities'),
    ('Lecture/Demonstration', 'Lecture/Demonstration'),
    ('Hands-on Experimentation', 'Hands-on Experimentation'),
    ('Group Projects', 'Group Projects'),
    ('Individual Assignments', 'Individual Assignments'),
    ('Arts and Crafts', 'Arts and Crafts'),
    ('Coding and Robotics', 'Coding and Robotics'),
    ('Field Exploration', 'Field Exploration'),
    ('Presentations', 'Presentations'),
    ('Reflection and Discussion', 'Reflection and Discussion'),
    ('Clean-up and Debrief', 'Clean-up and Debrief'),
]

TEAM_MEMBER_CHOICES = [
    ('Lead Instructor', 'Lead Instructor'),
    ('Assistant Instructor', 'Assistant Instructor'),
    ('Program Coordinator', 'Program Coordinator'),
    ('Volunteer', 'Volunteer'),
    ('Intern', 'Intern'),
    ('Guest Speaker', 'Guest Speaker'),
    ('Workshop Facilitator', 'Workshop Facilitator'),
    ('Curriculum Developer', 'Curriculum Developer'),
    ('Educational Technologist', 'Educational Technologist'),
]

USAGE_TYPE_CHOICES = [
    ('Added', 'Added'),
    ('Removed', 'Removed'),
    ('Adjusted', 'Adjusted'),
]

class Program(models.Model):
    name = models.CharField(max_length=200, choices=PROGRAM_CHOICES, unique=True)

    def __str__(self):
        return self.name


class AudienceGrade(models.Model):
    grade_level = models.CharField(max_length=50, choices=AUDIENCE_GRADE_CHOICES, unique=True)

    def __str__(self):
        return self.grade_level


class ClassSize(models.Model):
    size = models.CharField(max_length=50, choices=CLASS_SIZE_CHOICES, unique=True)

    def __str__(self):
        return self.size


class Task(models.Model):
    name = models.CharField(max_length=200, choices=TASK_CHOICES, unique=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices=TEAM_MEMBER_CHOICES)
    contact_info = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Partner(models.Model):
    name = models.CharField(max_length=200, unique=True)
    contact_info = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class SubjectArea(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class InstructionalMethod(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class AssessmentMethod(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField(blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200, unique=True)
    contact_phone = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    item_image = models.ImageField(upload_to='inventory_images/', blank=True, null=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    unit_of_measurement = models.CharField(max_length=50)
    minimum_stock_level = models.PositiveIntegerField(default=0)
    maximum_stock_level = models.PositiveIntegerField(blank=True, null=True)
    reorder_quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    storage_location = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.FileField(upload_to='inventory_attachments/', blank=True, null=True)

    def __str__(self):
        return self.name

    def total_stock_value(self):
        return self.quantity_in_stock * self.cost_per_unit


class LessonPlan(models.Model):
    title = models.CharField(max_length=200)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    class_time = models.CharField(max_length=50, choices=CLASS_TIME_CHOICES)
    audience_grade = models.ForeignKey(AudienceGrade, on_delete=models.SET_NULL, null=True)
    class_size = models.ForeignKey(ClassSize, on_delete=models.SET_NULL, null=True)
    subject_areas = models.ManyToManyField(SubjectArea)
    date_time = models.DateTimeField()
    duration = models.DurationField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    objectives = models.TextField(blank=True, null=True)
    state_common_core_standards = models.TextField(blank=True, null=True)
    themes = models.ManyToManyField(Theme, blank=True)
    lesson_overview = models.TextField(blank=True, null=True)
    assessment_methods = models.ManyToManyField(AssessmentMethod, blank=True)
    technology_requirements = models.TextField(blank=True, null=True)
    follow_up_activities = models.TextField(blank=True, null=True)
    vocabulary = models.TextField(blank=True, null=True)
    tasks = models.ManyToManyField(Task, blank=True)
    team_members = models.ManyToManyField(TeamMember, blank=True)
    partners = models.ManyToManyField(Partner, blank=True)
    materials_needed = models.ManyToManyField(InventoryItem, through='MaterialPreparation')

    def __str__(self):
        return self.title

class MaterialPreparation(models.Model):
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity_needed = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.inventory_item.name} for {self.lesson_plan.title}"


class InventoryTransaction(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=50, choices=USAGE_TYPE_CHOICES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.inventory_item.name} on {self.date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the quantity in stock
        if self.transaction_type == 'Added':
            self.inventory_item.quantity_in_stock += self.quantity
        elif self.transaction_type == 'Removed':
            self.inventory_item.quantity_in_stock -= self.quantity
        elif self.transaction_type == 'Adjusted':
            self.inventory_item.quantity_in_stock = self.quantity
        self.inventory_item.save()

