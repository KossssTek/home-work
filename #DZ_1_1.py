# Номер 1
duration = int(input('Ведите время в секундах'))
days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24)) // (60 * 60)
minutes = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
seconds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
