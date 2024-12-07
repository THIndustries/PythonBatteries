from collections import defaultdict

subjects = [('Mathematics', 'Alice Brown'),
            ('Mathematics', 'Bob Smith'),
            ('Physics', 'Cindy Lee'),
            ('Chemistry', 'David Johnson'),
            ('Biology', 'Eva Martinez'),
            ('English', 'Frank Davis'),
            ('History', 'Gina Rodriguez'),
            ('Mathematics', 'Hannah Kim'),
            ('Mathematics', 'Ian Chen'),
            ('Physics', 'Jackie Lee'),
            ('Chemistry', 'Kevin Wang'),
            ('Biology', 'Lucy Wong'),
            ('English', 'Michael Johnson'),
            ('History', 'Nadia Ali'),
            ('Mathematics', 'Olivia Taylor'),
            ('Mathematics', 'Peter Wong'),
            ('Physics', 'Quinn Jackson'),
            ('Chemistry', 'Rachel Chen'),
            ('Biology', 'Sarah Kim'),
            ('English', 'Thomas Smith'),
            ('History', 'Uma Patel'),
            ('Mathematics', 'Vivian Liu'),
            ('Mathematics', 'William Zhang'),
            ('Physics', 'Xavier Lee'),
            ('Chemistry', 'Yara Ahmed'),
            ('Biology', 'Zoe Chen'),
            ('English', 'Alan Davis'),
            ('History', 'Beth Lee'),
            ('Mathematics', 'Charlie Brown'),
            ('Mathematics', 'Diana Smith'),
            ('Physics', 'Emily Johnson')]


result = defaultdict(set)
for pred, stud in subjects:
    result[pred].add(stud)



print(*(f'{k}: {",".join(sorted(v))}' for k, v in sorted(result.items(), key=lambda x: x[0])), sep='\n')
