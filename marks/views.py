from django.shortcuts import render
from .models import Record
def table(request):
    records = Record.objects.order_by('-mark')
    context={
        'records':records
    }
    return render(request,'marks/table.html',context)
