from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from studentorg.models import Organization, College, Program, Student, OrgMember
from studentorg.forms import (
    OrganizationForm,
    CollegeForm,
    ProgramForm,
    StudentForm,
    OrgMemberForm,
)
from django.urls import reverse_lazy

class HomePageView(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()

        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values('student')
            .distinct()
            .count()
        )
        context['students_joined_this_year'] = count
        return context

class OrganizationList(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'organization_list'
    template_name = 'organization_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(name__icontains=q) | Q(description__icontains=q) | Q(college__name__icontains=q)
            )
        return qs


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


class CollegeList(LoginRequiredMixin, ListView):
    model = College
    context_object_name = 'college_list'
    template_name = 'college_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return qs


class CollegeCreateView(LoginRequiredMixin, CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('college-list')


class CollegeUpdateView(LoginRequiredMixin, UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('college-list')


class CollegeDeleteView(LoginRequiredMixin, DeleteView):
    model = College
    template_name = 'org_del.html'
    success_url = reverse_lazy('college-list')


class ProgramList(LoginRequiredMixin, ListView):
    model = Program
    context_object_name = 'program_list'
    template_name = 'program_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(prog_name__icontains=q) | Q(college__name__icontains=q))
        return qs


class ProgramCreateView(LoginRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('program-list')


class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('program-list')


class ProgramDeleteView(LoginRequiredMixin, DeleteView):
    model = Program
    template_name = 'org_del.html'
    success_url = reverse_lazy('program-list')


class StudentList(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'student_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(student_id__icontains=q)
                | Q(firstname__icontains=q)
                | Q(lastname__icontains=q)
                | Q(program__prog_name__icontains=q)
            )
        return qs


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'org_del.html'
    success_url = reverse_lazy('student-list')


class OrgMemberList(LoginRequiredMixin, ListView):
    model = OrgMember
    context_object_name = 'orgmember_list'
    template_name = 'orgmember_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(student__student_id__icontains=q)
                | Q(student__firstname__icontains=q)
                | Q(student__lastname__icontains=q)
                | Q(organization__name__icontains=q)
            )
        return qs


class OrgMemberCreateView(LoginRequiredMixin, CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberUpdateView(LoginRequiredMixin, UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = OrgMember
    template_name = 'org_del.html'
    success_url = reverse_lazy('orgmember-list')

