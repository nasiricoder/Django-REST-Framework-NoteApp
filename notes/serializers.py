from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id', 'title', 'content', 'created_at',
            'author_id'
        ]

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Note.objects.create(author_id=user_id, **validated_data)
