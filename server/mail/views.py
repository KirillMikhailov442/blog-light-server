from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives

from .models import Subscriber
from .serializer import SubscriberSerializer, FormContactSerializer
from server.settings import EMAIL_HOST_USER


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            subscriber = serializer.save()
            return Response({'id': subscriber.id})
        

    @action(methods=['post'], detail=False)
    def contact(self, request):
        data = FormContactSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        html_content = f"""
            <h1>Это сообщение написал {request.data['name']}<{request.data['email']}> с вашего сайта</h1>
            <p>{request.data['message']}</p>
            <p style='color: gray'>Не забудьте ответить ему :)</p>
        """
        text_content = f"""
            Это сообщение написал {request.data['name']}<{request.data['email']}> \n
            {request.data['message']}
        """

        mail = EmailMultiAlternatives('Пользователь написал вам письмо', text_content, EMAIL_HOST_USER, ['akcjdjs123456789@gmail.com'])
        mail.attach_alternative(html_content, 'text/html')
        mail.send()
        return Response(True)