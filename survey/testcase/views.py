from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from .models import Question, Answer, Option, Survey, SurveysDone

class Login(View):
    template = 'registration/login.html'

    def get(self, request):
        context = {
            'login_form': LoginForm()
        }
        return render(request, self.template, context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('login')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            try:
                login(request, user)
            except:
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')
        else:
            context = {
                'login_form': LoginForm(),
                'error': login_form.errors
            }
        return render(request, self.template, context)


class Registration(View):
    template = "registration/registration.html"

    def get(self, request):
        context = {
            'registration_form': RegistrationForm()
        }
        return render(request, self.template, context)

    def post(self, request):
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect('/login')
        else:
            context = {
                'registration_form': RegistrationForm(),
                'error': reg_form.errors
            }
            return render(request, self.template, context)


class MainPage(View):
    template = "index.html"

    def get(self, request):
        surveys = Survey.objects.filter(relevant=True)
        if request.user.is_superuser:
            surveys_done = SurveysDone.objects.all()
        else:
            surveys_done = SurveysDone.objects.filter(user=request.user)
        context = {
            'surveys': surveys,
            'surveys_done': surveys_done
        }
        return render(request, self.template, context)

    def post(self, request):
        pass

class SurveyView(View):
    template = "survey/survey.html"

    def get(self, request, pk):
        survey_list = []
        questions = Question.objects.filter(relevant=True, survey__relevant=True, survey=pk)
        for question in questions:
            options = Option.objects.filter(question=question)
            survey_list.append((question, options))
        context = {
            'survey_list': survey_list,
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken')
        survey_instance = Survey.objects.get(id=pk)
        survey_done = SurveysDone(user=request.user, survey=survey_instance)
        survey_done.save()
        for i in data:
            answer = Answer(user=request.user, question=Question.objects.get(id=i), answer=data[i], survey_done=survey_done)
            answer.save()

        return HttpResponseRedirect('/')

class OneSurvey(View):
    template = "survey/one_survey.html"

    def get(self, request, pk):
        answers = Answer.objects.filter(user=request.user, survey_done=pk)
        context = {
            'answers': answers
        }
        return render(request, self.template, context)

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
