
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from ..models import Question, Choice

class QuestionListSerializer(ModelSerializer):
    """
    This serializer serializes the Question model
    It should also include a field "choices" that will serialize all the
        choices for a question
    You well need a SerializerMethodField for choices,
        http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    Reference this stack overflow for the choices:
        https://stackoverflow.com/questions/33945148/return-nested-serializer-in-serializer-method-field
    """

    choices = SerializerMethodField(source='get_choices')

    class Meta:
        model = Question
        fields = ('id', 'text','pub_date','choices',)

    def get_choices(self,obj):
        choices_qs = obj.choice_set.all()
        return ChoiceSerializer(choices_qs, many=True).data


class ChoiceSerializer(ModelSerializer):
    """
    This serializes the Choice model
    """
    class Meta:
        model = Choice
        fields = ('choice_text','votes')
