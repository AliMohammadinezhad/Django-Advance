from rest_framework import serializers


from ...models import Post, Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    brief_content = serializers.ReadOnlyField(source="get_brief_content")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.HyperlinkedIdentityField(
        view_name="blog:api-v1:post-detail", read_only=True
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "relative_url",
            "absolute_url",
            "title",
            "content",
            "brief_content",
            "status",
            "category",
            "created_date",
            "published_date",
            "updated_date",
        ]
        read_only_fields = ["author"]

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("absolute_url", None)
            rep.pop("relative_url", None)
            rep.pop("brief_content", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
