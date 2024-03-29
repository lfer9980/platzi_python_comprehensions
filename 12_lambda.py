def increment(x):
    return x + 1 

result = increment(10)
print(result)

increment_lambda = lambda x: x + 1

result_2 = increment_lambda(12)
print(result_2)

full_name = lambda name, last_name: f"{name.title()}, {last_name.title()}"

name_lambda = full_name("luis", "fernandez")
print(name_lambda)