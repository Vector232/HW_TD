def get_unicue_names(mentors):
    # Добавьте в список всех преподавателей со всех курсов
    all_list = []
    for m in mentors:
        # Допишите здесь ваш код, который заполнит all_list. Можете как складывать списки, так и использовать метод extend
        all_list.extend(m)
    # Сделайте список all_names_list, состоящий только из имён, и заполните его
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
        
    # Сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
    unique_names = set(all_names_list)

    # Теперь необходимо отсортировать имена в алфавитном порядке. Подсказка: используйте sorted() для списка
    # Допишите код ниже
    all_names_sorted = sorted(unique_names)
    # Допишите конструкцию вывода результата. Можете использовать string.join()
    # Результат будет в all_names_sorted
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def top3name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    # Уникальные имена будут в unique_names
    unique_names = set(all_names_list)

    # Подсчитайте встречаемость каждого имени через list.count()
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)]) # Добавьте подсчёт имён

    # Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
    # Используйте его, как есть, или напишите собственный :)
    popular.sort(key=lambda x:x[1], reverse=True)

    # Получите топ-3 часто встречающихся имён из списка popular
    # Подсказка: возьмите срез списка
    top_3 = [ name + ": " + str(count) + " раз(а)" for name, count in popular[0:3]]

    return ', '.join(top_3)

def supermentors(courses, mentors):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0]) # Допишите код здесь
        # Допишите ниже код, который добавляет списки имён в общий список mentors_names:
        mentors_names.append(course_names)
    ans = ''
    # Храните здесь пары курсов, в которых есть совпавшие имена
    pairs = []
    # # Попарное сравнение "наборов" преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            # Проверьте, что вы не сравниваете список сам с собой:
            if id1 == id2: continue
            # Допишите ниже код для сравнения двух "наборов" преподавателей. Подсказка: используйте множества
            intersection_set = set(mentors_names[id1]).intersection(set(mentors_names[id2]))
            if len(intersection_set) > 0: # Допишите проверку, что результат не пустой, имена есть
                # Допишите ниже код, который проверяет, что эта пара ещё не встречалась
                pair = sorted([id1, id2])
                # Если pair еще не встречалась, то выведите на экран два курса и список преподавателей, которые есть на обоих курсах
                if pair not in pairs:
                    pairs.append(pair)
                    # Отсортируйте имена по алфавиту. Подсказка: используйте sorted() для списка
                    all_names_sorted = sorted(intersection_set)
                    # Допишите конструкцию вывода результата. Можете использовать string.join()
                    ans = ans + f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}\n"
    return ans

