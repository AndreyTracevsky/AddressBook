from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Proverka"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = [] # делаем "вырезку", удаляем элементы с 0 по 1 (удаляется первый элемент с индексом == 0)
    assert old_groups == new_groups # сравниваем списки