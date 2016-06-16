from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from items.models import *
# Create your views here.
def IndexView(req):
    expressions = Expression.objects.all()[:20];
    return render_to_response(template_name="index.html",context={'exps':expressions})

def toJson(exps):
    result = []
    for exp in exps:
        each = '{"fromwhom":"' + exp.fromwhom.name + '","towhom":"' +  exp.towhom.name + '","text":"' +  exp.text + '","pk":"' +  str(exp.pk) + '","pub_time":"' +  str(exp.pub_time.strftime("%Y-%m-%d %H:%M:%S"))+ '"}'
        result.append(each)
    result = str(result).replace("u'","")
    result = str(result).replace("']","]")
    result = str(result).replace("'","")
    return result
@csrf_exempt
def Update(req,id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    expressions = toJson(Expression.objects.filter(pk__gte=id))
    return HttpResponse(expressions+"Spliter")


def Person_detail(req,name):
    person = Person.objects.filter(name=name)
    if(person.count()>0):
        return render_to_response(template_name='detail.html',context={'person':person[0]})
    else:
        raise Http404

def Rank(req):
    top20 = Person.objects.all().order_by("-numb")[0:20]
    return render_to_response(template_name="rank.html",context={'top20':top20})

@csrf_exempt
def EP(req):
    if 'fromwhom' in req.POST or 'towhom' in req.POST or 'text' in req.POST:
        if (not req.POST['fromwhom']=="") and (not req.POST['towhom']=="") and (not req.POST['text']==""):
            text = req.POST['text']
            fromwhom = req.POST['fromwhom']
            towhom = req.POST['towhom']

            if(Person.objects.filter(name=fromwhom).count() < 1):
                person = Person(name=fromwhom)
                person.save()
            if(Person.objects.filter(name=towhom).count() < 1):
                person = Person(name=towhom)
                person.save()

            fromwhom = Person.objects.get(name=fromwhom)
            towhom = Person.objects.get(name=towhom)
            towhom.numb = towhom.numb + 1
            towhom.save();
            exp = Expression(towhom=towhom,fromwhom=fromwhom,text=text)
            exp.save()
            return HttpResponse('{"state":"success"}Spliter')

    return HttpResponse('{"state":"error"}Spliter')

