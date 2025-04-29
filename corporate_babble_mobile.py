import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.utils import get_color_from_hex

corporate_words_1 = ['proactively', 'asynchronously', 'synergistically', 'seamlessly', 'dynamically', 'robustly', 'strategically', 'iteratively', 'scalably', 'holistically', 'flexibly', 'optimally', 'efficiently']
corporate_words_2 = ['circle back on', 'leverage', 'actualize', 'align on', 'implement', 'touch base on', 'audit', 'make strides towards', 'onboard', 'streamline', 'facilitate', 'pivot towards', 'optimize']
corporate_words_3 = ['stakeholders', 'opportunities', 'deliverables', 'strategy', 'bandwidth', 'buy-ins', 'portfolios', 'touchpoints', 'pipelines', 'initiatives', 'frameworks', 'ecosystems', 'value propositions', 'workstreams']

class JargonApp(App):
    def build(self):
        self.title = "Corporate Jargon Generator"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.phrase_label = Label(
            text="",
            font_size=20,
            color=[1, 1, 1, 1],  # White text
            halign='center',
            valign='middle'
        )
        self.phrase_label.bind(size=self.phrase_label.setter('text_size'))  # enable wrapping
        layout.add_widget(self.phrase_label)

        # Pastel green generate button
        generate_button = Button(
            text="Generate Phrase",
            size_hint=(1, 0.2),
            font_size=18,
            background_normal='',
            background_color=get_color_from_hex("#A8E6A1"),  # pastel green
            color=[0, 0, 0, 1],  # black text
            on_press=self.generate_phrase
        )
        layout.add_widget(generate_button)

        # Pure white copy button
        copy_button = Button(
            text="Copy to Clipboard",
            size_hint=(1, 0.15),
            font_size=14,
            background_normal='',
            background_color=get_color_from_hex("#FFFFFF"),  # pure white
            color=[0, 0, 0, 1],  # black text
            on_press=self.copy_to_clipboard
        )
        layout.add_widget(copy_button)

        return layout

    def generate_phrase(self, instance):
        phrase = f"{random.choice(corporate_words_1)} {random.choice(corporate_words_2)} {random.choice(corporate_words_3)}"
        self.phrase_label.text = phrase

    def copy_to_clipboard(self, instance):
        phrase = self.phrase_label.text
        if phrase:
            Clipboard.copy(phrase)

if __name__ == "__main__":
    JargonApp().run()
