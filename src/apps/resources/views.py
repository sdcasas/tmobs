import json

from django.http import JsonResponse, Http404
from django.core.cache import cache


def get_redirect(request, key):
    url = cache.get(key)
    if url:
        data = {"key": key, "url": url}
        return JsonResponse(data)
    else:
        raise Http404(f"key: {key} does not exist.")