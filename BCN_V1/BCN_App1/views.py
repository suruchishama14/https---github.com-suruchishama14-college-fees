from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from num2words import num2words
from .forms import *


# Create your views here.


def handler404(request, exception):
    context = {}
    return render(request, "errors/404.html", context=context)


def handler500(request):
    context = {}
    return render(request, "errors/500.html", context=context)


def home(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def add_student_fees(request):
    add_stud_fees = StudentFeeDetailsForm(request.POST)
    if add_stud_fees.is_valid():
        add_stud_fees.save()
        return redirect('add_student_fees')
    else:
        context = {"add_stud_fees": add_stud_fees}
        return render(request, 'add_student.html', context)


@login_required(login_url='/accounts/login/')
def fees_transactions(request):
    shows = FeesTransaction.objects.all().order_by('-dos')
    return render(request, 'show.html', {'shows': shows})


def search(request):
    if request.method == 'POST':
        srch = request.POST['search']

        if srch:
            match = StudentFeeDetails.objects.filter(Q(student_name__istartswith=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                messages.error(request, "Not in Student's Record")
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')


@login_required(login_url='/accounts/login/')
def alldetail(request):
    context = {}
    fid = request.GET['fid']
    obj = StudentFeeDetails.objects.get(id=fid)
    context['show'] = obj
    return render(request, 'details.html', context)


@login_required(login_url='/accounts/login/')
def details(request, ):
    context = {}
    fid = request.GET['fid']
    obj = StudentFeeDetails.objects.get(id=fid)
    context['show'] = obj
    return render(request, 'printing.html', context)


@login_required(login_url='/accounts/login/')
def post_edit(request, pk=None):
    post = get_object_or_404(StudentFeeDetails, pk=pk)
    if request.method == "POST":
        form = StudentFeeDetailsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentFeeDetailsForm(instance=post)

    return render(request, 'student_update.html', {'form': form, 'post': post})


@login_required(login_url='/accounts/login/')
def fees_data(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        fathers_name = request.POST['fathers_name']
        year = request.POST['year']
        email = request.POST['email']
        fee_type = request.POST['fee_type']
        fees_amount = request.POST['fees_amount']
        FeesTransaction.objects.create(
            student_name=student_name,
            fathers_name=fathers_name,
            year=year,
            email=email,
            fee_type=fee_type,
            fees_amount=fees_amount,
        )
        return redirect('fees_transactions')


@login_required(login_url='/accounts/login/')
def fees_up(request, pk=None):
    post = get_object_or_404(StudentFeeDetails, pk=pk)
    if request.method == "POST":
        form = StudentFeeDetailsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("fees_transactions")
    else:
        form = StudentFeeDetailsForm(instance=post)

    return render(request, 'student_fees.html', {'form': form, 'post': post})


def st_name(request):
    if 'term' in request.GET:
        qs = StudentFeeDetails.objects.filter(student_name__icontains=request.GET.get('term'))
        st_names = list()
        for student_names in qs:
            st_names.append(student_names.student_name)
        return JsonResponse(st_names, safe=False)
    return render(request, 'index.html')


def update_data(request, pk=None):
    post = get_object_or_404(StudentFeeDetails, pk=pk)
    if request.method == 'POST':
        try:
            f_cp = request.POST.get('f_cp')
            f_b = request.POST.get('f_b')
            s_cp = request.POST.get('s_cp')
            s_b = request.POST.get('s_b')
            t_cp = request.POST.get('t_cp')
            t_b = request.POST.get('t_b')
            fo_cp = request.POST.get('fo_cp')
            fo_b = request.POST.get('fo_b')

            obj = StudentFeeDetails.objects.get(id=pk)
            obj.f_balance = f_b
            obj.f_currently_paid = f_cp
            obj.s_balance = s_b
            obj.s_currently_paid = s_cp
            obj.t_balance = t_b
            obj.t_currently_paid = t_cp
            obj.fo_balance = fo_b
            obj.fo_currently_paid = fo_cp
            obj.save()
        except IntegrityError as e:
            e = "Saved Successfully"
            return redirect('fees_transactions')
    else:
        return render(request, 'student_fees.html', {'post': post})
