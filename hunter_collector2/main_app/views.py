from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hunter, Weapon, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'huntercollector'


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def hunters_index(request):
  hunters = Hunter.objects.filter(user=request.user)
  return render(request, 'hunters/index.html', { 'hunters': hunters })

@login_required
def hunters_detail(request, hunter_id):
  hunter = Hunter.objects.get(id=hunter_id)
  weapons_hunter_doesnt_have = Weapon.objects.exclude(id__in = hunter.weapons.all().values_list('id'))
  return render(request, 'hunters/detail.html', { 'hunter': hunter, 'weapons': weapons_hunter_doesnt_have
 })

@login_required
def assoc_weapon(request, hunter_id, weapon_id):
  # Note that you can pass a toy's id instead of the whole object
  Hunter.objects.get(id=hunter_id).weapons.add(weapon_id)
  return redirect('detail', hunter_id=hunter_id)

class HunterCreate(LoginRequiredMixin, CreateView):
  model = Hunter
  fields = ['name', 'rank', 'gender', 'favorite_meal']
  success_url = '/hunters/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

def add_photo(request, hunter_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, hunter_id=hunter_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', hunter_id=hunter_id)

class HunterUpdate(LoginRequiredMixin, UpdateView):
  model = Hunter
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'rank', 'favorite_meal']

class HunterDelete(LoginRequiredMixin, DeleteView):
  model = Hunter
  success_url = '/hunters/'

class WeaponList(LoginRequiredMixin, ListView):
  model = Weapon

class WeaponDetail(LoginRequiredMixin, DetailView):
  model = Weapon

class WeaponCreate(LoginRequiredMixin, CreateView):
  model = Weapon
  fields = '__all__'

class WeaponUpdate(LoginRequiredMixin, UpdateView):
  model = Weapon
  fields = ['name', 'type', 'rarity']

class WeaponDelete(LoginRequiredMixin, DeleteView):
  model = Weapon
  success_url = '/weapons/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

