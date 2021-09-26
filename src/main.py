from dataclasses import dataclass
from typing import List, Dict


"""
The Problem
We would like you to change the below function to return which land parcels the given company owns (** directly and indirectly **).
When you are ready, please open any text-editor/IDE you wish, paste the code below, and share your screen so we can collaborate on the solution.
** Don't forget you can ask as many questions as you want. **
"""

# step 1 get company relationship
# c1 -> c3 -> [c5, c6]

# step 2, find land parcels from the companies
# land parcels -> filter_by (companies)
companies = [
    {"id": "c1", "name": "Big Corp A", "parentId": None},
    {"id": "c2", "name": "Big Corp B", "parentId": None},
    {"id": "c3", "name": "Medium Corp A", "parentId": "c1"},
    {"id": "c4", "name": "Medium Corp B", "parentId": "c2"},
    {"id": "c5", "name": "Small Corp A", "parentId": "c3"},
    {"id": "c6", "name": "Small Corp B", "parentId": "c3"},
]


@dataclass
class Company:
    id: str
    name: str
    parentId: str
    children: List[str]


def get_companies(companies: List[Dict[str, str]]) -> Dict[str, Company]:
    result = {}
    for c in companies:
        result[c["id"]] = Company(c["id"], c["name"], c["parentId"], [])

    for id, c in result.items():
        if c.parentId:
            children = result[c.parentId].children
            children.append(id)

    return result


land_parcels = [
    {"id": "l1", "companyId": "c1"},
    {"id": "l2", "companyId": "c2"},
    {"id": "l3", "companyId": "c3"},
    {"id": "l4", "companyId": "c5"},
    {"id": "l5", "companyId": "c5"},
]


def func1():
    return "To Do"


def get_land_parcels(land_parcels: List[Dict[str, str]]) -> Dict[str, List[str]]:
    result = {}
    for lp in land_parcels:
        companyId = lp["companyId"]
        landId = lp["id"]

        lands = result.get(companyId) or []
        lands.append(landId)
        result[companyId] = lands
    return result


# Implement the following function
#  E.g. get_land_parcels_for_company("c1") => ["l1","l3","l4","l5"]
def get_land_parcels_for_company(companies, land_parcels, company_id):
    pass
