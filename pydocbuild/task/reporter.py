from doit.reporter import ConsoleReporter

class MyReporter(ConsoleReporter):
    def execute_task(self, task):
        self.outstream.write('Reporter : Running --> %s\n' % task.title())
        self.outstream.write('Reporter : %s depends --> %s\n' % (task.title(), task.task_dep) )

DOIT_CONFIG = {
    #'default_tasks': ['t3']
    'backend': 'json',
    'reporter': MyReporter,
    'status' : True,
    'continue': True,
    'verbosity': 2
}

