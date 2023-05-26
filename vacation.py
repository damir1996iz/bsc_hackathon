from datetime import datetime


class Vacation:
    """
    Класс отпуска пользователя
    """
    fio: str
    job: str
    num_days: int
    start_date: datetime
    end_date: datetime
    bsc_approvers: [str]
    project_approvers: [str]

    def __init__(self, fio, job, num_days, start_date, end_date, bsc_approvers, project_approvers):
        self.fio = fio
        self.job = job
        self.num_days = num_days
        self.start_date = start_date
        self.end_date = end_date
        self.bsc_approvers = bsc_approvers
        self.project_approvers = project_approvers
