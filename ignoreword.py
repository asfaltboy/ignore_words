import sublime
import sublime_plugin


class Ignoreword(sublime_plugin.EventListener):
    def add_ignore_word(self, word):
        settings = sublime.load_settings('Preferences.sublime-settings')
        ignored_words = settings.get('ignored_words', [])
        if word and word not in ignored_words:
            ignored_words.append(word)
            settings.set('ignored_words', ignored_words)
            sublime.save_settings('Preferences.sublime-settings')

    def on_text_command(self, view, command_name, args):
        if command_name == 'ignore_word':
            sublime.set_timeout_async(lambda: self.add_ignore_word(args['word']))
