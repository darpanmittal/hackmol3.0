from django.shortcuts import render
from django.conf import settings
import pyqrcode
import png
from pyqrcode import QRCode
from django.http import HttpResponseRedirect as redir
import os
import shutil
import stat
BASE_DIR=settings.BASE_DIR

# Create your views here
def home(request):
    return render(request,'index.html')

def code(s):
      
    url = pyqrcode.create(s)
      
    url.svg("./myqr.svg", scale = 8)
      
  
    
    os.path.join(BASE_DIR,'myqr.svg'),os.path.join(BASE_DIR,'QRcode/static/img/myqr.svg')
def result(request):
    if request.method=='POST':
        s=request.POST.get('s')
        code(s)
      
        shutil.move(os.path.join(BASE_DIR,'myqr.svg'),os.path.join(BASE_DIR,'QRcode/static/img/myqr.svg'))
        os.chmod(os.path.join(BASE_DIR,'QRcode/static/img/myqr.svg'), 0o777)
        return render(request, 'result.html')