import sublime
import sublime_plugin
import subprocess
from . import hugocmd

class HugoVersionCommand(sublime_plugin.WindowCommand):
    def run(self):
        """
        Run `hugo version`

        Show the result in a dialog,
        Or print error
        """
        result = hugocmd.run(['hugo', 'version'])
        if result.status is hugocmd.Status.SUCCESS:
            sublime.message_dialog(result.output)
        elif result.status is not hugocmd.Status.UNKNOWN:
            sublime.error_message(result.output)
        else:
            # TODO: log it
            print(result.e)


# TODO: 配置文件参数
# class HugoServerCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         result = hugocmd.run(['hugo', 'server'])

class HugoBuildCommand(sublime_plugin.WindowCommand):
    def run(self):
        """
        Run `hugo` to build
        """
        result = hugocmd.run(['hugo'])
        if result.status is hugocmd.Status.SUCCESS:
            print(result.output)
        elif result.status is not hugocmd.Status.UNKNOWN:
            sublime.message_dialog(result.output)
        else:
            # TODO: log it
            print(result.e)
