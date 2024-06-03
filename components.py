import dash_mantine_components as dmc
from dash import dcc

from dash_iconify import DashIconify
def iconify(icon, color = 'dark', width=30):
    return DashIconify(icon=icon,  color=color, width = width)
text_style = {
    "border":"1px solid #f7f7f7",
    "color":"#a39e6c",
    "margin":"30px 0px",
    "padding":"10px",
    "borderRadius":'10px',
    "background":"#f7f7f7",
    "fontSize":"25px"


    }

__js = 'assets/theme.js'
__py = 'app.py'
__css = 'assets/appshell.css'
 
with open(__js, 'r') as file:
    __js = file.read()

with open(__py, 'r') as file:
    __py = file.read()
    
with open(__css, 'r') as file:
    __css = file.read()
 

elements = [
    {"position": 6, "mass": 12.011, "symbol": "C", "name": "Carbon"},
    {"position": 7, "mass": 14.007, "symbol": "N", "name": "Nitrogen"},
    {"position": 39, "mass": 88.906, "symbol": "Y", "name": "Yttrium"},
    {"position": 56, "mass": 137.33, "symbol": "Ba", "name": "Barium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
]

rows = [
    dmc.TableTr(
        [
            dmc.TableTd(element["position"]),
            dmc.TableTd(element["name"]),
            dmc.TableTd(element["symbol"]),
            dmc.TableTd(element["mass"]),
        ]
    )
    for element in elements
]

head = dmc.TableThead(
    dmc.TableTr(
        [
            dmc.TableTh("Element Position"),
            dmc.TableTh("Element Name"),
            dmc.TableTh("Symbol"),
            dmc.TableTh("Atomic Mass"),
        ]
    )
)
body = dmc.TableTbody(rows)
caption = dmc.TableCaption("Some elements from periodic table")



components_list = [               

              
dmc.Text('Accordion', style = text_style),
dmc.Accordion(
    value=["javascript"],
    multiple=True,
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl("Javascript"),
                dmc.AccordionPanel(
                   dmc.CodeHighlight(
                    language="javascript",
                    code=__js,
                )
                ),
            ],
            value="Javascript",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl("CSS"),
                dmc.AccordionPanel(
                        dmc.CodeHighlight(
                    language="css",
                    code=__css,
                )
                ),
            ],
            value="css",
        ),
            dmc.AccordionItem(
            [
                dmc.AccordionControl("Python"),
                dmc.AccordionPanel(
                          dmc.CodeHighlight(
                    language="python",
                    code=__py,
                )
                ),
            ],
            value="pyhton",
        ),
    ],
),
dmc.Text('Avatar', style = text_style),
dmc.Group(
    children=[
        dmc.Avatar(
            src="https://avatars.githubusercontent.com/u/91216500?v=4", radius="xl"
        ),
        # default placeholder
        dmc.Avatar(radius="xl"),
        # initials
        dmc.Avatar("MK", color="cyan", radius="xl"),
        # icon
        dmc.Avatar(DashIconify(icon="radix-icons:star"), color="blue", radius="xl"),
    ],
),
dmc.Text('Badge',style = text_style),
dmc.Group(
    [
        dmc.Badge("Default light badge"),
        dmc.Badge("Dot badge", variant="dot"),
        dmc.Badge("Outline badge", variant="outline"),
        dmc.Badge("Filled badge", variant="filled"),
    ]
),
dmc.Text('Card',style = text_style),
dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-8.png",
                h=160,
                alt="Norway",
            )
        ),
        dmc.Group(
            [
                dmc.Text("Norway Fjord Adventures", fw=500),
                dmc.Badge("On Sale", color="pink"),
            ],
            justify="space-between",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and "
            "around the fjords of Norway",
            size="sm",
            c="dimmed",
        ),
        dmc.Button(
            "Book classic tour now",
            color="blue",
            fullWidth=True,
            mt="md",
            radius="md",
        ),
    ],
    
    shadow="sm",
    radius="md",
    w=350,
),
dmc.Text('Indicator',style = text_style),
dmc.Indicator(
    dmc.Avatar(
        size="lg",
        radius="sm",
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
    ),
    inline=True,
    size=16,
    label="New",
),
dmc.Text('Kbd',style = text_style),
dmc.Box([dmc.Kbd("⌘"), " + ", dmc.Kbd("shift"), " + ", dmc.Kbd("M")]),
dmc.Text('Spoiler',style = text_style),
dmc.Spoiler(
    showLabel="Show more",
    hideLabel="Hide",
    maxHeight=50,
    children=[dmc.Text("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.""")],
),
dmc.Text('ThemeIcon',style = text_style),
dmc.ThemeIcon(
    size="xl",
    color="indigo",
    variant="filled",
    children=DashIconify(icon="tabler:photo", width=25)
),
dmc.Text('Timeline',style = text_style),
dmc.Timeline(
    active=1,
    bulletSize=15,
    lineWidth=2,
    children=[
        dmc.TimelineItem(
            title="New Branch",
            children=[
                dmc.Text(
                    [
                        "You've created new branch ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                        " from master",
                    ],
                    c="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Commits",
            children=[
                dmc.Text(
                    [
                        "You've pushed 23 commits to ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                    ],
                    c="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Pull Request",
            lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "You've submitted a pull request ",
                        dmc.Anchor(
                            "Fix incorrect notification message (#178)",
                            href="#",
                            size="sm",
                        ),
                    ],
                    c="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    [
                        dmc.Anchor(
                            "AnnMarieW",
                            href="https://github.com/AnnMarieW",
                            size="sm",
                        ),
                        " left a comment on your pull request",
                    ],
                    c="dimmed",
                    size="sm",
                ),
            ],
            title="Code Review",
        ),
    ],
),
dmc.Text('ActionIcon',style = text_style),
 dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line", width=20),
            size="lg",
            variant="filled",
            id="action-icon",
            n_clicks=0,
            mb=10,
        ),
dmc.Text('Button',style = text_style),
dmc.Group(
    [
        dmc.Button("Default button"),
        dmc.Button("Subtle button", variant="subtle"),
        dmc.Button("Gradient button", variant="gradient"),
        dmc.Button("Filled button", variant="filled"),
        dmc.Button("Light button", variant="light"),
        dmc.Button("Outline button", variant="outline"),
    ]
),
dmc.Text('Menu',style = text_style),
dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button("Click for options!")),
        dmc.MenuDropdown(
            [
                dmc.MenuItem(
                    "External Link",
                    href="https://www.github.com/snehilvj",
                    target="_blank",
                    leftSection=DashIconify(icon="radix-icons:external-link"),
                ),
                dmc.MenuItem("Useless Button", n_clicks=0),
            ]
        ),
    ],
    transitionProps={"transition": "rotate-right", "duration": 150},
),
dmc.Text('Tooltip',style = text_style),
dmc.Group(
    [
        dmc.Tooltip(
            dmc.Button("Default arrow", variant="outline"),
            label="Default arrow",
            withArrow=True,
            opened=True,
        ),
        dmc.Tooltip(
            dmc.Button("With size", variant="outline"),
            label="Arrow with size",
            withArrow=True,
            arrowSize=6,
            opened=True,
        ),
    ],
    mt=25,
),
dmc.Text('Alert',style = text_style),
dmc.Alert(
    "Something happened! You made a mistake and there is no going back, your data was lost forever!",
    title="Simple Alert!",
),

dmc.Text('Loader',style = text_style),
dmc.Group([dmc.Loader(color="red", size="md", type="oval"),dmc.Loader(color="red", size="md", type="dots")]),
dmc.Title(f"This is h1 title", order=1),    
dmc.Text('Anchor',style = text_style),
dmc.Anchor(
    "Dash Mantine Components Announcement",
    href="https://community.plotly.com/t/dash-mantine-components/58414",
),
dmc.Text('Breadcrumbs',style = text_style),
   dmc.Breadcrumbs(
            children=[
                dcc.Link("Home", href="/"),
                dcc.Link("Dash Mantine Components", href="/"),
                dcc.Link("Breadcrumbs", href="/components/breadcrumbs"),
            ],
        ),
dmc.Text('Group',style = text_style),
dmc.Group(
    [
        dmc.Burger(),
        dmc.Burger(color="red"),
        dmc.Burger(color="green"),
    ]
),
dmc.Text('NavLink',style = text_style),
dmc.Box(
    [
        dmc.NavLink(
            label="With icon",
            leftSection=iconify(icon="bi:house-door-fill"),
        ),
        dmc.NavLink(
            label="With right section",
            leftSection=iconify(icon="tabler:gauge"),
            rightSection=iconify(icon="tabler-chevron-right"),
        ),
        dmc.NavLink(
            label="Disabled",
            leftSection=iconify(icon="tabler:circle-off"),
            disabled=True,
        ),
        dmc.NavLink(
            label="With description",
            description="Additional information",
            leftSection=dmc.Badge(
                "3", size="xs", variant="filled", color="red", w=16, h=16, p=0
            ),
        ),
        dmc.NavLink(
            label="Active subtle",
            leftSection=iconify(icon="tabler:activity"),
            rightSection=iconify(icon="tabler-chevron-right"),
            variant="subtle",
            active=True,
        ),
        dmc.NavLink(
            label="Active light",
            leftSection=iconify(icon="tabler:activity"),
            rightSection=iconify(icon="tabler-chevron-right"),
            active=True,
        ),
        dmc.NavLink(
            label="Active filled",
            leftSection=iconify(icon="tabler:activity"),
            rightSection=iconify(icon="tabler-chevron-right"),
            variant="filled",
            active=True,
        ),
    ],
    style={"width": 240},
),
dmc.Text('Pagination',style = text_style),
dmc.Stack(
    [
        dmc.Pagination(total=20, siblings=1, value=10),
        dmc.Pagination(total=20, siblings=2, value=10, my=15),
        dmc.Pagination(total=20, siblings=3, value=10),
    ]
),
dmc.Text('Stepper',style = text_style),
dmc.Box(
    [
        dmc.Stepper(
            id="stepper-basic-usage",
            active=1,
            children=[
                dmc.StepperStep(
                    label="First step",
                    description="Create an account",
                    children=dmc.Text("Step 1 content: Create an account", ta="center"),
                ),
                dmc.StepperStep(
                    label="Second step",
                    description="Verify email",
                    children=dmc.Text("Step 2 content: Verify email", ta="center"),
                ),
                dmc.StepperStep(
                    label="Final step",
                    description="Get full access",
                    children=dmc.Text("Step 3 content: Get full access", ta="center"),
                ),
                dmc.StepperCompleted(
                    children=dmc.Text(
                        "Completed, click back button to get to previous step",
                        ta="center",
                    )
                ),
            ],
        ),
        dmc.Group(
            justify="center",
            mt="xl",
            children=[
                dmc.Button("Back", id="back-basic-usage", variant="default"),
                dmc.Button("Next step", id="next-basic-usage"),
            ],
        ),
    ]
),

dmc.Text('Typography',style = text_style),
dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ]
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery"),
        dmc.TabsPanel("Messages tab content", value="messages"),
        dmc.TabsPanel("Settings tab content", value="settings"),
    ],
    color="red",
    orientation="vertical",
),


dmc.Text('Typography',style = text_style),
dmc.Blockquote(
    "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.",
    cite="- Marcus Aurelius , Meditations",
),
dmc.Text('Typography',style = text_style),


dmc.Group(
    children=[
        dmc.Code("import collections", color=color) for color in ["red", "blue", "green", "pink"]
    ],
),
dmc.Text('CodeHighlight',style = text_style),
dmc.CodeHighlight(
    language="python",
    code="""# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, summ = nums[0], nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            summ = max(summ, curr)
        return summ""",
),
dmc.Text('Highlight',style = text_style),
dmc.Highlight(
    "Highlight this, definitely this and also this!", highlight="this"
),
dmc.Text('List',style = text_style),
dmc.List(
    icon=dmc.ThemeIcon(
        DashIconify(icon="radix-icons:check-circled", width=16),
        radius="xl",
        color="teal",
        size=24,
    ),
    size="sm",
    spacing="sm",
    children=[
        dmc.ListItem("Join our Discord Community."),
        dmc.ListItem("Install python virtual environment."),
        dmc.ListItem(
            dmc.Text(["Install npm dependencies with ", dmc.Code("npm install")])
        ),
        dmc.ListItem(
            dmc.Text(["Add your new component in ", dmc.Code("src/lib/components.")])
        ),
        dmc.ListItem(
            "Raise a PR, including an example to reproduce the changes contributed by the PR.",
            icon=dmc.ThemeIcon(
                DashIconify(icon="radix-icons:pie-chart", width=16),
                radius="xl",
                color="blue",
                size=24,
            ),
        ),
    ],
),
dmc.Text('Highlight',style = text_style),
dmc.Text(
    ["Highlight ", dmc.Mark("this section", color="cyan"), " of the text."]
),
dmc.Text('Table',style = text_style),



dmc.Table([head, body, caption]),
dmc.Text('Text',style = text_style),
dmc.Box(
    [
        dmc.Text("Extra small text", size="xs"),
        dmc.Text("Small text", size="sm"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Large text", size="lg"),
        dmc.Text("Extra large text", size="xl"),
        dmc.Text("Semi bold", fw=500),
        dmc.Text("Bold", fw=700),
        dmc.Text("Underlined", td="underline"),
        dmc.Text("Red text", c="red"),
        dmc.Text("Blue text", c="blue"),
        dmc.Text("Gray text", c="gray"),
        dmc.Text("Uppercase", tt="uppercase"),
        dmc.Text("capitalized text", tt="capitalize"),
        dmc.Text("Aligned to center", ta="center"),
        dmc.Text("Aligned to right", ta="right"),
    ]
),
dmc.Text('Title',style = text_style),


dmc.Box(
    [
        dmc.Title(f"This is h1 title", order=1),
        dmc.Title(f"This is h2 title", order=2),
        dmc.Title(f"This is h3 title", order=3),
        dmc.Title(f"This is h4 title", order=4),
        dmc.Title(f"This is h5 title", order=5),
        dmc.Title(f"This is h6 title", order=6),
    ]
),
dmc.Text('CheckboxGroup',style = text_style),
 dmc.CheckboxGroup(
            id="checkbox-group",
            label="Select your favorite framework/library",
            description="This is anonymous",
            withAsterisk=True,
            mb=10,
            children=dmc.Group(
                [
                    dmc.Checkbox(label="React", value="react"),
                    dmc.Checkbox(label="Vue", value="vue"),
                    dmc.Checkbox(label="Svelte", value="svelte"),
                    dmc.Checkbox(label="Angular", value="angular"),
                ],
                mt=10,
            ),
            value=["react", "vue"],
        ),
dmc.Text('ColorInput',style = text_style),
dmc.ColorInput(id="color-input", label="Your favorite color", w=250),
dmc.Text('ColorPicker',style = text_style),
dmc.ColorPicker(id="color-picker", format="rgba", value="rgba(41, 96, 214, 1)"),
dmc.Text('JsonInput',style = text_style),
dmc.JsonInput(
    label="Your package.json",
    placeholder="Textarea will autosize to fit the content",
    validationError="Invalid JSON",
    formatOnBlur=True,
    autosize=True,
    minRows=4,
),
dmc.Text('NumberInput',style = text_style),
dmc.NumberInput(
    label="Step on hold",
    description="Step the value when clicking and holding the arrows",
    stepHoldDelay=500,
    stepHoldInterval=100,
    value=0,
    w=250,
),
dmc.Text('PasswordInput',style = text_style),
dmc.PasswordInput(
    label="Your password:",
    w=250,
    placeholder="Your password",
    leftSection=DashIconify(icon="bi:shield-lock"),
    error=True,
    required = True,
    description = 'Password must include at least one letter, number and special character'
),
dmc.Text('PinInput',style = text_style),
dmc.Group(dmc.PinInput(length=8), justify="center"),

dmc.Text('RadioGroup',style = text_style),
dmc.RadioGroup(
            children=dmc.Group([dmc.Radio(l, value=k) for k, l in [["react", "React"], ["ng", "Angular"], ["svelte", "Svelte"], ["vue", "Vue"]]], my=10),
            id="radiogroup-simple",
            value="react",
            label="Select your favorite framework/library",
            size="sm",
            mb=10,
        ),
dmc.Text('Rating',style = text_style),
dmc.Stack(
    [
        dmc.Group([ dmc.Rating(fractions=2, value=1)]),
        dmc.Group([dmc.Rating(fractions=3, value=2.3333)]),
        dmc.Group([dmc.Rating(fractions=4, value=3.75)]),
    ]
),
dmc.Rating(
    value=1,
    emptySymbol=DashIconify(icon="tabler:sun"),
    fullSymbol=DashIconify(icon="tabler:moon"),
),
dmc.Text('SegmentedControl',style = text_style),

dmc.Stack(
    [dmc.SegmentedControl(data=["Dash", "Mantine", "Bootstrap", "Core"], radius=x) for x in [0, "md", "lg", 20]],
    align="flex-start",
),
dmc.Text('Slider',style = text_style),
 dmc.Slider(
            id="drag-slider",
            value=26,
            updatemode="drag",
            marks=[
                {"value": 20, "label": "20%"},
                {"value": 50, "label": "50%"},
                {"value": 80, "label": "80%"},
            ],
        ),
dmc.Text('Switch',style = text_style),

dmc.Switch(
    size="lg",
    radius="sm",
    label="Enable this option",
    checked=True
),
dmc.Text('TextInput',style = text_style),

dmc.Stack(
    children=[
        dmc.TextInput(label="Your Email:", w=200),
        dmc.TextInput(label="Your Email:", w=200, error="Enter a valid email"),
    ],
),
dmc.Text('Textarea',style = text_style),
dmc.Stack(
    children=[
        dmc.Textarea(
            label="Autosize with no rows limit",
            placeholder="Autosize with no rows limit",
            w=500,
            autosize=True,
            minRows=2,
        ),
        dmc.Textarea(
            label="Autosize with 4 rows max",
            placeholder="Autosize with 4 rows max",
            w=500,
            autosize=True,
            minRows=2,
            maxRows=4,
        ),
    ],
),

dmc.Text('TimeInput',style = text_style),
dmc.Group(
    gap=50,
    children=[
        dmc.TimeInput(label="What time is it now?"),
        dmc.TimeInput(
            label="What time is it now?",
            withSeconds=True,
            value='06/03/2024',
        ),
    ],
),
dmc.Text('DateInput',style = text_style),
dmc.DateInput(
            id="dateinput2",
            label="Enter a date",
            description="You can type a date or select from the calendar",
            w=300,
        ),
dmc.Text('DatePicker',style = text_style),
 dmc.DatePicker(
            id="date-picker-input",
            label="Start Date",
            description="You can also provide a description",
            minDate='05/03/2024',
            value='06/03/2024',  # or string in the format "YYYY-MM-DD"
            w=250,
        ),
dmc.Text('MultiSelect',style = text_style),

dmc.MultiSelect(
            label="Select frameworks",
            placeholder="Select all you like!",
            id="framework-multi-select",
            value=["ng", "vue"],
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            w=400,
            mb=10,
        ),

dmc.Text('Select',style = text_style),
  dmc.Select(
            label="Select framework",
            placeholder="Select one",
            id="framework-select",
            value="ng",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            w=200,
            mb=10,
        ),
dmc.Text('TagsInput',style = text_style),
dmc.TagsInput(
            label="Select frameworks",
            placeholder="Select all you like!",
            id="framework-tags-input",
            value=["ng", "vue"],
            w=400,
            mb=10,
        ),




   
]