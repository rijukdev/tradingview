from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from signals.serializer import SignalSerializer
from django.http import Http404
from signals.models import Signals


class SignalAPI(APIView):
    def get(self, request):
        signals = Signals.objects.all()
        serializer = SignalSerializer(signals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SignalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignalDeleteAPI(APIView):
    def delete(self, request):
        count, _ = Signals.objects.all().delete()
        return Response(
            {"message": f"Deleted {count} signals records."},
            status=status.HTTP_204_NO_CONTENT
        )


class SignalDetailsAPI(APIView):
    def get_object(self, pk):
        try:
            return Signals.objects.get(pk=pk)
        except Signals.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        signals = self.get_object(pk)
        serializer = SignalSerializer(signals)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        signals = self.get_object(pk)
        serializer = SignalSerializer(signals, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignalDetailsDeleteAPI(APIView):
    def delete(self, request, pk):
        signals = self.get_object(pk)
        signals.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
