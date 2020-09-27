from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.models import User
from .models import Goal, Tracker
from .serializers import GoalSerializer, TrackerSerializer, RegisterSerializer, UserSerializer
import datetime


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def add_goals(request):
    user = User.objects.get(pk=request.data['user'])
    goal = Goal(user=user, name=request.data['name'],
                startDate=request.data['startDate'], endDate=request.data['endDate'])
    if 'details' in request.data:
        goal.details = request.data['details']
    elif 'frequency' in request.data:
        goal.frequency = request.data['frequency']
    elif 'description' in request.data:
        goal.description = request.data['description']

    goal.save()
    serializer = GoalSerializer(goal)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def get_all_goals(request):
    goals = Goal.objects.all()
    serializer = GoalSerializer(goals, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def get_all_trackers(request):
    trackers = Tracker.objects.all()
    serializer = TrackerSerializer(trackers, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def add_tracker(request):
    goal = Goal.objects.get(pk=request.data['goal'])
    time = datetime.datetime.now()
    tracker = Tracker(goal=goal, doneday=time, notes=request.data['notes'])
    tracker.save()
    serializer = TrackerSerializer(tracker)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def goals_for_user(request):
    goals = Goal.objects.all().filter(user_id=request.data['user'])
    serializer = GoalSerializer(goals, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def trackers_for_goal(request):
    trackers = Tracker.objects.all().filter(goal_id=request.data['goal'])
    serializer = TrackerSerializer(trackers, many=True)
    return Response(serializer.data)
