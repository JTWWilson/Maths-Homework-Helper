from string import ascii_letters


all_same = lambda items: all(x == items[0] for x in items)


def find_difference(sequence):
    """
    Finds the difference between each number in the sequence provided,
    if the difference between each of them is the same, it must be linear, if not; quadratic
    :argument sequence: The sequence that is tested by the function
    :returns nextLayer[0]: If it is linear it returns the number that it goes up in
    :returns nextLayer: If it is quadratic then it returns all of the differences between the terms
    """
    assert all([isinstance(i, (int, float)) for i in sequence]), 'Not all of the items in sequence were integers or floating point values: {}'.format(sequence)
    nextLayer = []
    i = 0
    while i < (len(sequence) - 1):
        nextLayer.append(sequence[i + 1] - sequence[i])
        i += 1
    return nextLayer


def get_general_formulae(highest_power):
    highest_power += 1
    layers = [[]]
    # For each power of n
    for i in range(highest_power):
        # Add a list of all the needed powers
        layers[0].append([(j + 1) ** i for j in range(highest_power + 1)])
    # Layers -> [[a0, a1, a2, a3], [b0, b1, b2, b3], [c0, c1, c2, c3] ad infinitum]
    # print(layers)

    # Find the highest_power-th difference of the sequence
    for i in range(highest_power - 1):
        layers.append([find_difference(layers[-1][j]) for j in range(len(layers[-1]))])
    # print(layers)
    # For each item in the 'sausage' save the expression it forms
    # print([' + '.join(reversed([str(j)  + str(ascii_letters[(highest_power - 1) - index]) for index, j in enumerate(i)])) for i in [[j[0] for j in i] for i in layers]])
    formulae = [list(reversed([j for index, j in enumerate(i)]))
                        for i in [[j[0]
                            for j in i]
                                for i in layers]]
    # print(formulae)
    return formulae


def substitute(equation, values):
    result = []
    for index, i in enumerate(equation):
        result.append(i * values[index])
    return result


class beautify:
    def __init__(self, f):
        self.f = f

    def __call__(self, sequence):
        answer = self.f(sequence)
        # Runs through answer neatening it up to match mathematical conventions
        print(''.join(["{coefficient}{power} ".format(coefficient=i if i < 0 else "+ " + str(i) if not str(i).endswith('.0') else int(i) if i < 0 else "+ " + str(int(i)), power="n**" + str((len(answer) - 1) - index) if (len(answer) - 1) - index != 0 else '') if i != 0 else '' for index, i in enumerate(answer)]).lstrip('+ '))
        return answer


@beautify
def solve(sequence):
    layers = [sequence]
    for i in sequence:
        if not all_same(layers[-1]):
            layers.append(find_difference(layers[-1]))
    print(layers)
    general_formulae = get_general_formulae(len(layers) - 1)
    print(general_formulae)
    answers = [None for i in general_formulae]
    print(len(answers))
    # Go up through the layers, working out the values of each variable as it goes
    for index, i in enumerate(reversed(general_formulae)):
        variable = layers[-(index + 1)][0]
        for subindex, j in enumerate(i):
            if answers[subindex] is None:
                variable /= j
                break
            else:
                variable -= answers[subindex] * j
        answers[index] = variable
    # print(answers)
    return answers




nth_term = solve([3, 6, 11, 18, 27])
print(nth_term)

#def main():
#    sequence = [int(item) for item in input('What is the sequence? ').split(',').split()]
#    # sequence=[int(a) for a in sequence]
#    print('The Nth Term is... ')
#    nth_term = solve(sequence)
#    print(nth_term)
#    print('The next three terms are... ' + str(find_term(sequence, len(sequence) + 1)) + ',' + str(
#        find_term(sequence, len(sequence) + 2)) + ',' + str(find_term(sequence, len(sequence) + 3)))
#    print('The 100th term is... ' + str(find_term(sequence, 100)))
