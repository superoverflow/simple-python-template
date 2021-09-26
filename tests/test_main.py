from src.main import func1
from src.main import Company, get_land_parcels, get_companies


def test_func1():
    assert func1() == "To Do"


def test_get_land_parcels():
    land_parcels = [
        {"id": "l1", "companyId": "c1"},
        {"id": "l2", "companyId": "c2"},
        {"id": "l3", "companyId": "c3"},
        {"id": "l4", "companyId": "c5"},
        {"id": "l5", "companyId": "c5"},
    ]

    result = get_land_parcels(land_parcels)
    expected = {"c1": ["l1"], "c2": ["l2"], "c3": ["l3"], "c5": ["l4", "l5"]}
    assert result == expected


def test_get_companies():
    companies = [
        {"id": "c6", "name": "Small Corp B", "parentId": "c3"},
        {"id": "c1", "name": "Big Corp A", "parentId": "c5"},
        {"id": "c2", "name": "Big Corp B", "parentId": None},
        {"id": "c3", "name": "Medium Corp A", "parentId": "c1"},
        {"id": "c4", "name": "Medium Corp B", "parentId": "c2"},
        {"id": "c5", "name": "Small Corp A", "parentId": "c3"},
    ]

    expected = {
        "c6": Company(id="c6", name="Small Corp B", parentId="c3", children=[]),
        "c1": Company(id="c1", name="Big Corp A", parentId=None, children=["c3"]),
        "c2": Company(id="c2", name="Big Corp B", parentId=None, children=["c4"]),
        "c3": Company(
            id="c3", name="Medium Corp A", parentId="c1", children=["c6", "c5"]
        ),
        "c4": Company(id="c4", name="Medium Corp B", parentId="c2", children=[]),
        "c5": Company(id="c5", name="Small Corp A", parentId="c3", children=[]),
    }

    result = get_companies(companies)
    assert result == expected
