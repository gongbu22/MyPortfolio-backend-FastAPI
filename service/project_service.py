from typing import List
from models.projects import myportfolio

async def get_all_projects() -> List[myportfolio]:
    projects = await myportfolio.find_all().to_list()
    # print(f"✅ find_all 결과: {projects}")
    return projects

async def get_detail(project_num: str) -> myportfolio:
    project = await myportfolio.find_one(myportfolio.num == project_num)
    return project