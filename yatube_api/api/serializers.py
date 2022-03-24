from email.policy import default
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.shortcuts import get_object_or_404


from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'following')#'__all__'
        model = User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(source='follower', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True) #PrimaryKeyRelatedField(read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    validators = [
        UniqueTogetherValidator(
        queryset=Follow.objects.all(),
        fields=('user', 'following')
    )
    ]
    class Meta:
        fields = '__all__'
        model = Follow

    def create(self, validated_data):
        '''if 'following' not in self.initial_data:
            raise serializers.ValidationError('required field not found')'''
        username = self.initial_data.get('following')
        user = get_object_or_404(User, username=username)
        follow = Follow.objects.create(**validated_data, following=user)
        return follow

    def validate(self, data):
        if 'following' not in self.initial_data:
            raise serializers.ValidationError('required field not found')
        print('\n\n\natrs= ', data)
        
        return data
