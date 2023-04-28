from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Musician,Album
from employee import forms

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction={'title':'Hello from the SQL DataBase learning','musician_list':musician_list}
    return render(request,'employee/index.html',context=diction)
def album_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    diction={'title':'List of Album','artist_info':artist_info}
    return render(request,'employee/album_list.html',context=diction)
def musician_form(request):
    form=forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':'Add Musician','MusicianForm':form}
    return render(request,'employee/musician_form.html',context=diction)
def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':'Add Album','AlbumForm':form}
    return render(request,'employee/album_form.html',context=diction)