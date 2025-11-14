import datetime
import tempfile
from pathlib import Path
from .serializers import CredentialsSerializer
from django.conf import settings
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import User
from docxtpl import DocxTemplate
import os

# Create your views here.

class credentialsTemplateView(CreateAPIView):
    serializer_class = CredentialsSerializer

    def post(self, request):
        if request.user.is_staff or request.user.is_hr:
            try:
                template_path = Path(settings.BASE_DIR) / 'gener' / 'templ' / 'credentials.docx'
                if not template_path.exists():
                    return Response({'error': 'Шаблон не найден'}, status=404)

                doc = DocxTemplate(str(template_path))
                user = User.objects.get(id=request.POST.get('user'))
                context = {
                    'username': f'{user.first_name} {user.last_name} {user.middle_name}',
                    'org': user.organization.name,
                    'org_pre': user.organization.name_prepositional,
                    'post': user.post.lower(),
                    'date': datetime.date.strftime(datetime.date.today(), '%d.%m.%Y'),
                }

                doc.render(context)

                with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
                    doc.save(tmp_file.name)

                    with open(tmp_file.name, 'rb') as f:
                        response = HttpResponse(
                            f.read(),
                            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                        )
                        response['Content-Disposition'] = f'attachment; filename="credentials_{user.username}.docx"'

                    os.unlink(tmp_file.name)
                return response

            except Exception as e:
                return Response({'error': str(e)}, status=500)
        return Response({'error': 'Доступ запрещен'}, status=403)

