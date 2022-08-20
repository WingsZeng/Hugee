import sublime
import sublime_plugin
import datetime
from .settings import settings


class SaveListener(sublime_plugin.ViewEventListener):
    def on_pre_save(self):
        """
        Called on pre save to auto fill lastmod.
        """
        if settings is not None and settings.get('auto_fill_lastmod'):
            self.view.run_command("hugee_auto_fill_lastmod")


class HugeeFillLastmodCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """
        Update lastmod in the header
        """
        filename = self.view.file_name()
        if filename[-3:] == '.md':
            prefix = 'lastmod: '
            time_regex = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
            regex = prefix + time_regex
            region = self.view.find(regex, 0)
            if not region.empty():
                region = sublime.Region(region.a + len(prefix), region.b)
                time = datetime.datetime.now()
                time_str = time.strftime("%Y-%m-%dT%H:%M:%S")
                self.view.replace(edit, region, time_str)
