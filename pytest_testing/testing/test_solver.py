from solver import Solver
from pytest import fixture, mark, param, raises


@fixture
def solver_instance():
    solver = Solver(2, 3)
    return solver


class TestSolver:
    def test_add(self, solver_instance):
        result = solver_instance.add()
        assert result == 5

    def test_mult(self, solver_instance):
        result = solver_instance.mult()
        assert result == 6

    @mark.parametrize("a, b, expected_result", [
        [2, 3, 6],
        [4, 3, 12],
        [7, 8, 56]
    ])
    def test_mult_params(self, a, b, expected_result):
        s = Solver(a, b)
        result = s.mult()
        assert result == expected_result

    @mark.parametrize("solver_instance", [
        param([0,"1"], id="only-one-string"),
        param(["1","0"], id="both-strings")
    ], indirect=True)
    def test_mult_raises(self, solver_instance: Solver):
        with raises(TypeError) as exc_info:
            solver_instance.mult()

        print(exc_info)
