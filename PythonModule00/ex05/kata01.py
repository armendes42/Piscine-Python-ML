kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print('\n'.join([f"{key} was created by {value}" for key, value in kata.items()]))