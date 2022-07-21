from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', { 
  'bird': bird,
  'feeding_form': feeding_form,
  })

class BirdCreate(CreateView):
  model = Bird
  fields = '__all__'
  success_url = '/birds/'

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'

def add_feeding(request, bird_id):
   # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the bird_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('detail', bird_id=bird_id)