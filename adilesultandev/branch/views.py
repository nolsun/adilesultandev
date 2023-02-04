from django.shortcuts import render,redirect
from .forms import BranchMonthlyDataForm
from .models import BranchMonthlyData
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.core.exceptions import PermissionDenied

def branchmonthlydata(request):
    if request.method =="POST":
        form=BranchMonthlyDataForm(request.POST)
        if form.is_valid():
            branchmonthlydatasave = BranchMonthlyData(
                branch_name = form.cleaned_data["branch_name"],
                person_name = form.cleaned_data["person_name"],
                email = form.cleaned_data["email"],
                re_email = form.cleaned_data["re_email"],
                
                yemeksepeti_fee = form.cleaned_data["yemeksepeti_fee"],
                getiryemek_fee = form.cleaned_data["getiryemek_fee"],
                trendyolyemek_fee = form.cleaned_data["trendyolyemek_fee"],
                creditcards_fee = form.cleaned_data["creditcards_fee"],
                foodcards_fee = form.cleaned_data["foodcards_fee"],
                
                branchdrink_expenses = form.cleaned_data["branchdrink_expenses"],
                branchayranyoghurt_expenses = form.cleaned_data["branchayranyoghurt_expenses"],
                branchbread_expenses = form.cleaned_data["branchbread_expenses"],
                branchkitchen_expenses = form.cleaned_data["branchkitchen_expenses"],
                branchconsumables_expenses = form.cleaned_data["branchconsumables_expenses"],
                branchutility_expenses = form.cleaned_data["branchutility_expenses"],
                branchrent_expenses = form.cleaned_data["branchrent_expenses"],
                branchinternet_expenses = form.cleaned_data["branchinternet_expenses"],
                
                manager_count = form.cleaned_data["manager_count"],
                manager_expenses = form.cleaned_data["manager_expenses"],
                staff_count = form.cleaned_data["staff_count"],
                staff_expenses = form.cleaned_data["staff_expenses"],
                courier_count = form.cleaned_data["courier_count"],
                courier_expenses = form.cleaned_data["courier_expenses"])
            if form.cleaned_data["email"]==form.cleaned_data["re_email"]:
                branchmonthlydatasave.save()
                messages.success(request,"Veriler başarıyla kaydedildi.")
                return redirect("index")
            else:
                messages.error(request,"Girilen mail adresleri birbiri ile eşleşmiyor!")
                return render(request,"branch/branchmonthlydata.html",{"form":form},)
        
    else:
        form=BranchMonthlyDataForm()
    return render(request,"branch/branchmonthlydata.html",{"form":form})