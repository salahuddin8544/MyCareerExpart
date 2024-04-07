from django.db import models
from users.models import User
from django_editorjs_fields import EditorJsJSONField

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogs')
    content = EditorJsJSONField(
        plugins=[
            "@editorjs/image",
            "@editorjs/header",
            "editorjs-github-gist-plugin",
            "@editorjs/code@2.6.0",  # version allowed :)
            "@editorjs/list@latest",
            "@editorjs/inline-code",
            "@editorjs/table",
        ],
        tools={
            "Gist": {
                "class": "Gist"  # Include the plugin class. See docs Editor.js plugins
            },
            "Image": {
                "config": {
                    "endpoints": {
                        "byFile": "/editorjs/image_upload/",  # Your custom backend file uploader endpoint
                    }
                }
            }
        },
        i18n={
            'messages': {
                'blockTunes': {
                    "delete": {
                        "Delete": "Удалить"
                    },
                    "moveUp": {
                        "Move up": "Переместить вверх"
                    },
                    "moveDown": {
                        "Move down": "Переместить вниз"
                    }
                }
            },
        },
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
