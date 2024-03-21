import smtplib
import flet as ft

PASSWORD = "zhul owaw efbz apke"


class MailApp(ft.UserControl):
    def __init__(self):
        super(MailApp, self).__init__()

        self.sender = ft.TextField(
            label="Expéditeur...",
            height=50,
            width=400,
            border_radius=30,
            focused_bgcolor="yellow"
        )
        self.receiver = ft.TextField(
            label="Destinataire...",
            height=50,
            width=400,
            border_radius=30,
            focused_bgcolor="yellow"
        )
        self.subject = ft.TextField(
            height=50,
            width=400,
            label="Objet...",
            prefix_text="SUBJECT:",
            border_radius=30,
            focused_bgcolor="yellow"
        )
        self.body = ft.TextField(
            height=200,
            width=400,
            prefix_text="MESSAGE:",
            multiline=True,
            border_radius=30,
            focused_bgcolor="yellow"
        )
        self.send = ft.ElevatedButton(
            text="Envoyer",
            icon=ft.icons.SEND,
            icon_color="white",
            color="white",
            bgcolor="blue",
            on_click=self.send_email
        )

    def send_email(self, e):
        sender = self.sender.value
        receiver = self.receiver.value
        subject = self.subject.value
        body = self.body.value
        text = f'subject: {subject}\n\n{body}'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, PASSWORD)
        server.sendmail(sender, receiver, text)

        self.receiver.value = ""
        self.sender.value = ""
        self.subject.value = ""
        self.body.value = ""
        self.receiver.update()
        self.sender.update()
        self.subject.update()
        self.body.update()

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.sender,
                    self.receiver,
                    self.subject,
                    self.body,
                    self.send
                ], spacing=10
            )
        )


def main(page: ft.Page):
    mail_app = MailApp()
    page.add(mail_app)


if __name__ == '__main__':
    ft.app(target=main)
