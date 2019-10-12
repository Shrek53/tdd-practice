from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lists/home.html')

    def post(self, request, *args, **kwargs):
        item_text = request.POST.get('item_text')
        context = {
            'new_item_text': item_text
        }
        return render(request, 'lists/home.html', context=context)

# def home_page(request):
#     return render(request, 'lists/home.html')
