import getpass

from crontab import CronTab


class schedule:

    def __init__(self):
        '''
            crontab 에 schedule job 을 관리 
        '''
        self.user = getpass.getuser()
        # File logger Setting

    def create_job(self, command, comment):
        '''
        Crontab 에 작업을 등록
        - 1시간 마다 command 작업을 수행하도록 등록
        - crontab 의 작업 등록시 추후 식별을 위해 comment 를 함께 등록

        Args:
            command: crontab 작업을 할 command
            comment: crontab 작업 comment

        '''
        cron = CronTab(user=self.user)
        job = cron.new(command=command, comment=comment)
        job.hour.every(1)
        cron.write()

    def list_job(self):
        '''
        Crontab 에 등록된 작업 목록 조회 

        Returns: crontab job 리스트
                 ex) [<CronItem '* * 1 * * date >> /home/jjeaby/date.log # date_now'>]


        '''
        cron_job_list = []
        cron = CronTab(user=self.user)
        for item in cron:
            cron_job_list.append(item)
        cron.write()
        return cron_job_list

    def remove_all(self):
        '''
            Crontab 에 등록된 모든 작업을 삭제
        '''
        cron = CronTab(user=self.user)
        cron.remove_all()
        for item in cron:
            print(item)
        cron.write()

    def remove_job(self, comment):
        '''
            Crontab 에 등록된 모든 작업 중 comment 가 동일한 작업을 삭제

        Args:
            comment: crontab 의 작업 식별자

        '''
        cron = CronTab(user=self.user)
        for job in cron:
            if job.comment == comment:
                cron.remove(job)
                break
        cron.write()


if __name__ == '__main__':
    sc = schedule()
    sc.remove_job(comment='date_now')
    sc.list_job()
    sc.create_job(command='date >> /home/jjeaby/date.log', comment='date_now')
    sc.list_job()
