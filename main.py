import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle

# Set background color
Window.clearcolor = (0.06, 0.09, 0.16, 1)

class PrayerTimesApp(App):
    def build(self):
        self.title = "مواقيت الصلاة - Prayer Times"
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        header = Label(
            text="[b]مواقيت الصلاة[/b]",
            markup=True,
            font_size='24sp',
            size_hint_y=None,
            height=50,
            color=(0.22, 0.74, 0.97, 1)
        )
        main_layout.add_widget(header)
        
        # Next Prayer Card
        card = BoxLayout(orientation='vertical', padding=15, spacing=5, size_hint_y=None, height=120)
        with card.canvas.before:
            Color(0.01, 0.52, 0.78, 1)
            self.rect = RoundedRectangle(size=card.size, pos=card.pos, radius=[15])
        card.bind(size=self._update_rect, pos=self._update_rect)
        
        next_lbl = Label(text="الصلاة القادمة: صلاة العصر", font_size='18sp', bold=True, color=(1, 1, 1, 1))
        timer_lbl = Label(text="متبقي: 01:45:20", font_size='16sp', color=(0.9, 0.9, 0.9, 1))
        
        card.add_widget(next_lbl)
        card.add_widget(timer_lbl)
        main_layout.add_widget(card)
        
        # Prayer Table
        prayers = [
            ("الفجر", "04:15 AM"),
            ("الشروق", "05:45 AM"),
            ("الظهر", "12:30 PM"),
            ("العصر", "04:05 PM"),
            ("المغرب", "07:15 PM"),
            ("العشاء", "08:45 PM")
        ]
        
        scroll = ScrollView()
        list_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        
        for name, time_str in prayers:
            row = BoxLayout(orientation='horizontal', padding=10, size_hint_y=None, height=50)
            with row.canvas.before:
                Color(0.12, 0.16, 0.23, 1)
                RoundedRectangle(size=row.size, pos=row.pos, radius=[8])
            
            p_name = Label(text=name, font_size='16sp', color=(1, 1, 1, 1), halign='right')
            p_time = Label(text=time_str, font_size='16sp', color=(0.22, 0.74, 0.97, 1), halign='left')
            
            row.add_widget(p_time)
            row.add_widget(p_name)
            list_layout.add_widget(row)
            
        scroll.add_widget(list_layout)
        main_layout.add_widget(scroll)
        
        return main_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    PrayerTimesApp().run()
