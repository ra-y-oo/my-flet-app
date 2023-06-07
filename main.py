import flet as ft
from flet import colors, Image

def main(page:ft.Page):
    page.window_width = 400
    page.window_height = 720
    page.appbar = ft.AppBar(title=ft.Text("LOGIN FORM"), bgcolor=colors.BLUE, center_title=True)
    img =Image(
        src=f"https://img.freepik.com/free-vector/mobile-login-concept-illustration_114360-83.jpg?w=2000",
          fit="contain"
          )
    login = ft.TextField(label="Email", hint_text="example@email.com")
    password = ft.TextField(label="Password", password=True,can_reveal_password=True, hint_text="input password")
    btn = ft.FilledButton(text="Login", height=45)
    page.add(
        ft.Container(
        content=ft.Column([
        img,
        login,
        password,
        btn], spacing=40)
        )
        )

ft.app(target=main)