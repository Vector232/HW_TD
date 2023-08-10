from task1 import *
import pytest

class TestTask1:
    def test_get_unicue_names(self):
        names = [
            ['a', 'b', 'c', 'd', 'e'],
            ['f', 'g',],
            ['a', 'c', 'g']
        ]
        ans = 'Уникальные имена преподавателей: a, b, c, d, e, f, g'
        assert get_unicue_names(names) == ans

        names = []
        ans = 'Уникальные имена преподавателей: '
        assert get_unicue_names(names) == ans
    
    def test_top3name(self):
        names = [
            ['c', 'c', 'c', 'c', 'c'],
            ['g', 'g',],
            ['a', 'a', 'a']
        ]
        ans = 'c: 5 раз(а), a: 3 раз(а), g: 2 раз(а)'
        assert top3name(names) == ans

    def test_supermentors(self):
        courses = ["1", "2"]
        mentors = [
            ['a','b'],
            ['b']
        ]
        ans = "На курсах '1' и '2' преподают: b\n"
        assert supermentors(courses, mentors) == ans


if __name__ == '__main__':
    pytest.main(["-vv"])
