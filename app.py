
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from dash import Dash, _dash_renderer, dcc, callback, Input, Output, State, clientside_callback,  ClientsideFunction
from components import components_list

_dash_renderer._set_react_version("18.2.0")

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

header = dmc.Group(
            justify='space-between',
            className = 'header-inner-container',
            px = 10,
            children = [
                dmc.Burger(id="burger-button", opened=False, hiddenFrom="md"),
                dmc.Paper(
                    className = 'logo-image',
                    children = [
                        dmc.Image(src="/assets/baylek.png",  className='image-width'),
                    ]
                ),
                dmc.ActionIcon(
                    id = 'color-scheme-toggle',
                    n_clicks=0, 
                    variant= "transparent",
                    children = [
                        DashIconify(icon="ic:baseline-light-mode",  color='100%')
                    ]
                ) 
            ]
        )



app = Dash(external_stylesheets=stylesheets)
server = app.server

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    children = [
        dmc.AppShell(
            id="app-shell",
            navbar={ "breakpoint": "md", "collapsed": {"mobile": True}},
            children = [
                dmc.AppShellHeader(header),
                dmc.AppShellNavbar(dmc.Box(dmc.Badge("Side Bar")), withBorder=False),
                dmc.AppShellMain(components_list, p=20),
                dmc.AppShellFooter(dmc.Badge("Footer"), withBorder=False),
                dmc.AppShellAside(dmc.Center(dmc.Badge("Aside")),  withBorder=False),
            ]
        )
    ]   
)

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher_callback'
    ),
    Output("mantine-provider", "theme"),
    Output("mantine-provider", "forceColorScheme"),
    Output("color-scheme-toggle", "children"),
    Input("color-scheme-toggle", "n_clicks")

)
clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='side_bar_toggle'
    ),
    Output("app-shell", "navbar"),
    Input("burger-button", "opened"),
    State("app-shell", "navbar"),

)

if __name__ == "__main__":
    app.run_server(debug=True, port= 8053)

