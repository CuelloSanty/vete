from django.contrib import admin
from appVete.models import Proveedore, Articulo, Cliente, Mascota, Atencione, ArticuloAtencion, Empleado, Adelanto,Venta, DetalleVenta, Pedido, DetallePedido

# Register your models here.
class ProveedoresAdmin(admin.ModelAdmin):
    model = Proveedore

class ArticulosAdmin(admin.ModelAdmin):
    model = Articulo

class ClienteAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'direccion', 'telefono', 'email')
    search_fields = ('nombre', 'email')

class MascotasAdmin(admin.ModelAdmin):
    model = Mascota


# [Atencion] [Open]
class AtencionInline(admin.TabularInline):
    model = ArticuloAtencion
        

class AtencionesAdmin(admin.ModelAdmin):
    inlines = [AtencionInline]
    
# [Atencion] [Close]


# Empleados [Open]
class AdelantoInline(admin.TabularInline):
    model = Adelanto

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [AdelantoInline]
# Empleados [Close]



# [Ventas] [Open]
class DetallesVentaInline(admin.TabularInline):
   model = DetalleVenta

class VentasAdmin(admin.ModelAdmin):
   inlines = [DetallesVentaInline]
# [Ventas] [Close]


class DetallesComprasInline(admin.TabularInline):
    model = DetallePedido

class PedidosAdmin(admin.ModelAdmin):
    inlines = [
        DetallesComprasInline,
    ]

admin.site.register(Proveedore, ProveedoresAdmin)

admin.site.register(Articulo, ArticulosAdmin) 

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Mascota, MascotasAdmin)

admin.site.register(Atencione, AtencionesAdmin)

admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(Venta, VentasAdmin)

admin.site.register(Pedido, PedidosAdmin)