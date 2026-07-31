''' 
Problem statement

Build a reusable function execution pipeline.

The pipeline should:

Accept an initial value.
Accept any number of transformation functions.
Pass the result of each function into the next function.
Return the final result.
Stop and raise an error if a transformation is not callable.
'''


def pipeline(initial_value, *transformations):
    result = initial_value

    for transformation in transformations:
        if not callable(transformation):
            raise TypeError(
                f"{transformation!r} is not callable"
            )

        result = transformation(result)
    return result

def add_two(value):
    return value + 2

def multiply_by_three(value):
    return value * 3

def convert_to_string(value):
    return f"Result: {value}"


final_result = pipeline(
    5,
    add_two,
    multiply_by_three,
    convert_to_string
)

print(final_result)