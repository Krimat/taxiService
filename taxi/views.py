from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets

from .forms import CarForm, CarSearchForm
from .models import Driver, Car, Manufacturer
from .serializers import DriverSerializer

DENIED_PERMISSION_MESSAGE = "You need to have admin status to view this page"


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 2


class ManufacturerCreateView(generic.CreateView):
    model = Manufacturer
    context_object_name = "form"
    fields = ["name", "country"]
    template_name = "taxi/manufacturer_form.html"

    def get_success_url(self):
        return reverse_lazy("taxi:manufacturer-detail", kwargs={"pk":self.object.id})


class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
    template_name = "taxi/manufacturer_detail.html"


class ManufacturerUpdateView(generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"

    def get_success_url(self):
        return reverse_lazy("taxi:manufacturer-detail", kwargs={"pk": self.object.id})


class ManufacturerDeleteView(generic.DetailView):
    model = Manufacturer


class CarListView(generic.ListView):
    model = Car
    paginate_by = 2
    queryset = Car.objects.all().select_related("manufacturer")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = CarSearchForm()

        return context

    def get_queryset(self):
        name = self.request.GET.get('name')

        if name:
            return self.queryset.filter(model__icontains=name)

        return self.queryset


class CarDetailView(generic.DetailView):
    model = Car


def car_create_view(request):
    if request.method == "POST":
        car_form = CarForm(request.POST)

        car = None
        if car_form.is_valid():
            car = Car.objects.create(**car_form.cleaned_data)
            car.drivers.add(request.user)
        else:
            return render(
                request=request,
                template_name="taxi/car_form.html",
                context={"error": True, "form": car_form},
            )
        if car:
            return redirect(reverse_lazy("taxi:car-detail", kwargs={"pk":car.id}))
        else:
            return HttpResponse(status=501)

    elif request.method == "GET":
        return render(
            request=request,
            template_name="taxi/car_form.html",
            context={"form": CarForm()},
        )


class CarUpdateView(generic.UpdateView):
    model = Car
    template_name = "taxi/car_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("taxi:car-detail", kwargs={"pk": self.object.id})


class CarDeleteView(generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 2
    queryset = Driver.objects.filter(is_staff=False)


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'taxi.admin'
    permission_denied_message = DENIED_PERMISSION_MESSAGE

    model = Driver
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"

    def get_success_url(self):
        return reverse_lazy("taxi:car-detail", kwargs={"pk": self.object.id})


class DriverUpdateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'taxi.change_driver'
    permission_denied_message = DENIED_PERMISSION_MESSAGE

    model = Driver
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"

    def get_success_url(self):
        return reverse_lazy("taxi:car-detail", kwargs={"pk": self.object.id})


class DriverDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'taxi.delete_driver'
    permission_denied_message = DENIED_PERMISSION_MESSAGE

    model = Driver
    success_url = reverse_lazy("taxi:driver-list")


# API Views

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


