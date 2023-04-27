FROM_RU_TO_ENG_DICT = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
                       'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
                       'й': 'i', 'к': 'k', 'л': 'l','м': 'm','н': 'n',
                       'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                       'у': 'u', 'ф': 'f','х': 'h','ц': 'c', 'ч': 'ch',
                       'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y','ь': '',
                       'э': 'e','ю': 'u', 'я': 'ya'}


def translit(name: str) -> str:
    name = name.lower()
    for key in FROM_RU_TO_ENG_DICT:
        name = name.replace(key, FROM_RU_TO_ENG_DICT[key])
    return name
