def pick_max(*args, default=None, abs_mode=False):
    # Якщо аргументів немає — повертаємо default
    if not args:
        return default

    # Якщо abs_mode=True — порівнюємо по абсолютному значенню
    if abs_mode:
        return max(args, key=lambda x: abs(x))
    return max(args)

