from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from django.db.models import Q, Count, Value

from ats.models import Candidate
from ats.serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        """
        Search for candidates based on the provided query.

        The search query is split into individual words, and candidates whose names contain any of the words
        are filtered. The results are then annotated with a match score based on the number of words in the
        search query that can be found in the candidate's name. The results are sorted by the match score
        in descending order.

        Example:
        If the search query is "Ajay Kumar Yadav", the order of results will be:
        ["Ajay Kumar Yadav", "Ajay Kumar", "Ajay Yadav", "Kumar Yadav", "Ramesh Yadav", "Ajay Singh"]

        Args:
            request (Request): The HTTP request object containing the search query parameter 'q'.

        Returns:
            Response: A JSON response containing the serialized candidate data sorted by relevancy.
        """
        query = request.GET.get("q", "").strip()

        if query:
            words = query.split()
            queries = [Q(name__icontains=word) for word in words]
            query_combined = queries.pop()
            for item in queries:
                query_combined |= item

            queryset = (
                Candidate.objects.filter(query_combined)
                .annotate(
                    match_score=Count(
                        "id",
                        filter=Q(name__icontains=Value(query)),
                    )
                )
                .order_by("-match_score")
            )
        else:
            queryset = Candidate.objects.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def validate_phone_number(self, phone_number):
        if phone_number and (not phone_number.isdigit() or len(phone_number) != 10):
            raise ValidationError(
                {"phone_number": "Phone number must be a 10-digit number."}
            )

    def perform_create(self, serializer):
        self.validate_phone_number(serializer.validated_data.get("phone_number"))
        serializer.save()

    def perform_update(self, serializer):
        self.validate_phone_number(serializer.validated_data.get("phone_number"))
        serializer.save()
