from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from os import walk
from .inequality import Inequality

# импортируем скрипты Javascript
js_scripts = {}
for dw in walk(__file__.replace('views.py', 'js/')):
    for jss in dw[2]:
        s = open(__file__.replace('views.py', 'js/') + jss)
        js_scripts[jss.replace('.', '_')] = s.read()
        s.close()
    break



# Страница для решения
solveView = lambda request: render(request=request, template_name='solve.html', context=js_scripts)

# Страница с инструкцией к сайту
manualView = lambda request: render(request=request, template_name='man.html', context={})


# Обработка результата
def resultView(request: WSGIRequest):
    inequality = Inequality(request.POST.get('k_a'),
                            request.POST.get('k_b'),
                            request.POST.get('k_c'),
                            request.POST.get('is_d') == 'true',
                            request.POST.get('sign_of'))

    context = {
        # Репрезентация неравенства
        'solve_to': inequality.to_str,
        # Шаги
        'steps': inequality.steps,
        # Изображение
        'img': 'images/'+inequality.img+'.jpg',
    }
    return render(request=request, template_name='result.html', context=context)
