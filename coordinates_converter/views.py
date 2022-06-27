from django.shortcuts import render

# Create your views here.

def coordinates_converter_view(request):
    coordinates_type = [
        'GEOGRAPHIC - (degree, minute, second)',
        'GEOGRAPHIC - (degree decimal)',
        'UTM - (meter)',
        'UTM - (meter)',
        'UTM - (meter)',
        'UTM - (meter)',
    ]

    return render(request, 'coordinates_converter/index.html', {
        'coordinates_type': coordinates_type,
    })