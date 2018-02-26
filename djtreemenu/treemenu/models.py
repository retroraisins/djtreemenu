from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)


class MenuItem(models.Model):

    title = models.CharField(max_length=100)

    root_menu = models.ForeignKey(
        Menu, null=True, on_delete=models.CASCADE, blank=True)

    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    link_url = models.CharField(max_length=100, unique=True)

    level = models.IntegerField(default=0, editable=False)

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def get_level(self):
        def get_parent_id(id):
            return MenuItem.objects.values_list('parent', flat=True).get(id=id)

        def is_has_parent(id_):
            if MenuItem.objects.get(id=id_).parent:
                return True
            return False
        level = 0
        id_ = self.id
        while is_has_parent(id_):
            level += 1
            id_ = get_parent_id(id_)
        return level

    def is_has_children(id):
        if MenuItem.objects.filter(parent=id).exists():
            return True
        return False

    def get_children(self):
        kyes = ['id', 'title', 'url', 'level', 'children']
        children = []
        for menu in MenuItem.objects.filter(parent=self.id):
            if MenuItem.is_has_children(id=menu.id):
                children.append(
                    {
                        'id': menu.id,
                        'title': menu.title,
                        'url': menu.link_url,
                        'level': menu.level,
                        'children': menu.get_children()
                    }
                )
            else:
                children.append(
                    {
                        'id': menu.id,
                        'title': menu.title,
                        'url': menu.link_url,
                        'level': menu.level,
                        'children': None
                    }
                )

        return children

    def get_menu_from(root):
        menu_tree = []

        for menu in MenuItem.objects.filter(root_menu=root):
            if MenuItem.is_has_children(id=menu.id):
                menu_tree.append(
                    {
                        'id': menu.id,
                        'title': menu.title,
                        'url': menu.link_url,
                        'level': menu.level,
                        'children': menu.get_children()
                    }
                )
            else:
                menu_tree.append(
                    {
                        'id': menu.id,
                        'title': menu.title,
                        'url': menu.link_url,
                        'level': menu.level,
                        'children': None
                    }
                )
        return menu_tree

    def save(self, *args, **kwargs):
        setattr(self, 'level', self.get_level())
        super().save(*args, **kwargs)
