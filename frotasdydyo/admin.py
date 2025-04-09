from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Veiculo, Kilometragem, Horario, Condutor, Data

admin.site.register(Veiculo)
admin.site.register(Kilometragem)
admin.site.register(Horario)
admin.site.register(Condutor)
admin.site.register(Data)
