from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

from oat.domain.colors_token import ColorsToken

class GetColorToken(View):
    @login_required
    def get(self, request):
        now = datetime.now()
        user_id = request.user.id

        color_token = ColorsToken.objects.filter(user_id=user_id, date_start__lte=now, date_end__gt=now)
        return JsonResponse({
            "first_color": color_token.first_color,
            "second_color": color_token.second_color,
            "pattern": color_token.pattern,
            "date_start": color_token.date_start,
            "date_end": color_token.date_end
        })