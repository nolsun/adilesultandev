from django.db import models

class BranchMonthlyData(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    branch_name = models.CharField(verbose_name="Şubeniz",max_length=100, null=True)
    person_name = models.CharField(verbose_name="Adınız Soyadınız",max_length=100)
    email = models.CharField(verbose_name="E-Posta Adresiniz",max_length=100)
    re_email = models.CharField(verbose_name="Tekrar E-Posta Adresiniz",max_length=100, null=True)

    yemeksepeti_fee             = models.DecimalField(verbose_name="YemekSepeti Komisyon Tutarı", decimal_places=2, max_digits=10, null=True)
    getiryemek_fee              = models.DecimalField(verbose_name="GetirYemek Komisyon Tutarı", decimal_places=2, max_digits=10, null=True)
    trendyolyemek_fee           = models.DecimalField(verbose_name="TrendyolYemek Komisyon Tutarı", decimal_places=2, max_digits=10, null=True)
    creditcards_fee             = models.DecimalField(verbose_name="Kredi Kartları Komisyon Tutarı", decimal_places=2, max_digits=10, null=True)
    foodcards_fee               = models.DecimalField(verbose_name="Yemek Kartları Komisyon Tutarı", decimal_places=2, max_digits=10, null=True)

    branchdrink_expenses        = models.DecimalField(verbose_name="Meşrubat Giderleri", decimal_places=2, max_digits=10, null=True)
    branchayranyoghurt_expenses = models.DecimalField(verbose_name="Ayran ve Yoğurt Giderleri", decimal_places=2, max_digits=10, null=True)
    branchbread_expenses        = models.DecimalField(verbose_name="Ekmek Giderleri", decimal_places=2, max_digits=10, null=True)
    branchkitchen_expenses      = models.DecimalField(verbose_name="Şube İçi Mutfak Giderleri", decimal_places=2, max_digits=10, null=True)
    branchconsumables_expenses  = models.DecimalField(verbose_name="Şube İçi Sarf Kullanım", decimal_places=2, max_digits=10, null=True)
    branchutility_expenses      = models.DecimalField(verbose_name="Elektrik, Su, Doğalgaz", decimal_places=2, max_digits=10, null=True)
    branchrent_expenses         = models.DecimalField(verbose_name="Kira ve Stopaj Toplamı", decimal_places=2, max_digits=10, null=True)
    branchinternet_expenses     = models.DecimalField(verbose_name="Telefon, İnternet, Muhasebe vb.", decimal_places=2, max_digits=10, null=True)

    manager_count               = models.DecimalField(verbose_name="Yönetici Personel Kişi Sayısı", decimal_places=2, max_digits=10, null=True)
    manager_expenses            = models.DecimalField(verbose_name="Yönetici Personel Giderleri", decimal_places=2, max_digits=10, null=True)
    staff_count                 = models.DecimalField(verbose_name="İç Personel Kişi Sayısı", decimal_places=2, max_digits=10, null=True)
    staff_expenses              = models.DecimalField(verbose_name="İç Personel Giderleri", decimal_places=2, max_digits=10, null=True)
    courier_count               = models.DecimalField(verbose_name="Kurye Kişi Sayısı", decimal_places=2, max_digits=10, null=True)
    courier_expenses            = models.DecimalField(verbose_name="Motor ve Kurye Giderleri", decimal_places=2, max_digits=10, null=True)