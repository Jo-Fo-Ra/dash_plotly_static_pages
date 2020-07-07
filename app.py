import dash_html_components as html
import dash

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            children=[

                html.H1(
                    'Title of the first page'
                )
            ],
            className='page'
        ),

        html.Div(
            html.H1(
                'Title of the second page'
            ),
            className='page'
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True,
                   dev_tools_ui=False, #If true, the browser printer adds the tool-button onto the page
                   port=8050)