from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import conseil, tribunal
from .models import Profile,User
from .models import Message,Lawyer,Notary,News

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'الاسم الأول',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'اسم العائلة',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'اسم المستخدم',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'بريد إلكتروني',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'كلمة المرور',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'تأكيد كلمة المرور',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
  

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LawyerRegisterForm(forms.ModelForm):
    # Additional fields for lawyer registration
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': ' الاسم الأول',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'اسم العائلة',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'اسم المستخدم',
                                                             'class': 'form-control',
                                                             }))
    lawyer_license = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'رخصة المحاماة', 'class': 'form-control'}))
    practice_areas = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'منطقة الممارسة', 'class': 'form-control'}))
    experience_years = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'سنوات الخبرة', 'class': 'form-control'}))
    
    phone_number = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'رقم الهاتف', 'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'بريد إلكتروني',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'كلمة المرور',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'تأكيد كلمة المرور',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
  
    class Meta:
        model = Lawyer
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', 'lawyer_license', 'practice_areas', 'experience_years', 'phone_number',]
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class NotaryRegisterForm(forms.ModelForm):
    # Additional fields for Notary registration
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    Notary_license = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Notary License', 'class': 'form-control'}))
    practice_areas = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Practice Areas', 'class': 'form-control'}))
    experience_years = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Experience Years', 'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    phone_number = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'phone_number', 'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    class Meta:
        model = Notary
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', 'Notary_license', 'practice_areas', 'experience_years', 'phone_number',]
        
        
#-----------------------------


JUDGMENT_CHOICES = [
    ('جنائي', 'جنائي'),
    ('مدني', 'مدني'),
    ('إداري', 'إداري'),
    ('أسري', 'أسري'),
    ('تجاري', 'تجاري'),
    ('عمالي', 'عمالي'),
    # Add more choices as needed
]
NATURE_CHOICES = [
    ('مدعى', 'مدعى'),
    ('مدعى عليه', 'مدعى عليه'),
    ('جاني', 'جاني'),
    ('مجنى عليه', 'مجنى عليه'),
    # Add more choices as needed
]
ETAPE_CHOICES = [
    ('ابتدائي', 'ابتدائي'),
    (' جزئي', ' جزئي'),
    ('نقض', 'نقض'),
    ('استئناف ', ' استئناف'),
    # Add more choices as needed
]
ETAT_CHOICES = [
    ('منتهية', 'منتهية'),
    (' معلقة', ' معلقة'),
    ('تحت الدراسة', 'تحت الدراسة'),
    ('مرفوضة ', ' مرفوضة'),
    # Add more choices as needed
]

class JugeForm(forms.Form):
    
    type = forms.ChoiceField(label='نوع القضية', choices=JUDGMENT_CHOICES, widget=forms.Select(attrs={'style': 'text-align: right;'}))
    numeroaffaire=forms.IntegerField(label='مبلغ القضية', widget=forms.TextInput(attrs={'style': 'text-align: right;'}))
    etape = forms.ChoiceField(label='مرحلة التقاضي ', choices=ETAPE_CHOICES, widget=forms.Select(attrs={'style': 'text-align: right;'}))
    etat = forms.ChoiceField(label='حالة القضية  ', choices=ETAT_CHOICES, widget=forms.Select(attrs={'style': 'text-align: right;'}))
    conseil = forms.ModelChoiceField(label='المجلس', queryset=conseil.objects.all(), widget=forms.Select(attrs={'style': 'text-align: right;'}))
    tribunal = forms.ModelChoiceField(label='محكمة', queryset=tribunal.objects.all(), widget=forms.Select(attrs={'style': 'text-align: right;'}))
    sujeta = forms.CharField(label='موضوع القضية', widget=forms.TextInput(attrs={'style': 'text-align: right;'}))
    datea = forms.DateField(label='تاريخ القيد', widget=forms.DateInput(attrs={'style': 'text-align: right;'}))
    budjeta = forms.DecimalField(label='المبلغ الاجمالي للقضية', widget=forms.NumberInput(attrs={'style': 'text-align: right;'}))
    adver = forms.CharField(label='الخصم', widget=forms.TextInput(attrs={'style': 'text-align: right;'}))
    adre = forms.CharField(label='عنوان الخصم', widget=forms.TextInput(attrs={'style': 'text-align: right;'}))
    avocata = forms.CharField(label='محامي الخصم', widget=forms.TextInput(attrs={'style': 'text-align: right;'}))
    tclient = forms.ChoiceField(label='صفة الموكل', choices=NATURE_CHOICES, widget=forms.Select(attrs={'style': 'text-align: right;'}))
    nomclient = forms.CharField(label='الموكل', widget=forms.TextInput(attrs={'style': 'width: 200px; text-align: right; font-size: 16px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;color: #000;'}))
    details = forms.CharField(label='تفاصيل القضية')
    num = forms.IntegerField(label='رقم الهاتف', widget=forms.NumberInput(attrs={'style': 'text-align: right;'}))



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo'] 