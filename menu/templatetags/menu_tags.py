from django import template
from menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('menu/node.html', takes_context=True)
def draw_menu(context, menu_name):
    full_tree = MenuNode.get_all_tree(menu_name)

    active_node_slug = context['request'].path.strip('/')
    if len(active_node_slug) > 0:
        if active_node_in_tree(active_node_slug, full_tree):
            return active_node_context(active_node_slug, full_tree)
    return {'children': full_tree}


@register.inclusion_tag('menu/node.html')
def draw_node(menu_node, active=False):
    local_context = {'menu_node': menu_node,
                     'tab': '-' * (menu_node.level - 1)}
    if active:
        local_context['active'] = True
    return local_context

def active_node_in_tree(active_node_slug, tree):
    """
    Checks if active node in current tree.
    Necessary to let several menus work independently.
    """
    for node in tree:
        if node.slug_name == active_node_slug:
            return True
    return False


def active_node_context(active_node_slug, full_tree):
    for i, node in enumerate(full_tree):
        if node.slug_name == active_node_slug:
            active_node = node
            active_node_position = i
            active_node_lvl = node.level
            break
    else:
        raise ValueError("Нужное значение не найдено в дереве.")

    parents = []
    cur_lvl = active_node_lvl
    for i in range(active_node_position, -1, -1):
        if full_tree[i].level == cur_lvl - 1:
            parents.append(full_tree[i])
            cur_lvl -= 1
    parents.reverse()

    kids = []
    for i in range(active_node_position + 1, len(full_tree)):
        if full_tree[i].parent == active_node:
            kids.append(full_tree[i])

    return {'active_menu_node': active_node,
            'parents': parents,
            'children': kids}
