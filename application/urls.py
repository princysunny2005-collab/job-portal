from django.urls import path
from application import views

urlpatterns = [
    path("",views.home,name="home"),
    path("category/",views.category,name="category"),
    path("find/",views.find,name="find"),
    path("career/",views.career,name="career"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("update/<int:pk>/",views.update,name="update"),
    path("profile/",views.profile,name="profile"),
    path("logout/",views.logout,name="logout")
    # path("regisetr_view",views.register_view,name="register_view")

]
