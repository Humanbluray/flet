from email.message import EmailMessage
import ssl
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
            border_radius=30,
            focused_bgcolor="yellow"
        )
        self.body = ft.TextField(
            height=200,
            width=400,
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
        """Send an e-mail"""
        context = ssl.create_default_context()
        sender = self.sender.value
        receiver = self.receiver.value
        subject = self.subject.value
        body = self.body.value

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)

        em = EmailMessage()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password=PASSWORD)
            smtp.sendmail(sender, receiver, em.as_string())

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


# def send_mail(sender, receiver, subject, body):
#     """Send an e-mail"""
#     context = ssl.create_default_context()
#     em = EmailMessage()
#     em['From'] = sender
#     em['To'] = receiver
#     em['Subject'] = subject
#     em.set_content(body)
#
#     em = EmailMessage()
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(sender, password=PASSWORD)
#         smtp.sendmail(sender, receiver, em.as_string())
