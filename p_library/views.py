from django.http import HttpResponse
from django.template import loader
from p_library.models import Friend


def collections(request):
    template = loader.get_template('library.html')
    friends = Friend.objects.all()
    data = {
        "friends": friends,
    }
    return HttpResponse(template.render(data, request))