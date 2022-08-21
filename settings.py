import sublime
import sublime_plugin


def getSettings() -> sublime.Settings:
    """
    Gets the plugin settings.

    :returns:   The settings.
    :rtype:     sublime Settings
    """
    settings = sublime.load_settings('hugee.sublime-settings')
    if len(settings.get('site_path')) == 0:
        window = sublime.active_window()
        project_data = window.extract_variables()
        folder_path = project_data['folder']
        settings.set('site_path', folder_path)
    return settings
