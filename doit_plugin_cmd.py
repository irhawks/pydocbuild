from doit.cmd_base import Command

class SampleCmd(Command):
    doc_purpose = "sample command plugin"

    def execute(self, params, args):
        print("This sample command does nothing!")
