def thesaurus_adv(*names):
    names_list = {}
    for name in sorted(names):
        n, s = name.split()
        val = names_list.setdefault(s[0], {n[0]: [name]})
        n_val = val.setdefault(n[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_list

print(thesaurus_adv("Дмитрий Калинин", "Николай Харченко", "Галина Хареба", "Надежда Середникова", "Юлия Медведева", "Николай Аспидов", "Карина Серова", "Малик Саилов", "Алексей Лухта"))
