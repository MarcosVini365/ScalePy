import flet as ft
from ScalePy.core.gerador_escalas import gerar_escala

def main(page: ft.page):
    page.title = 'ScalePy'

    page.theme_mode = 'light'
    lista = []

    def mode_page(e):
        mode = page.theme_mode
        global color_text

        if mode == 'light':
            page.theme_mode = 'dark'
        else:
            page.theme_mode = 'light'
        page.update()

    def button_clicked_scale(e):
        lista.clear()
        key = str(select_tom.value).lower()
        scale = str(select_scale.value).lower()

        if key == 'none' or scale == 'none':
            page.snack_bar.open = True
            page.update()
        else:
            lista_escala = gerar_escala(key, scale)

            titulo_principal.opacity = 100
            for i in lista_escala:
                lista.append(
                ft.ResponsiveRow(
                    expand=True,
                    controls=[
                        ft.Container(
                            col={"sm": 9, "md": 10, "xl": 12},
                            alignment=ft.alignment.center,
                            content=ft.Text(i, color=ft.colors.BLACK, size=16, text_align=ft.alignment.center),
                            width=70,
                            height=70,
                            border_radius=6,
                            bgcolor=ft.colors.WHITE,
                            border=ft.border.all(2, ft.colors.BLACK12),
                        ),]
                )
            )
        page.update()

    page.snack_bar = ft.SnackBar(
        content=ft.Text("Por favor, preencha todos os campos."),
        action="Ok!",
    )

    appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text('ScalePy'),
        bgcolor=ft.colors.ORANGE,
        actions=[
            ft.IconButton(
                icon=ft.icons.DARK_MODE,
                on_click=mode_page
            )
        ]

    )

    titulo_principal = ft.Container(
        content=ft.Text('Escala', color=ft.colors.ON_SURFACE, size=16),
        alignment=ft.alignment.center,
        opacity=0,
    )

    select_tom = ft.Dropdown(
        width=100,
        hint_text="Key",
        options=[
            ft.dropdown.Option('C'),
            ft.dropdown.Option('D'),
            ft.dropdown.Option('E'),
            ft.dropdown.Option('F'),
            ft.dropdown.Option('G'),
            ft.dropdown.Option('A'),
            ft.dropdown.Option('B'),
        ],
    )
    select_scale = ft.Dropdown(
        width=250,
        hint_text="Scale",
        options=[
            ft.dropdown.Option('Major'),
            ft.dropdown.Option('Minor'),
        ],
    )

    button_selector = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                text='Atualizar',
                icon=ft.icons.MUSIC_NOTE_SHARP,
                on_click=button_clicked_scale,
            )
        ]
    )

    items=[
        select_tom,
        select_scale,
    ]

    bloco_01 = ft.Row(
        controls=items,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    bloco_02 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=lista
    )


    page.add(
        appbar,
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    bloco_01,
                    button_selector,
                    ft.Divider(),
                    titulo_principal,
                    bloco_02,
                ]
            )
        )
    )