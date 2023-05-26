from python_docx_replace import docx_replace
from docx import Document


def format_file(
        job: str,
        fio: str,
        num_days: str,
        start_day: str,
        start_month: str,
        start_year: str,
        end_day: str,
        end_month: str,
        end_year: str):
    """

    Пример:
    format_file(
        job="Старший инженер-программист",
        fio="Гильмутдинов Дамир Тахирович",
        num_days="14",
        start_day="31",
        start_month="ноября",
        start_year="2023",
        end_day="1",
        end_month="декабря",
        end_year="2023"
    )

    :param job: Должность
    :param fio: ФИО
    :param num_days: Число дней отпуска
    :param start_day: Дата начала
    :param start_month: Месяц начала
    :param start_year: Год начала
    :param end_day: День конца
    :param end_month: Месяц конца
    :param end_year: Год конца
    :return:
    """
    doc = Document("otpusk.docx")
    docx_replace(
        doc,
        job=job,
        fio=fio,
        num_days=num_days,
        start_day=start_day,
        start_month=start_month,
        start_year=start_year,
        end_day=end_day,
        end_month=end_month,
        end_year=end_year
    )
    doc.save("otpusk_out.docx")
