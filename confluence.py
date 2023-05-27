from atlassian import Confluence
from bs4 import BeautifulSoup
from datetime import datetime

from auth import CONFL_USER, CONFL_PASS
from vacation import Vacation


def get_user_vacations(user_name: str):
    """
    Функция получения списка отпусков пользователя

    Пример: get_user_vacations("Гильмутдинов Дамир Тахирович")

    :param user_name ФИО пользователя
    :return: Список с отпусками или пустой список
    """
    confluence = Confluence(
        url='https://cz-support.finshape.com/confl',
        username=CONFL_USER,
        password=CONFL_PASS
    )

    page = confluence.get_page_by_id("213857043", "space,body.view,version,container")

    result = []

    soup = BeautifulSoup(page["body"]["view"]["value"], features="html.parser")
    table = soup.find("div", {"class": "table-wrap"})
    rows = table.find_all("tr")[1:]
    for row in rows:
        columns = row.find_all("td", {"class": "confluenceTd"})
        if columns[0].text == user_name:

            if (not columns[1].text) or (not columns[2].text) or (not columns[5].text) or (not columns[6].text):
                raise ValueError("Incorrect table")

            result.append(
                Vacation(
                    fio=columns[0].text,
                    job=columns[1].text,
                    num_days=columns[2].text,
                    start_date=string_to_datetime(columns[3].text),
                    end_date=string_to_datetime(columns[4].text),
                    bsc_approvers=columns[5].text,
                    project_approvers=columns[6].text
                )
            )
    return result


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
        name = columns[1].find("h4").text.strip()
        user_tg = columns[3].find("div", {"class": "content-wrapper"}).find_all("p")[1].text
        data[name] = user_tg.strip()

    for key, value in data.items():
        if value == tg:
            return key


def string_to_datetime(string: str):
    try:
        return datetime.strptime(string, "%d-%m-%Y")
    except:
        return ""
