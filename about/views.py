from django.shortcuts import render

# Create your views here.
def main(request):
	return render(request, 'about/index.html', context={
		'name': 'kostya',
		})