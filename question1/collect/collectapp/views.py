from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def hero_list(request):
    if request.method == 'POST':
        mi=10**9
        ma=0
        val=0
        su=0
        inval=0
        summation=0
        for i in request.data:
            i=str(i)
            if i.isnumeric() and int(i)>0:
                val+=1
                su+=int(i)
                mi=min(mi,int(i))
                ma=max(ma,int(i))
                summation+=int(i)
            else:
                inval+=1
        return Response({"valid_entries": val,"invalid_entries": inval,"min": mi,"max": ma,"average": summation/val})