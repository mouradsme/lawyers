from django.contrib import admin
from .models import Profile,Lawyer,SubscriptionPlan
from .models import Aff,  Seance,  conseil,  paiement, tribunal, decision,News
from .models import Documents, Profile,Lawyer,SubscriptionPlan,lawyerclients, notaryclients, nrdv, rdv
from .models import Aff,  Seance, conseil,  paiement, tribunal, decision

admin.site.register(Profile)
admin.site.register(Lawyer)
admin.site.register(lawyerclients)
admin.site.register(notaryclients)
admin.site.register(SubscriptionPlan)
admin.site.register(rdv)
admin.site.register(nrdv)
admin.site.register(conseil)
admin.site.register(tribunal)
admin.site.register(Aff)
admin.site.register(Seance)
admin.site.register(decision)
admin.site.register(paiement)
admin.site.register(News)
admin.site.register(Documents)