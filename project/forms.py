from django import forms
from models import Project, Application
from redactor.widgets import RedactorEditor

class ProjectForm(forms.ModelForm):

    description = forms.CharField(widget=RedactorEditor())
    class Meta:
        model = Project
        fields = ("title",  "display_image", "short_description", "description")

class ApplicationForm(forms.ModelForm):

    def __init__(self, project, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.project = project
        self.set_roles()

    def set_roles(self):
        roles = self.project.vacancies.exclude(available=0)
        if(roles):
            choices = []
            for r in roles:
                choices += [[r.title, r.title]]

            self.fields["roles"] = forms.MultipleChoiceField(choices = choices, widget  = forms.CheckboxSelectMultiple)

    class Meta:
        model = Application
        fields = ("pitch",)
