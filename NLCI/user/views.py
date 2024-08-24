from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member, Master
from .forms import MasterForm, DetailFormSet
# Create your views here.
def welcome(request):
    return HttpResponse("hello jupiter")
def first(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())
def members(request):
    mymembers=Member.objects.all().values()
    template= loader.get_template("allMembers.html")
    context={
        'myMembers':mymembers,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    template=loader.get_template("child.html")
    return HttpResponse(template.render())

from django.shortcuts import render, redirect
from .forms import EmpForm

def add_employee(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
           # return redirect('testing')  # Redirect to a success page or another view
    else:
        form = EmpForm()
    return render(request, 'addEmployee.html', {'form': form})
def master_detail_view(request, pk=None):
    if pk:
        master = get_object_or_404(Master, pk=pk)
    else:
        master = Master()

    if request.method == 'POST':
        master_form = MasterForm(request.POST, instance=master)
        detail_formset = DetailFormSet(request.POST, instance=master)

        if master_form.is_valid() and detail_formset.is_valid():
            master = master_form.save()
            detail_formset.save()
            return redirect('master-list')  # Replace with your view name
        else:
            master_form = MasterForm(instance=master)
            detail_formset = DetailFormSet(instance=master)

        return render(request, 'templates.html', {
            'master_form': master_form,
            'detail_formset': detail_formset,
        })