from django.urls import path, include
from .views import Login, Registration, MainPage, SurveyView, OneSurvey, Logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('login/', Login.as_view(), name='login'),
	path('registration/', Registration.as_view(), name='registration'),
    path('', login_required(MainPage.as_view()), name="main_page"),
    path('survey/<int:pk>', login_required(SurveyView.as_view()), name='survay'),
    path('survey_done/<int:pk>', login_required(OneSurvey.as_view()), name='one_survay'),
    path('logout/', Logout.as_view(), name='logout')
]
