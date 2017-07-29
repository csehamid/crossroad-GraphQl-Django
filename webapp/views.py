from django.shortcuts import render
from django.http import HttpResponse
#import subprocess
#something = subprocess.check_output(['python', 'v4.py']).decode('utf-8')
import v4

def index(request):
    #return HttpResponse("<h2>HEY!</h2>")
    #output="output string"
    #return HttpResponse(something)
    #return HttpResponse("<br>%s</br>" %(v4.main()))
    data={}
    if request.method == 'POST':
        data['owner'] = request.POST.get('owner', 'some name')
        data['repository'] = request.POST.get('repository')
        data['commits']= v4.main(data['owner'],data['repository']  )
        #data['commits']= v4.main("csehamid", "crossroad")
    return render(request, 'webapp/index.html',data)
