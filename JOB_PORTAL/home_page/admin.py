from django.contrib import admin
from home_page.models import Comsingup
from home_page.models import Candidatesingup
from home_page.models import Candidatelogin
from home_page.models import Comlogin

admin.site.register(Comsingup)
admin.site.register(Comlogin)
admin.site.register(Candidatelogin)
admin.site.register(Candidatesingup)