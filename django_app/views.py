from django.http import HttpResponse
import socket

def home(request):
    hostname = socket.gethostname()
    return HttpResponse(
        f"<h1>Hello from Django on Kubernetes!</h1>"
        f"<p><strong>Pod hostname:</strong> {hostname}</p>"
        f"<p>Это доказывает балансировку нагрузки между репликами</p>"
    )

def health(request):
    return HttpResponse("OK")
