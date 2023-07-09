
from django.contrib import admin
from django.urls import path
from . import view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.upload,name="upload"),
    path('model/',view.result,name="knn"),
    path('result/',view.result1,name="result"),
    path('Decision/',view.Decision,name="Decision"),
    path('naivebayes/',view.naivebayes,name="naivebayes"),
    path('logisticreg/',view.logisticreg,name="logisticreg"),
    path('linearreg/',view.linearreg,name="linearreg"),
    path('MLPClassifier/',view.MLPClassifier,name="MLPClassifier"),
    path('SVC_Classifier/',view.SVC_Classifier,name="SVC_Classifier"),
    path('DecisionTreeREG/',view.DecisionTreeREG,name="DecisionTreeREG"),
    path('kmeans/',view.kmeans,name="kmeans"),
    path('home/',view.home,name='home'),

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'MLGraphX.view.error_404'
handler500 = 'MLGraphX.view.error_500'