from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModelName
@api_view(['GET','POST'])
def hero_list(request):
    if request.method == 'GET':
        fi=[]
        all=MyModelName.objects.all()
        for i in all:
            fi.append({"slot":i.id,"names":i.list})
        return Response(fi)
    if request.method == 'POST':
        action=request.data["action"]
        if action=="booking":
            sl=request.data["slot"]
            nm=request.data["name"]
            slot = MyModelName.objects.filter(id=sl)
            if slot.count()==0:
                record = MyModelName(id=sl,strength=10,cur=0)
                record.save()
            slot = MyModelName.objects.filter(id=sl)[0]
            if slot.cur+1<=slot.strength:
                slot.cur+=1
                slot.list.append(nm)
                slot.save()
                return Response({"status": "confirmed"})
            else:
                return Response({"status": "slot full, unable to save booking for "+nm+" in slot "+str(sl)})
        else:
            sl = request.data["slot"]
            nm = request.data["name"]
            slot = MyModelName.objects.filter(id=sl)
            if slot.count() == 0:
                return Response({"status": "no booking for the name " + nm + " in slot " + str(sl)})
            else:
                slot = MyModelName.objects.filter(id=sl)[0]
                for i in slot.list:
                    if i==nm:
                        slot.list.remove(i)
                        slot.save()
                        return Response({"status": "Cancelled booking for the name " + nm + " in slot " + str(sl)})
                return Response({"status": "no booking for the name " + nm + " in slot " + str(sl)})