from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render

from training.models import Course


def course_list(request):

    context = dict()
    context['courses'] = Course.objects.all()

    return render(request, 'course/course_list.html', context=context)


def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse("Product not found")
    queryset  = Course.objects.filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        course = queryset.first()

        return render(request, 'course/course_detail.html', {'course': course})
    raise Http404
