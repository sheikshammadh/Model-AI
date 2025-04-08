from kivy.uix.textinput import TextInput  # 🔥 New import

class ChatBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.chat_label = Label(
            size_hint_y=None,
            text_size=(340, None),
            halign='left',
            valign='top',
            markup=True
        )
        self.chat_label.bind(texture_size=self.update_height)

        self.scroll = ScrollView(size_hint=(1, 0.75))  # 🔥 Changed size_hint
        self.scroll.add_widget(self.chat_label)
        self.add_widget(self.scroll)

        self.voice_button = Button(
            text="🎙️ Speak to AI",
            size_hint=(1, 0.1),  # 🔥 Adjusted size
            font_size=22,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.voice_button.bind(on_press=lambda x: self.start_listening())
        self.add_widget(self.voice_button)

        # 🔥 New UI: Text input and Send button
        bottom_row = BoxLayout(size_hint=(1, 0.1), spacing=5)
        self.text_input = TextInput(
            multiline=False,
            hint_text="Type your message here...",
            font_size=18
        )
        send_button = Button(
            text="Send",
            size_hint_x=0.3,
            background_color=(0.2, 0.7, 0.3, 1),
            font_size=18
        )
        send_button.bind(on_press=self.send_text_input)
        bottom_row.add_widget(self.text_input)
        bottom_row.add_widget(send_button)
        self.add_widget(bottom_row)

    def send_text_input(self, instance):
        user_text = self.text_input.text.strip()
        if user_text:
            self.text_input.text = ""
            self.respond_to_user(user_text)

    # ... rest of the methods remain unchanged ...
``
