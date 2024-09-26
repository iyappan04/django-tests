from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from .models import Groups

class SubdomainMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host().split('.')
        if len(host) > 2:  
            subdomain = host[0]
            try:
                request.group = Groups.objects.get(subdomain=subdomain)
            except Campus.DoesNotExist:
                request.group = None
        else:
            request.campus = None
