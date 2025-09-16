from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


def index(request):
    return HttpResponse(
        """
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Apartment Management API</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Arial, sans-serif; margin: 40px; color: #222; }
    h1 { margin-bottom: 0; }
    p { margin-top: 8px; color: #555; }
    ul { line-height: 1.9; }
    a { color: #0b69ff; text-decoration: none; }
    a:hover { text-decoration: underline; }
    code { background: #f4f4f5; padding: 2px 6px; border-radius: 4px; }
    .card { border: 1px solid #eee; border-radius: 8px; padding: 16px 20px; max-width: 720px; }
  </style>
  <link rel=\"icon\" href=\"data:,\">
  </head>
<body>
  <div class=\"card\">
    <h1>Apartment Management API</h1>
    <p>Welcome. Explore the API endpoints below.</p>
    <ul>
      <li><a href=\"/admin/\">/admin/</a></li>
      <li><a href=\"/api/auth/\">/api/auth/</a></li>
      <li><a href=\"/api/apartments/\">/api/apartments/</a></li>
      <li><a href=\"/api/payments/\">/api/payments/</a></li>
      <li><a href=\"/api/notices/\">/api/notices/</a></li>
      <li><a href=\"/api/maintenance/\">/api/maintenance/</a></li>
    </ul>
    <p>Use JWT auth for protected endpoints. Start at <code>/api/auth/login/</code>.</p>
  </div>
</body>
</html>
        """,
        content_type="text/html; charset=utf-8",
    )

class AdminOnlySpectacularAPIView(SpectacularAPIView):
    permission_classes = [AllowAny]


class AdminOnlySwaggerView(SpectacularSwaggerView):
    permission_classes = [AllowAny]


class AdminOnlyRedocView(SpectacularRedocView):
    permission_classes = [AllowAny]


