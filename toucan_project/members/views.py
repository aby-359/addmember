from django.shortcuts import render, redirect
from .models import Member, School
from .forms import MemberForm
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()

    return render(request, 'members/add_member.html', {'form': form})


def member_list(request):
    schools = School.objects.all()
    selected_school = request.GET.get('school')

    if selected_school:
        members = Member.objects.filter(school__name=selected_school)
    else:
        members = Member.objects.all()

    return render(request, 'members/member_list.html',
                  {'members': members, 'schools': schools, 'selected_school': selected_school})
