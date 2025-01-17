from django import forms

from myPlantApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['profile_picture']


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = []
