import pandas as pd
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render
from requests import Response
import matplotlib.pyplot as plt
import base64
from training.models import Course
from io import BytesIO

def course_list(request):

    context = dict()
    context['courses'] = Course.objects.all()

    return render(request, 'course/course_list.html', context=context)


def course_detail(request, pk):

    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse("Product not found")
    queryset  = Course.objects.filter(Q(pk=pk) | Q(pk=pk))
    if queryset.exists():
        course = queryset.first()

        return render(request, 'course/course_detail.html', {'course': course})
    raise Http404

def course_report(request):
    if request.method == "POST":
        return HttpResponse("POST Response")
    else:
        courses = Course.objects.all().order_by('id')  # Adjust according to your needs
        titles = [course.title for course in courses]
        count = [course.buy_count for course in courses]

        # Step 2: Generate the scatter plot
        # plt.figure(figsize=(10, 6))
        plt.scatter(titles, count, color='blue', label="Course Price")

        # plt.ylim(20000, 200000)
        # Set the default (linear) scale for the Y-axis (no log scale)
        plt.title("Course Price vs Title (Exact Prices)")
        plt.xlabel("Course Title")
        plt.ylabel("Course Price")

        # Rotate title labels for better visibility
        plt.xticks(rotation=90)

        # Step 3: Save the plot to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Step 4: Encode the PNG image to base64
        image_base64 = base64.b64encode(image_png).decode('utf-8')

        # Step 5: Pass the image to the template
        return render(request, 'plot_view.html', {'plot_image': image_base64})

        # return HttpResponse("GET Response")


