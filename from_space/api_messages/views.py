from .models import Message
from django.http import JsonResponse


def get_messages(request):
    if request.GET.get('last_id'):
        last_id = request.GET.get('last_id')
    else:
        return JsonResponse([], safe=False)

    response = Message.get_latest(last_id)

    return JsonResponse(response, safe=False)


def mark_read(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
    else:
        print(1)
        return JsonResponse({'answer': 'ERR'}, safe=False)
    try:
        Message.objects.get(id=id)
        item = Message.objects.get(id=id)
        item.is_read = True
        item.save()
    except:
        print(2)
        return JsonResponse({'answer': 'ERR'}, safe=False)

    return JsonResponse({'answer': 'OK'}, safe=False)
