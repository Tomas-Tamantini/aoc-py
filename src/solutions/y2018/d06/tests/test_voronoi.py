import pytest

from src.solutions.shared.geometry import Vector2D
from src.solutions.y2018.d06.logic.voronoi import Voronoi, VoronoiCell


@pytest.fixture
def voronoi() -> Voronoi:
    seeds = {
        Vector2D(1, 1),
        Vector2D(1, 6),
        Vector2D(8, 3),
        Vector2D(3, 4),
        Vector2D(5, 5),
        Vector2D(8, 9),
    }
    return Voronoi(seeds)


def test_finite_voronoi_cells_are_yielded(voronoi: Voronoi):
    cells = voronoi.finite_cells()
    assert set(cells) == {
        VoronoiCell(seed=Vector2D(3, 4), area=9),
        VoronoiCell(seed=Vector2D(5, 5), area=17),
    }


def test_safe_area_is_num_cells_whose_sum_of_distances_is_within_bounds(
    voronoi: Voronoi,
):
    safe_area = voronoi.safe_area(sum_dist_less_than=32)
    assert safe_area == 16
