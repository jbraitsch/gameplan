from django.db import models
from django.urls import reverse
from django import forms
CITIES = (
    ('Colorado Springs', 'Colorado Springs'),
    ('Denver', 'Denver'),
    ('Fort Collins', 'Fort Collins'))


class Business(models.Model):
    ACTIVE = ((True,'True'), (False,'False'))
    name = models.CharField("Name", max_length=200)
    email = models.CharField("Email", max_length=200)
    city = models.CharField("Location", choices=CITIES, max_length=200)
    address = models.CharField("Address", max_length=200)
    phone_number = models.CharField("Phone", max_length=10)
    is_open = models.BooleanField("Open", default=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('business-detail', args=[str(self.id)])

'''
class Customer(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    city = models.CharField(max_length=200, choices = CITIES)
    home_base = models.OneToOneField(Business, on_delete=models.CASCADE, unique=True, blank = True)
    

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    portfolio = models.ForeignKey(Business, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

"""
# Model to represent the relationship between projects and portfolios.
# Each instance of this model will have a reference to a Portfolio and a Project,
# creating a many-to-many relationship between portfolios and projects. T
class ProjectsInPortfolio(models.Model):

    #deleting a portfolio will delete associate projects
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    #deleting a project will not affect the portfolio
    #Just the entry will be removed from this table
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        #ensures that each project is associated with only one portfolio
        constraints = [
            models.UniqueConstraint(fields=["project"],
                name="unique project"
            )
        ]
"""
'''