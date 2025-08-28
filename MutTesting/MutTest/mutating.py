import ast

import astunparse

from Tester import RunTest


def apply_mutations(node, tree, mutation_number, killed_count):
    if isinstance(node, ast.BinOp) and isinstance(node.op, (
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow, ast.RShift, ast.LShift, ast.BitOr,
            ast.BitAnd,
            ast.BitXor)):

        old_op = node.op
        for op_class in [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow, ast.RShift, ast.LShift,
                         ast.BitOr,
                         ast.BitAnd,
                         ast.BitXor]:
            if not isinstance(old_op, op_class):
                node.op = op_class()
                mutation_number += 1
                mutated_code = astunparse.unparse(tree)
                if RunTest.run_tests(mutated_code, mutation_number):
                    killed_count += 1
        node.op = old_op

    return killed_count, mutation_number


def use_mutation(source_code):
    tree = ast.parse(source_code)
    killed_count = 0
    mutation_number = 0
    for node in ast.walk(tree):
        killed_count, mutation_number = apply_mutations(node, tree, mutation_number, killed_count)

    return killed_count, mutation_number
