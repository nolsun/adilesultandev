from django import forms
from .models import BranchMonthlyData

BRANCHCHOICES=[
        ('',''),
        ('Ataşehir (Atatürk Mah.) Toplam', 'Ataşehir (Atatürk Mah.)'),
        ('Ataşehir (Küçükbakkalköy Mah.) Toplam', 'Ataşehir (Küçükbakkalköy Mah.)'),
        ('Bağcılar (Mahmutbey Mah.) Toplam', 'Bağcılar (Mahmutbey Mah.)'),
        ('Bahçelievler (Siyavuşpaşa Mah. - Yayla) Toplam', 'Bahçelievler (Siyavuşpaşa Mah. - Yayla)'),
        ('Bakırköy (Zuhuratbaba Mah.) Toplam', 'Bakırköy (Zuhuratbaba Mah.)'),
        ('Başakşehir (Kayabaşı Mah.) Toplam', 'Başakşehir (Kayabaşı Mah.)'),
        ('Beşiktaş (Gayrettepe Mah.) Toplam', 'Beşiktaş (Gayrettepe Mah.)'),
        ('Beylikdüzü (Adnan Kahveci Mah.) Toplam', 'Beylikdüzü (Adnan Kahveci Mah.)'),
        ('Çekmeköy (Mehmet Akif Mah.) Toplam', 'Çekmeköy (Mehmet Akif Mah.)'),
        ('Esenyurt (Aşık Veysel Mah.) Toplam', 'Esenyurt (Aşık Veysel Mah.)'),
        ('Esenyurt (Güzelyurt Mah.) Toplam', 'Esenyurt (Güzelyurt Mah.)'),
        ('Fatih (Yavuz Sultan Selim Mah.) Toplam', 'Fatih (Yavuz Sultan Selim Mah.)'),
        ('Fatih (Silivrikapı Mah.) Toplam', 'Fatih (Silivrikapı Mah.)'),
        ('Güngören (A. Nafiz Gürman Mah.) Toplam', 'Güngören (A. Nafiz Gürman Mah.)'),
        ('Kadıköy (Acıbadem Mah.) Toplam', 'Kadıköy (Acıbadem Mah.)'),
        ('Kadıköy (Feneryolu Mah.) Toplam', 'Kadıköy (Feneryolu Mah.)'),
        ('Kadıköy (Fikirtepe Mah.) Toplam', 'Kadıköy (Fikirtepe Mah.)'),
        ('Kadıköy (Göztepe Mah.) Toplam', 'Kadıköy (Göztepe Mah.)'),
        ('Kadıköy (Kozyatağı Mah.) Toplam', 'Kadıköy (Kozyatağı Mah.)'),
        ('Kadıköy (Rasimpaşa Mah.) Toplam', 'Kadıköy (Rasimpaşa Mah.)'),
        ('Kağıthane (Merkez Mah.) Toplam', 'Kağıthane (Merkez Mah.)'),
        ('Kartal (Esentepe Mah.) Toplam', 'Kartal (Cevizli Mah.)'),
        ('Kartal (Uğur Mumcu Mah.) Toplam', 'Kartal (Uğur Mumcu Mah.)'),
        ('Küçükçekmece (Halkalı Merkez Mah.) Toplam', 'Küçükçekmece (Halkalı Merkez Mah.)'),
        ('Maltepe (Cevizli Mah.) Toplam', 'Maltepe (Cevizli Mah.)'),
        ('Maltepe (Küçükyalı Mah.) Toplam', 'Maltepe (Küçükyalı Mah.)'),
        ('Maltepe (Zümrütevler Mah.) Toplam', 'Maltepe (Zümrütevler Mah.)'),
        ('Pendik (Ahmet Yesevi Mah.) Toplam', 'Pendik (Ahmet Yesevi Mah.)'),
        ('Pendik (Kurtköy Mah.) Toplam', 'Pendik (Kurtköy Mah.)'),
        ('Şişli (Merkez Mah.) Toplam', 'Şişli (Merkez Mah.)'),
        ('Tuzla (Yayla Mah.) Toplam', 'Tuzla (Yayla Mah.)'),
        ('Tuzla (Orta Mah.) Toplam', 'Tuzla (Orta Mah.)'),
        ('Ümraniye (Çamlık Mah.) Toplam', 'Ümraniye (Çamlık Mah.)'),
        ('Ümraniye (Yamanevler Mah.) Toplam', 'Ümraniye (Yamanevler Mah.)'),
        ('Üsküdar (Barbaros Mah.) Toplam', 'Üsküdar (Barbaros Mah.)'),
        ('Üsküdar (Bulgurlu Mah.) Toplam', 'Üsküdar (Bulgurlu Mah.)'),
        ('Zeytinburnu (Çırpıcı Mah.) Toplam', 'Zeytinburnu (Çırpıcı Mah.)'),]

class BranchMonthlyDataForm(forms.Form):
    branch_name                 = forms.ChoiceField(choices=BRANCHCHOICES, label="Şubeniz")
    person_name                 = forms.CharField(label="Adınız Soyadınız")
    email                       = forms.EmailField(label="E-Posta Adresiniz")
    re_email                    = forms.EmailField(label="Tekrar E-Posta Adresiniz")

    yemeksepeti_fee             = forms.DecimalField(max_value=1000000,label="YemekSepeti Komisyon Tutarı (KDV Dahil Ödediğiniz Toplam Tutar)")
    getiryemek_fee              = forms.DecimalField(max_value=1000000,label="GetirYemek Komisyon Tutarı (KDV Dahil Ödediğiniz Toplam Tutar)")
    trendyolyemek_fee           = forms.DecimalField(max_value=1000000,label="TrendyolYemek Komisyon Tutarı (KDV Dahil Ödediğiniz Toplam Tutar)")
    creditcards_fee             = forms.DecimalField(max_value=1000000,label="Kredi Kartları Komisyon Tutarı (KDV Dahil Ödediğiniz Toplam Tutar)")
    foodcards_fee               = forms.DecimalField(max_value=1000000,label="Ödeme Kartları Komisyon Tutarı (KDV Dahil Ödediğiniz Toplam Tutar)")

    branchdrink_expenses        = forms.DecimalField(max_value=1000000,label="Meşrubat Giderleri (KDV Dahil Toplam Tutar)")
    branchayranyoghurt_expenses = forms.DecimalField(max_value=1000000,label="Ayran ve Yoğurt Giderleri (KDV Dahil Toplam Tutar)")
    branchbread_expenses        = forms.DecimalField(max_value=1000000,label="Ekmek Giderleri (KDV Dahil Toplam Tutar)")
    branchkitchen_expenses      = forms.DecimalField(max_value=1000000,label="Şube İçi Mutfak Giderleri (Damacana Su, Çay, Kahve, Şeker, vb.)")
    branchconsumables_expenses  = forms.DecimalField(max_value=1000000,label="Şube İçi Sarf Kullanım (Kağıt Havlu, Zımba Teli, Şeffaf Poşet, vb.)")
    branchutility_expenses      = forms.DecimalField(max_value=1000000,label="Elektrik, Su, Doğalgaz")
    branchrent_expenses         = forms.DecimalField(max_value=1000000,label="Kira ve Stopaj Toplamı")
    branchinternet_expenses     = forms.DecimalField(max_value=1000000,label="Telefon, İnternet, Muhasebe vb.")

    manager_count               = forms.DecimalField(max_value=1000000,label="Yönetici Personel Giderleri (Yönetici Personellerin Tümünün Toplam Maaşı)")
    manager_expenses            = forms.DecimalField(max_value=1000000,label="Yönetici Personel Kişi Sayısı")
    staff_count                 = forms.DecimalField(max_value=1000000,label="İç Personel Giderleri (İç Personellerin Tümünün Toplam Maaşı)")
    staff_expenses              = forms.DecimalField(max_value=1000000,label="İç Personel Kişi Sayısı")
    courier_count               = forms.DecimalField(max_value=1000000,label="Motor ve Kurye Giderleri (Motorlar ve Kuryelerle İlgili Bütün Giderlerin Toplamı (Maaşlar, Bakım Giderleri, Benzin vb.))")
    courier_expenses            = forms.DecimalField(max_value=1000000,label="Kurye Kişi Sayısı")