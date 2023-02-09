from django.urls import path
from .views import *
urlpatterns=[
    path('home/',home),
    path('supreg/',supclass),
    path('suplog/',suplogclass),
    path('suppro/',supprofile),
    path('addmat/', matclass),
    path('dismat/', dismat),
    path('userdispro/',userdispro),
    path('matdel/<int:id>',matdelete),
    path('supeditpro/<int:id>',matedit),
    path('supdis/', regsupdis),
    path('userpro/', userprofile),
    path('userreg/', userregclass),
    path('userlog/', userlogclass),
    path('viewuserpro/', userpro),
    path('buynow/<int:id>',buynow),
    # path('final/<int:id>',finalclass),
    path('edituserprofile/<int:id>',edituserprofile),
    path('userdel/<int:id>',userprofiledel),
    path('wishlist/<int:id>',wishlist),
    path('wishdis/',wishdis),
    path('addmac/',macclass),
    path('dismac/',dismac),
    path('supprodis/',supprofiledis),
    path('supprofileedit/<int:id>',supprofiledit),
    path('supprofiledel/<int:id>',supprofiledel),
    path('confirmorder/',confirm),
    path('viewbookedpro/',viewbookedpro),
    path('confirmmessage/<int:id>',confirmessage),
    path('macdisall/',disallmac),
    path('messagealert/',messagealert),
    path('macedit/<int:id>',editmac),
    path('macdel/<int:id>',macdel),
    path('viewdetails/',viewdetails),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path('wishlistalert/',wishlistalert)



]