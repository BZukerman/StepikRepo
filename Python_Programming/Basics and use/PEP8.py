# Какие способы слайсинга списка являются допустимыми с точки
# зрения рекомендаций PEP 8?

a[lower + offset:upper + offset]        # Wrong

a[lower:upper], a[lower:upper:], a[lower::step]     # Correct

a[lower + offset : upper + offset]      # Correct

a[lower+offset : upper+offset]          # Correct

a[lower : : upper]                      # Wrong