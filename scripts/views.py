from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template, TemplateDoesNotExist
from .models import Script, Category
from .services import execute_script

def index(request):
    scripts = Script.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'scripts/index.html', {
        'scripts': scripts,
        'categories': categories,
    })

def script_detail(request, pk):
    script = get_object_or_404(Script, pk=pk)
    result = None

    if request.method == "POST":
        # تنفيذ السكريبت تلقائياً إذا كان يتطلب واجهة تفاعلية
        result = execute_script(script.slug, request)

    context = {
        'script': script,
        'result': result,
    }
    return render(request, 'scripts/script_detail.html', context)
  

def script_detail(request, pk):
    script = get_object_or_404(Script, pk=pk)
    result = None
    runner_template = None

    # التحقق مما إذا كان هناك قالب تفاعلي مخصص لهذا الـ slug
    if script.slug:
        template_path = f"scripts/runners/{script.slug}.html"
        try:
            get_template(template_path)
            runner_template = template_path  # القالب موجود ومستعد للعرض
        except TemplateDoesNotExist:
            runner_template = None  # السكريبت للعرض فقط ولا يوجد له قالب تفاعلي

    if request.method == "POST":
        result = execute_script(script.slug, request)

    context = {
        'script': script,
        'result': result,
        'runner_template': runner_template,
    }
    return render(request, 'scripts/script_detail.html', context)