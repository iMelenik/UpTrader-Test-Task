from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from menu.utils.slugs import slug_check
from menu.utils.transliterate import translit


class MenuNode(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Наименование'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
        verbose_name='Родитель'
    )
    slug_name = models.SlugField(
        unique=True,
        max_length=70,
        null=True,
        blank=True
    )
    level = models.IntegerField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slug_check(self, slugify(translit(self.name)))

        if not self.level and self.parent:
            self.level = self.parent.level + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.slug_name)

    def get_absolute_url(self):
        return reverse("menus:index", kwargs={'slug_name': self.slug_name})

    @staticmethod
    def get_all_tree(node_slug_name):
        """returns RawQuerySet with node's kids ordered by depth"""
        return MenuNode.objects.raw(f"""
    WITH recursive tree (id, name, slug_name, parent_id, level, path)
    AS (
        SELECT *,  CAST(id AS CHAR(200)) AS path
        FROM menu_menunode
        WHERE slug_name = '{node_slug_name}'

    UNION ALL

        SELECT m.*, t.path || "," || m.id
        FROM menu_menunode AS m
        INNER JOIN tree AS t ON t.id = m.parent_id
        )

    SELECT id, name, slug_name, parent_id, level
    FROM tree
    ORDER BY path;
            """)
