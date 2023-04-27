from random import randint


def slug_check(obj, slug):
    """
    Checks slug to be unique. If not - generate random suffix and repeat check
    """
    qs = type(obj).objects.filter(slug_name=slug).exclude(id=obj.pk)
    if qs.exists():
        slug = f"{slug}-{obj.pk + randint(1, 10_000)}"
        return slug_check(obj, slug)
    else:
        return slug
