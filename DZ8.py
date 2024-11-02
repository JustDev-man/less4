import time

def time_function(func, *args, **kwargs):
    start_time = time.time()
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        print(f"Помилка: {exc}")
        return None, 0
    else:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Час виконання: {elapsed_time:.6f} секунд")
        return result, elapsed_time
def add_numbers(a, b):
    print(a, "+", b, "=", a + b)

result, elapsed_time = time_function(add_numbers, 2, 2)
