from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModelName
@api_view(['POST'])
def hero_list(request):
    if request.method == 'POST':
        x=request.data["x"]
        y=request.data["y"]
        record=MyModelName(x=x,y=y)
        record.save()
        l=[]
        for i in MyModelName.objects.all():
            l.append((i.x,i.y))
        se=set(l)
        l.sort()
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                a,b=l[i]
                c,d=l[j]
                if a==c and (a!=c or b!=d):
                    diff=abs(b-d)
                    if (a+diff,b) in se and (c+diff,d) in se:
                        return Response({"status":"Success ("+str(a)+","+str(b)+") ("+str(c)+","+str(d)+") ("+str(a+diff)+","+str(b)+") ("+str(c+diff)+","+str(d)+")"})
        return Response({"status": "accepted"})
