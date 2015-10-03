from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from yunity.models import Feedback


class FeedbackViewSet(viewsets.ViewSet):
    """
    Viewset to handle feedback about mapitem
    """
    queryset = Feedback.objects.all()

    def create(self, request):
        """
        Create new feedback about mapitem

        {mapitemid, type, status, text}
        """
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        Get Feedback for Mapitem pk
        """
        return Response(status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """
        Modify Feedback status/type or add arbitrator of mapitem pk
        """
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=["POST"])
    def arbitrationlog(self, request, pk=None):
        """
        Add entry to arbitrationlog

        {sender, type, content, replyTo}
        """
        return Response(status=status.HTTP_201_CREATED)