from django.shortcuts import render,redirect
from .models import CenterCommentData
from django.contrib import messages
from .forms import CenterCommentDataForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.core.exceptions import PermissionDenied

def centercommentdata(request):
    if request.method =="POST":
        form=CenterCommentDataForm(request.POST)
        if form.is_valid():
            centercommentdatasave = CenterCommentData(
                total_comment = form.cleaned_data["total_comment"],
                total_negative_comment = form.cleaned_data["total_negative_comment"],
                total_center_negative_comment = form.cleaned_data["total_center_negative_comment"],
                total_branch_negative_comment = form.cleaned_data["total_branch_negative_comment"],
                spice_problems = form.cleaned_data["spice_problems"],
                price_problems = form.cleaned_data["price_problems"],
                portion_problems = form.cleaned_data["portion_problems"],
                chicken_skin_problems = form.cleaned_data["chicken_skin_problems"],
                fabrication_problems = form.cleaned_data["fabrication_problems"],
                vegatables_problems = form.cleaned_data["vegatables_problems"],
                foodcard_problems = form.cleaned_data["foodcard_problems"],
                chicken_unbaked_problems = form.cleaned_data["chicken_unbaked_problems"],
                stuffed_unbaked_problems = form.cleaned_data["stuffed_unbaked_problems"],
                sickness_problems = form.cleaned_data["sickness_problems"],
                package_fall_problems = form.cleaned_data["package_fall_problems"],
                meat_crackling_problems = form.cleaned_data["meat_crackling_problems"],
                salt_problems = form.cleaned_data["salt_problems"],
                oil_problems = form.cleaned_data["oil_problems"],
                fermantation_problems = form.cleaned_data["fermantation_problems"],
                cold_service_problems = form.cleaned_data["cold_service_problems"],
                forgot_problems = form.cleaned_data["forgot_problems"],
                late_problems = form.cleaned_data["late_problems"],
                note_problems = form.cleaned_data["note_problems"],
                bread_set_problems = form.cleaned_data["bread_set_problems"],
                courier_problems = form.cleaned_data["courier_problems"],
                receipt_problems = form.cleaned_data["receipt_problems"])
            
            centercommentdatasave.save()
            messages.success(request,"Yorum analizi başarıyla kaydedildi.")
            return redirect("index")
    else:
        form=CenterCommentDataForm()
    return render(request,"center/centercommentdata.html",{"form":form})