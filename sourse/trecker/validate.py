from django.core.exceptions import ValidationError


def summary_max_10_len(value):
    if len(value) > 10:
        raise ValidationError("Название не может быть больше 10 символов! Будьте кратки)))")
    return value


