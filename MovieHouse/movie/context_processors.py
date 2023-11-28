from movie.models import Language
def links(request):
    link=Language.objects.all()
    return {'links':link}