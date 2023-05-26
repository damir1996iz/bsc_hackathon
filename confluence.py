from atlassian import Confluence
from bs4 import BeautifulSoup
from auth import CONFL_USER, CONFL_PASS


def get_username_by_tg(tg: str):
    confluence = Confluence(
        url='https://cz-support.finshape.com/confl',
        username=CONFL_USER,
        password=CONFL_PASS
    )

    page = confluence.get_page_by_id("169810267", "space,body.view,version,container")

    data = {}

    soup = BeautifulSoup(page["body"]["view"]["value"], features="html.parser")
    table = soup.find("div", {"class": "table-wrap"})
    rows = table.find_all("tr")[3:]
    for r in rows:
        columns = r.find_all("td")
        name = columns[1].find("h4").text
        user_tg = columns[3].find("div", {"class": "content-wrapper"}).find_all("p")[1].text
        data[name] = user_tg

    for key, value in data.items():
        if value == tg:
            return key
