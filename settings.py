import sublime
import sublime_plugin

settings = None

class ProjectLoadListener(sublime_plugin.EventListener):
    def on_load_project(self, window):
        global settings
        print('hugee load settings')
        settings = sublime.load_settings('hugee.sublime-settings')
        if len(settings.get('site_path')) == 0:
            project_data = window.extract_variables()
            folder_path = project_data['folder']
            settings.set('site_path', folder_path)
