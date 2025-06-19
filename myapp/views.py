import sys
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def home(request):
    response = HttpResponse('elcome to my app home')
    return response

def info(request):
    r = HttpResponse(sys.version)
    return r

def data(request):
    d = {
        '6700000000':{
            'first_name': 'Anna',
            'last_name': 'anan'
            
        },
        '6700000001':{
            'first_name': 'Moon',
            'last_name': 'Moom'
        }
    }
    return JsonResponse(d) # type: ignore

def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
