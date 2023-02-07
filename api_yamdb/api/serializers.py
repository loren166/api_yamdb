from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Review, Comments, User, Category, Genre, Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Оценки."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'pub_date', 'score')

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data

        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user
        if Review.objects.filter(author=author, title=title_id).exists():
            raise serializers.ValidationError(
                'Можно написать лишь один отзыв.'
            )
        return data

    def validate_score(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError(
                'Оценкой должно быть число от 1 до 10.'
            )
        return value


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')


class AdminUserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя с ролью администратор."""
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')


class NotAdminUserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя - не администратора."""
<<<<<<< HEAD

=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категорий."""
<<<<<<< HEAD

=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
    class Meta:
        model = Category
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели жанров."""
<<<<<<< HEAD

=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения произведения."""
<<<<<<< HEAD

=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitleWriteSerializer(serializers.ModelSerializer):
    """Сериализатор для записи произведения."""
<<<<<<< HEAD

=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )

    class Meta:
        model = Title
        fields = '__all__'
