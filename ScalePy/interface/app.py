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
                ft.Column(
                    col={"xs": 3,"sm": 2, "md": 2, "xl": 1},
                    spacing=0,
                    controls=[
                        ft.ElevatedButton(
                            width=70,
                            height=70,
                            text=i,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(radius=30),

                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        page.update()

    # POPUP: é apresentado quando não é selecionado uma tonalidade
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Por favor, preencha todos os campos."),
        action="Ok!",
    )

    # AppBar
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

    select_tom = ft.Dropdown(
        width=100,
        hint_text="Key",
        options=[
            ft.dropdown.Option('C'),
            ft.dropdown.Option('C#'),
            ft.dropdown.Option('D'),
            ft.dropdown.Option('D#'),
            ft.dropdown.Option('E'),
            ft.dropdown.Option('F'),
            ft.dropdown.Option('F#'),
            ft.dropdown.Option('G'),
            ft.dropdown.Option('G#'),
            ft.dropdown.Option('A'),
            ft.dropdown.Option('A#'),
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

    # Titulo referente ao setor
    titulo_principal = ft.Container(
        content=ft.Text('Escala', color=ft.colors.ON_SURFACE, size=16),
        alignment=ft.alignment.center,
        opacity=0,
    )

    items=[
        select_tom,
        select_scale,
    ]

    # Bloco de Seleção de Tonalidade e Escala
    bloco_01 = ft.Row(
        controls=items,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    # Bloco de Visualização da escala gerada
    bloco_02 = ft.ResponsiveRow(
        alignment=ft.MainAxisAlignment.CENTER,
        run_spacing=20,
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