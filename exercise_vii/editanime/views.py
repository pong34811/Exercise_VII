from django.shortcuts import redirect, render

from .models import Animal_list



# Create your views here.

def homepage(request):
    animes = Animal_list.objects.all()
    return render(request, 'index.html', {"animes": animes})

# def editanimelist(request):
#     return render(request, 'editanime.html')

def editanimelist(request, animal_id):
    anime = Animal_list.objects.get(id=animal_id)
    if request.method == 'POST':
        # Get the updated data from the form
        anime_order = request.POST.get('anime_order')
        anime_name_th = request.POST.get('anime_name_th')
        anime_name_en = request.POST.get('anime_name_en')
        anime_seasons = request.POST.get('anime_seasons')
        anime_channel = request.POST.get('anime_channel')

        # Update the existing anime object
        anime.anime_order = anime_order
        anime.anime_name_th = anime_name_th
        anime.anime_name_en = anime_name_en
        anime.anime_seasons = anime_seasons
        anime.anime_channel = anime_channel
        anime.save()

        # Redirect to the homepage or another appropriate page
        return redirect('/')

    else:
        # If it's a GET request, display the edit form
        return render(request, "editanime.html", {"anime": anime})

   


