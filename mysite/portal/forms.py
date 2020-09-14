from django import forms
from .models import Details

GENDER = [
    ('',''),
    ('male', 'Male'),
    ('female','Female'),
]

STAGE = [
    ('',''),
    ('unskilled','Unskilled'),
    ('10th_pass','10th Passed'),
    ('12th_pass','12th Passed'),
    ('graduate', 'Graduate'),
    ('post_graduate','Post Graduate'),
    ('diploma','Diploma'),
]

class ApplyJobForm(forms.ModelForm):
    gender = forms.CharField(label="Candidate Gender", widget=forms.Select(choices=GENDER))
    stage = forms.CharField(label="Qualification", widget=forms.Select(choices=STAGE))
    mobile = forms.CharField(label="Mobile Number")
    w_mobile = forms.CharField(label="Whattsapp Number")
    skills = forms.CharField(label="Other Skills")
    Name = forms.CharField(label="Cadidate Name")
    age = forms.CharField(label="Candidate Age")
    class Meta:
        model = Details
        fields = (
            'Name',
            'age',
            'gender',
            'mobile',
            'w_mobile',
            'stage',
            'occupation',
            'skills',
            'comments',
            'resume'
        )
