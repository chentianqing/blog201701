##########################################
#@Date      :   20170105
#@Author    :   chentianqing
#@email     :   993049884@qq.com
#@version   :   0.0.1
##########################################

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')