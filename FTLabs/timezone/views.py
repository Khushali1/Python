from django.shortcuts import render
from .serializers import MemberSerializer, PeriodSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Member, Period


# Create your views here.

class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer

    def get_queryset(self):
        period_var = Period.objects.all()
        return period_var


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer

    def get_queryset(self):
        member_var = Member.objects.all()
        return member_var

