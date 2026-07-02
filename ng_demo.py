"""
Northrop Grumman Design System — Component Showcase
=====================================================
Run:  python ng_demo.py
Req:  pip install flet

Displays all design system atoms and molecules across
light and dark mode with a live theme toggle.
"""

import flet as ft
from ng_theme import light_theme, dark_theme, get_flet_light_theme, get_flet_dark_theme
from ng_tokens import NGSpacingTokens as S, NGRadiusTokens as R
from ng_components import (
    ng_button,
    ng_text_field,
    ng_chip,
    ng_alert_banner,
    ng_badge,
    ng_status_pill,
    ng_divider,
    ng_label_text,
    ng_section_header,
    ng_card,
    ng_kpi_card,
    ng_nav_item,
    ng_input_field,
    ng_node_status_card,
)


# ─── Sidebar ──────────────────────────────────────────────────────────────────
def build_sidebar(t, active_section: str, on_nav) -> ft.Container:
    """Build the fixed dark-navy sidebar using ng_nav_item."""

    logo = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    width=28, height=28,
                    bgcolor=t.sidebar_accent,
                    border_radius=ft.border_radius.only(
                        top_left=R.sm, top_right=R.sm,
                        bottom_left=R.sm, bottom_right=R.xl,
                    ),
                ),
                ft.Column(
                    [
                        ft.Text("NG Design System", size=13, weight=ft.FontWeight.W_700,
                                color=ft.colors.WHITE, letter_spacing=0.5),
                        ft.Text("Component Showcase", size=9, color=t.sidebar_accent,
                                letter_spacing=1.0, weight=ft.FontWeight.W_500),
                    ],
                    spacing=0, tight=True,
                ),
            ],
            spacing=S.s3,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(vertical=S.s5, horizontal=S.s4),
        border=ft.border.only(bottom=ft.BorderSide(1, "rgba(255,255,255,0.08)")),
    )

    def nav(label, icon, section):
        return ng_nav_item(
            t, label, icon=icon,
            active=(active_section == section),
            on_click=lambda e, s=section: on_nav(s),
        )

    nav_content = ft.Column(
        [
            ft.Container(
                ft.Text("ATOMS", size=9, color="rgba(255,255,255,0.3)",
                        weight=ft.FontWeight.W_700, letter_spacing=1.5),
                padding=ft.padding.only(left=S.s4, top=S.s4, bottom=S.s2),
            ),
            nav("Buttons",    ft.icons.SMART_BUTTON_OUTLINED,    "buttons"),
            nav("Typography", ft.icons.TEXT_FIELDS_OUTLINED,     "typography"),
            nav("Text Fields",ft.icons.INPUT_OUTLINED,           "fields"),
            nav("Chips",      ft.icons.LABEL_OUTLINE,            "chips"),
            nav("Alerts",     ft.icons.NOTIFICATIONS_NONE,       "alerts"),
            nav("Badges",     ft.icons.NUMBERS_OUTLINED,         "badges"),
            nav("Status",     ft.icons.CIRCLE_OUTLINED,          "status"),
            nav("Dividers",   ft.icons.HORIZONTAL_RULE,          "dividers"),

            ft.Container(
                ft.Text("MOLECULES", size=9, color="rgba(255,255,255,0.3)",
                        weight=ft.FontWeight.W_700, letter_spacing=1.5),
                padding=ft.padding.only(left=S.s4, top=S.s6, bottom=S.s2),
            ),
            nav("Cards",      ft.icons.CROP_SQUARE_OUTLINED,     "cards"),
            nav("KPI Cards",  ft.icons.SPEED_OUTLINED,           "kpi"),
            nav("Node Cards", ft.icons.ROUTER_OUTLINED,          "nodes"),
            ng_nav_item(t, "Alerts Feed", icon=ft.icons.WARNING_AMBER_OUTLINED,
                        active=(active_section == "feed"), badge_count=7,
                        on_click=lambda e: on_nav("feed")),

            ft.Container(
                ft.Text("TOKENS", size=9, color="rgba(255,255,255,0.3)",
                        weight=ft.FontWeight.W_700, letter_spacing=1.5),
                padding=ft.padding.only(left=S.s4, top=S.s6, bottom=S.s2),
            ),
            nav("Colors",     ft.icons.PALETTE_OUTLINED,         "colors"),
            nav("Spacing",    ft.icons.SPACE_BAR_OUTLINED,       "spacing"),
        ],
        spacing=0,
    )

    footer = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Text("JD", size=12, weight=ft.FontWeight.W_700,
                                    color=ft.colors.WHITE),
                    width=32, height=32,
                    bgcolor=t.primary,
                    border_radius=ft.border_radius.all(R.full),
                    alignment=ft.alignment.center,
                ),
                ft.Column(
                    [
                        ft.Text("J. Davis", size=12, weight=ft.FontWeight.W_500,
                                color=ft.colors.WHITE),
                        ft.Text("System Designer", size=10,
                                color="rgba(255,255,255,0.45)"),
                    ],
                    spacing=0, tight=True,
                ),
            ],
            spacing=S.s3,
        ),
        padding=ft.padding.all(S.s4),
        border=ft.border.only(top=ft.BorderSide(1, "rgba(255,255,255,0.08)")),
    )

    return ft.Container(
        content=ft.Column(
            [logo, ft.Container(content=nav_content, expand=True), footer],
            spacing=0,
            expand=True,
        ),
        bgcolor=t.sidebar_bg,
        width=232,
        expand=True,
    )


# ─── Section renderers ────────────────────────────────────────────────────────

def section_buttons(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "Buttons", badge_text="ATOM",
                              subtitle="Five variants · Three sizes"),
            ng_divider(t, label="Filled"),
            ft.Row([
                ng_button(t, "Primary",   variant="filled",    size="lg"),
                ng_button(t, "Action",    variant="filled",    size="md"),
                ng_button(t, "Small",     variant="filled",    size="sm"),
                ng_button(t, "Secondary", variant="secondary", size="md"),
            ], spacing=S.s3, wrap=True),

            ng_divider(t, label="Outlined & Tonal"),
            ft.Row([
                ng_button(t, "Outlined", variant="outlined", size="md"),
                ng_button(t, "Tonal",    variant="tonal",    size="md"),
                ng_button(t, "Text",     variant="text",     size="md"),
            ], spacing=S.s3, wrap=True),

            ng_divider(t, label="With Icon"),
            ft.Row([
                ng_button(t, "Deploy",   variant="filled",   size="md",
                          icon=ft.icons.ROCKET_LAUNCH_OUTLINED),
                ng_button(t, "Export",   variant="outlined", size="md",
                          icon=ft.icons.DOWNLOAD_OUTLINED),
                ng_button(t, "Disabled", variant="filled",   size="md",
                          disabled=True),
            ], spacing=S.s3, wrap=True),
        ],
        spacing=S.s5,
    )


def section_typography(t) -> ft.Column:
    specs = [
        ("Display LG",   57, ft.FontWeight.W_400, "Define Possible"),
        ("Display MD",   36, ft.FontWeight.W_400, "Mission Systems"),
        ("Headline LG",  32, ft.FontWeight.W_400, "Aerospace & Defense"),
        ("Headline MD",  28, ft.FontWeight.W_400, "Space Division"),
        ("Headline SM",  24, ft.FontWeight.W_400, "Advanced Weapons"),
        ("Title LG",     22, ft.FontWeight.W_500, "Network Operations"),
        ("Title MD",     16, ft.FontWeight.W_500, "System Interface Label"),
        ("Title SM",     14, ft.FontWeight.W_500, "Card Header"),
        ("Body LG",      16, ft.FontWeight.W_400,
         "Northrop Grumman delivers a full spectrum of capabilities."),
        ("Body MD",      14, ft.FontWeight.W_400,
         "Supporting paragraph text for interface content and documentation."),
        ("Body SM",      12, ft.FontWeight.W_400,
         "Caption text, helper messages, supplemental details."),
        ("Label LG",     14, ft.FontWeight.W_500, "Button Text · Form Label"),
        ("Label MD",     12, ft.FontWeight.W_500, "CHIP · TAG · STATUS"),
        ("Label SM",     11, ft.FontWeight.W_500, "OVERLINE · MICRO LABEL"),
    ]
    rows = []
    for role, size, weight, preview in specs:
        rows.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            ft.Text(role, size=11, color=t.text_secondary,
                                    weight=ft.FontWeight.W_500, font_family="Roboto Mono"),
                            width=120,
                        ),
                        ft.Container(
                            ft.Text(f"{size}px", size=10, color=t.primary,
                                    font_family="Roboto Mono"),
                            width=48,
                        ),
                        ft.Text(preview, size=size, weight=weight, color=t.text_primary,
                                overflow=ft.TextOverflow.ELLIPSIS, expand=True),
                    ],
                    spacing=S.s4,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                border=ft.border.only(bottom=ft.BorderSide(0.5, t.outline_variant)),
                padding=ft.padding.symmetric(vertical=S.s3),
            )
        )
    return ft.Column(
        [ng_section_header(t, "Typography", badge_text="ATOM",
                           subtitle="Material Design 3 type scale · Roboto"),
         *rows],
        spacing=0,
    )


def section_fields(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "Text Fields", badge_text="ATOM",
                              subtitle="Input atoms with label, helper, error states"),
            ft.ResponsiveRow(
                [
                    ft.Column([ng_text_field(t, "Unit Identifier",
                                             hint_text="e.g. NGC-ALPHA-7")],
                              col={"sm": 12, "md": 6}),
                    ft.Column([ng_text_field(t, "Access Code",
                                             hint_text="Enter access code",
                                             password=True)],
                              col={"sm": 12, "md": 6}),
                    ft.Column([ng_text_field(t, "Segment", helper_text="IP range or CIDR block",
                                             hint_text="10.0.0.0/24")],
                              col={"sm": 12, "md": 6}),
                    ft.Column([ng_text_field(t, "Validation Error",
                                             value="Invalid entry",
                                             error_text="This field contains an error.",
                                             prefix_icon=ft.icons.ERROR_OUTLINE)],
                              col={"sm": 12, "md": 6}),
                    ft.Column([ng_text_field(t, "Notes", multiline=True,
                                             hint_text="Describe the issue…")],
                              col=12),
                ],
                spacing=S.s4,
            ),
        ],
        spacing=S.s5,
    )


def section_chips(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "Chips & Tags", badge_text="ATOM"),
            ng_divider(t, label="Variants"),
            ft.Row([
                ng_chip(t, "Filled",   variant="filled"),
                ng_chip(t, "Outlined", variant="outlined"),
                ng_chip(t, "Tonal",    variant="tonal"),
            ], spacing=S.s2, wrap=True),

            ng_divider(t, label="Semantic"),
            ft.Row([
                ng_chip(t, "Info",    severity="info",    leading_icon=ft.icons.INFO_OUTLINE),
                ng_chip(t, "Success", severity="success", leading_icon=ft.icons.CHECK_CIRCLE_OUTLINE),
                ng_chip(t, "Warning", severity="warning", leading_icon=ft.icons.WARNING_AMBER),
                ng_chip(t, "Error",   severity="error",   leading_icon=ft.icons.ERROR_OUTLINE),
            ], spacing=S.s2, wrap=True),

            ng_divider(t, label="With Icon"),
            ft.Row([
                ng_chip(t, "Router",   variant="tonal",    leading_icon=ft.icons.ROUTER),
                ng_chip(t, "Firewall", variant="outlined", leading_icon=ft.icons.SHIELD_OUTLINED),
                ng_chip(t, "Server",   variant="filled",   leading_icon=ft.icons.DNS_OUTLINED),
                ng_chip(t, "Offline",  variant="outlined", leading_icon=ft.icons.SIGNAL_WIFI_OFF),
            ], spacing=S.s2, wrap=True),
        ],
        spacing=S.s5,
    )


def section_alerts(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "Alert Banners", badge_text="ATOM",
                              subtitle="Four severity levels"),
            ng_alert_banner(t, "System check complete. All 248 nodes online.",
                            severity="info",    title="Info"),
            ng_alert_banner(t, "Mission data uploaded and verified successfully.",
                            severity="success", title="Success"),
            ng_alert_banner(t, "Communication delay detected on WAN link GE0/1.",
                            severity="warning", title="Warning"),
            ng_alert_banner(t, "Authentication failed. Contact security operations.",
                            severity="error",   title="Error"),
            ng_divider(t, label="Dismissible"),
            ng_alert_banner(t, "BGP session flap detected on RTR-CORE-01.",
                            severity="warning", title="Warning", dismissible=True),
        ],
        spacing=S.s4,
    )


def section_badges(t) -> ft.Column:
    demo_row = ft.Row(
        [
            ft.Stack(
                [
                    ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED, size=28, color=t.text_secondary),
                    ft.Container(ng_badge(t, 4,  color="primary"),
                                 right=0, top=0),
                ],
                width=36, height=36,
            ),
            ft.Stack(
                [
                    ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, size=28, color=t.text_secondary),
                    ft.Container(ng_badge(t, 12, color="error"),
                                 right=0, top=0),
                ],
                width=36, height=36,
            ),
            ft.Stack(
                [
                    ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, size=28, color=t.text_secondary),
                    ft.Container(ng_badge(t, "✓", color="success"),
                                 right=0, top=0),
                ],
                width=36, height=36,
            ),
        ],
        spacing=S.s6,
    )

    standalone_row = ft.Row(
        [
            ng_badge(t, 1,  color="primary"),
            ng_badge(t, 7,  color="error"),
            ng_badge(t, 42, color="warning"),
            ng_badge(t, "✓", color="success"),
            ng_badge(t, "NEW", color="primary"),
        ],
        spacing=S.s3,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.Column(
        [
            ng_section_header(t, "Badges", badge_text="ATOM",
                              subtitle="Notification counts · Stacked on icons"),
            ng_divider(t, label="Stacked on icons"),
            demo_row,
            ng_divider(t, label="Standalone"),
            standalone_row,
        ],
        spacing=S.s5,
    )


def section_status(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "Status Pills", badge_text="ATOM"),
            ft.Row([
                ng_status_pill(t, "Online",   status="online"),
                ng_status_pill(t, "Warning",  status="warning"),
                ng_status_pill(t, "Offline",  status="offline"),
                ng_status_pill(t, "Critical", status="critical"),
            ], spacing=S.s3, wrap=True),
        ],
        spacing=S.s5,
    )


def section_dividers(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "Dividers", badge_text="ATOM"),
            ng_divider(t),
            ng_divider(t, label="Section Label"),
            ng_divider(t, label="Infrastructure", thickness=2.0),
        ],
        spacing=S.s6,
    )


def section_cards(t) -> ft.Column:
    basic = ng_card(
        t,
        header=ft.Column([
            ft.Text("Card Header", size=14, weight=ft.FontWeight.W_700,
                    color=t.text_primary),
            ft.Text("Subtitle / secondary text", size=12, color=t.text_secondary),
        ], spacing=2, tight=True),
        body=ft.Text(
            "Cards are surface containers that group related content. "
            "They support optional headers, bodies, and footers. "
            "Elevation and corner radius come from design system tokens.",
            size=13, color=t.text_primary,
        ),
        footer=ft.Row(
            [ng_button(t, "Cancel", variant="text",     size="sm"),
             ng_button(t, "Confirm", variant="filled",  size="sm")],
            spacing=S.s2, alignment=ft.MainAxisAlignment.END,
        ),
    )

    elevated = ng_card(
        t,
        body=ft.Column([
            ft.Row([
                ft.Icon(ft.icons.ROUTER_OUTLINED, color=t.primary, size=20),
                ft.Text("Elevated Card (Level 3)", size=14, weight=ft.FontWeight.W_600,
                        color=t.text_primary),
            ], spacing=S.s2),
            ft.Text("Higher elevation indicates greater prominence in the hierarchy.",
                    size=12, color=t.text_secondary),
        ], spacing=S.s2, tight=True),
        elevation=4,
    )

    return ft.Column(
        [
            ng_section_header(t, "Cards", badge_text="MOLECULE",
                              subtitle="Surface containers · Elevation 0–5"),
            basic,
            elevated,
        ],
        spacing=S.s5,
    )


def section_kpi(t) -> ft.Column:
    return ft.Column(
        [
            ng_section_header(t, "KPI Cards", badge_text="MOLECULE",
                              subtitle="Metric display with accent bar and delta"),
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [ng_kpi_card(t, "Total Nodes",  "248",   unit="/ 251",
                                     delta="3 added", delta_positive=True,
                                     subtitle="this week",
                                     icon=ft.icons.DNS_OUTLINED,  accent="primary")],
                        col={"sm": 12, "md": 6, "lg": 3},
                    ),
                    ft.Column(
                        [ng_kpi_card(t, "Avg. Uptime",  "99.7",  unit="%",
                                     delta="0.2%", delta_positive=True,
                                     subtitle="vs 30-day avg",
                                     icon=ft.icons.SPEED_OUTLINED, accent="success")],
                        col={"sm": 12, "md": 6, "lg": 3},
                    ),
                    ft.Column(
                        [ng_kpi_card(t, "Throughput",   "42.3",  unit="Gbps",
                                     delta="4.1 Gbps", delta_positive=True,
                                     subtitle="vs 1h ago",
                                     icon=ft.icons.SEND_OUTLINED,  accent="secondary")],
                        col={"sm": 12, "md": 6, "lg": 3},
                    ),
                    ft.Column(
                        [ng_kpi_card(t, "Active Alerts", "7",    unit="",
                                     delta="3 critical", delta_positive=False,
                                     subtitle="4 high · 0 med",
                                     icon=ft.icons.WARNING_AMBER_OUTLINED, accent="warning")],
                        col={"sm": 12, "md": 6, "lg": 3},
                    ),
                ],
                spacing=S.s4,
            ),
        ],
        spacing=S.s5,
    )


def section_nodes(t) -> ft.Column:
    nodes = [
        ("RTR-CORE-01", "10.0.0.1",  "Router",   "online",   "12%", "34%",  "99.9%"),
        ("SW-DIST-04",  "10.0.1.4",  "Switch",   "online",   "8%",  "21%",  "100%"),
        ("FW-PERIM-02", "10.0.2.2",  "Firewall", "critical", "97%", "88%",  "98.7%"),
        ("SW-ACC-11",   "10.0.1.11", "Switch",   "warning",  "78%", "61%",  "99.1%"),
        ("DNS-PRI-01",  "10.0.0.53", "DNS",      "online",   "5%",  "18%",  "100%"),
        ("LB-FRONT-01", "10.0.3.1",  "LB",       "online",   "29%", "44%",  "100%"),
        ("SRV-APP-07",  "10.1.0.7",  "Server",   "warning",  "61%", "72%",  "99.4%"),
        ("SRV-BAK-03",  "10.1.2.3",  "Server",   "offline",  "—",   "—",    "—"),
    ]
    grid = ft.ResponsiveRow(
        [
            ft.Column(
                [ng_node_status_card(
                    t, name, ip, ntype, status,
                    cpu=cpu, memory=mem, uptime=up,
                )],
                col={"sm": 12, "md": 6, "lg": 4, "xl": 3},
            )
            for name, ip, ntype, status, cpu, mem, up in nodes
        ],
        spacing=S.s3,
    )
    return ft.Column(
        [ng_section_header(t, "Node Status Cards", badge_text="MOLECULE",
                           subtitle="Network node cards with status, metrics"),
         grid],
        spacing=S.s5,
    )


def section_alert_feed(t) -> ft.Column:
    feed_items = [
        ("crit", "CPU threshold exceeded — 97%",
         "FW-PERIM-02 · 10.0.2.2", "2m ago"),
        ("crit", "Interface GE0/1 — packet loss 18%",
         "RTR-WAN-05 · 10.0.5.1",  "5m ago"),
        ("high", "Memory utilization high — 78%",
         "SW-ACC-11 · 10.0.1.11",  "9m ago"),
        ("high", "BGP session flap detected · AS 65001",
         "RTR-CORE-01 · 10.0.0.1", "14m ago"),
        ("med",  "NTP sync failure — drift > 500ms",
         "SRV-APP-07 · 10.1.0.7",  "21m ago"),
        ("med",  "SRV-BAK-03 unreachable (ping)",
         "SRV-BAK-03 · 10.1.2.3",  "37m ago"),
        ("low",  "SSL certificate expiry in 14 days",
         "LB-FRONT-01 · 10.0.3.1", "1h ago"),
    ]

    _sev_color = {
        "crit": t.error,
        "high": t.warning,
        "med":  t.info,
        "low":  t.text_disabled,
    }
    _sev_label = {"crit": "CRITICAL", "high": "HIGH", "med": "MEDIUM", "low": "LOW"}

    rows = []
    for sev, title, meta, ts in feed_items:
        color = _sev_color[sev]
        rows.append(
            ft.Container(
                content=ft.Row(
                    [
                        # Severity bar
                        ft.Container(bgcolor=color, width=4, border_radius=ft.border_radius.all(2)),
                        # Content
                        ft.Column(
                            [
                                ft.Text(title, size=13, weight=ft.FontWeight.W_500,
                                        color=t.text_primary),
                                ft.Text(f"{meta}  ·  {ts}", size=11, color=t.text_secondary,
                                        font_family="Roboto Mono"),
                            ],
                            spacing=2, tight=True, expand=True,
                        ),
                        # Badge
                        ft.Container(
                            content=ft.Text(_sev_label[sev], size=9, weight=ft.FontWeight.W_700,
                                            color=color),
                            bgcolor=t.semantic_bg(
                                {"crit": "error", "high": "warning",
                                 "med":  "info",  "low":  "info"}[sev]
                            ),
                            border_radius=ft.border_radius.all(R.sm),
                            padding=ft.padding.symmetric(vertical=2, horizontal=6),
                        ),
                    ],
                    spacing=S.s3,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                border=ft.border.only(bottom=ft.BorderSide(0.5, t.outline_variant)),
                padding=ft.padding.symmetric(vertical=S.s3, horizontal=S.s4),
                bgcolor=(t.primary_subtle if sev == "crit" else "transparent"),
            )
        )

    return ft.Column(
        [
            ng_section_header(t, "Alert Feed", badge_text="MOLECULE",
                              subtitle="Severity-ranked live alert list"),
            ft.Container(
                content=ft.Column(rows, spacing=0),
                border=ft.border.all(1, t.outline),
                border_radius=ft.border_radius.all(R.lg),
                bgcolor=t.surface,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            ),
        ],
        spacing=S.s5,
    )


def section_colors(t) -> ft.Column:
    """Color token swatch grid."""
    def scale_row(name, shades):
        swatches = []
        for step, hex_val in shades:
            swatches.append(
                ft.Column(
                    [
                        ft.Container(height=52, bgcolor=hex_val,
                                     border_radius=ft.border_radius.all(R.sm),
                                     expand=True),
                        ft.Text(str(step), size=9, color=t.text_secondary,
                                font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                        ft.Text(hex_val, size=8, color=t.text_disabled,
                                font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                    ],
                    spacing=2, tight=True, expand=True,
                )
            )
        return ft.Column(
            [
                ft.Text(name, size=11, weight=ft.FontWeight.W_600, color=t.text_secondary),
                ft.Row(swatches, spacing=S.s2, expand=True),
            ],
            spacing=S.s2,
        )

    from ng_tokens import NGColorTokens as C
    blue_scale = [
        (50,  C.blue_50),  (100, C.blue_100), (200, C.blue_200),
        (300, C.blue_300), (400, C.blue_400), (500, C.blue_500),
        (600, C.blue_600), (700, C.blue_700), (800, C.blue_800), (900, C.blue_900),
    ]
    navy_scale = [
        (50,  C.navy_50),  (100, C.navy_100), (200, C.navy_200),
        (300, C.navy_300), (400, C.navy_400), (500, C.navy_500),
        (600, C.navy_600), (700, C.navy_700), (800, C.navy_800), (900, C.navy_900),
    ]
    gray_scale = [
        (50, C.gray_50), (100, C.gray_100), (200, C.gray_200),
        (300, C.gray_300), (400, C.gray_400), (500, C.gray_500),
        (600, C.gray_600), (700, C.gray_700), (800, C.gray_800), (900, C.gray_900),
    ]

    return ft.Column(
        [
            ng_section_header(t, "Color Tokens", badge_text="TOKENS",
                              subtitle="Raw palette scales · Honolulu Blue PMS 2196 C · Navy PMS 2736 C"),
            scale_row("NG Blue — Primary",   blue_scale),
            scale_row("NG Navy — Secondary", navy_scale),
            scale_row("Neutral Gray",        gray_scale),
        ],
        spacing=S.s6,
    )


def section_spacing(t) -> ft.Column:
    """Spacing token visual grid."""
    items = [
        ("--s1",  S.s1,  "4px",  "Icon gap, tight nudge"),
        ("--s2",  S.s2,  "8px",  "Inline item gap, chip padding"),
        ("--s3",  S.s3,  "12px", "Button V-pad, list gap"),
        ("--s4",  S.s4,  "16px", "Card padding, form gap"),
        ("--s5",  S.s5,  "20px", "Component internal spacing"),
        ("--s6",  S.s6,  "24px", "Section gap"),
        ("--s8",  S.s8,  "32px", "Page padding, modal padding"),
        ("--s10", S.s10, "40px", "Section between-group spacing"),
        ("--s12", S.s12, "48px", "Major section breaks"),
        ("--s16", S.s16, "64px", "Hero padding"),
    ]
    max_w = 420

    rows = []
    for token, px, label, usage in items:
        rows.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            ft.Text(token, size=11, color=t.primary,
                                    font_family="Roboto Mono"),
                            width=72,
                        ),
                        ft.Container(
                            ft.Text(label, size=10, color=t.text_secondary,
                                    font_family="Roboto Mono"),
                            width=40,
                        ),
                        ft.Container(
                            ft.Container(
                                bgcolor=t.primary,
                                height=18,
                                border_radius=ft.border_radius.all(R.xs),
                                opacity=0.7,
                                width=px / S.s16 * max_w,
                            ),
                            expand=True,
                        ),
                        ft.Container(
                            ft.Text(usage, size=10, color=t.text_secondary),
                            width=220,
                            alignment=ft.alignment.center_right,
                        ),
                    ],
                    spacing=S.s4,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                border=ft.border.only(bottom=ft.BorderSide(0.5, t.outline_variant)),
                padding=ft.padding.symmetric(vertical=S.s2),
            )
        )

    return ft.Column(
        [
            ng_section_header(t, "Spacing Tokens", badge_text="TOKENS",
                              subtitle="4px base grid · 14 steps"),
            *rows,
        ],
        spacing=0,
    )


# ─── Section dispatch ─────────────────────────────────────────────────────────
SECTIONS = {
    "buttons":    section_buttons,
    "typography": section_typography,
    "fields":     section_fields,
    "chips":      section_chips,
    "alerts":     section_alerts,
    "badges":     section_badges,
    "status":     section_status,
    "dividers":   section_dividers,
    "cards":      section_cards,
    "kpi":        section_kpi,
    "nodes":      section_nodes,
    "feed":       section_alert_feed,
    "colors":     section_colors,
    "spacing":    section_spacing,
}


# ─── Main app ────────────────────────────────────────────────────────────────
def main(page: ft.Page):
    page.title = "NG Design System — Component Showcase"
    page.fonts = {
        "Roboto":      "https://fonts.gstatic.com/s/roboto/v32/KFOmCnqEu92Fr1Mu4mxKKTU1Kg.woff2",
        "Roboto Mono": "https://fonts.gstatic.com/s/robotomono/v23/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_3vq_RME.woff2",
    }
    page.theme      = get_flet_light_theme()
    page.dark_theme = get_flet_dark_theme()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding    = 0

    # State
    active_section  = "buttons"
    _current_theme  = light_theme

    # Content area ref
    content_ref     = ft.Ref[ft.Column]()
    sidebar_ref     = ft.Ref[ft.Container]()

    def get_theme() -> object:
        return light_theme if page.theme_mode == ft.ThemeMode.LIGHT else dark_theme

    def rebuild_content():
        t  = get_theme()
        fn = SECTIONS.get(active_section, section_buttons)
        content_ref.current.controls = [fn(t)]
        page.update()

    def rebuild_sidebar():
        t = get_theme()
        sidebar_ref.current.content = build_sidebar(
            t, active_section, on_nav_click
        ).content
        sidebar_ref.current.bgcolor = t.sidebar_bg

    def on_nav_click(section: str):
        nonlocal active_section
        active_section = section
        rebuild_sidebar()
        rebuild_content()

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        t = get_theme()
        topbar_container.bgcolor = t.surface
        topbar_container.border  = ft.border.only(
            bottom=ft.BorderSide(1, t.outline_variant))
        content_container.bgcolor = t.bg
        theme_btn.text = "Light Mode" if t.is_dark() else "Dark Mode"
        theme_btn.icon = (
            ft.icons.LIGHT_MODE_OUTLINED if t.is_dark()
            else ft.icons.DARK_MODE_OUTLINED
        )
        rebuild_sidebar()
        rebuild_content()

    t = get_theme()

    # ── Topbar ────────────────────────────────────────────────────────────────
    theme_btn = ft.ElevatedButton(
        text="Dark Mode",
        icon=ft.icons.DARK_MODE_OUTLINED,
        on_click=toggle_theme,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=R.full),
            bgcolor={ft.ControlState.DEFAULT: t.primary,
                     ft.ControlState.HOVERED: t.primary_hover},
            color=t.on_primary,
            elevation=1,
        ),
    )

    topbar_container = ft.Container(
        content=ft.Row(
            [
                ft.Text("NG Design System", size=14, weight=ft.FontWeight.W_500,
                        color=t.text_secondary),
                ft.Text("·", color=t.text_disabled),
                ft.Text("Component Showcase", size=14, weight=ft.FontWeight.W_700,
                        color=t.text_primary),
                ft.Container(expand=True),
                theme_btn,
            ],
            spacing=S.s3,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=t.surface,
        border=ft.border.only(bottom=ft.BorderSide(1, t.outline_variant)),
        padding=ft.padding.symmetric(vertical=S.s4, horizontal=S.s6),
        height=56,
    )

    # ── Content scroller ─────────────────────────────────────────────────────
    initial_fn = SECTIONS.get(active_section, section_buttons)

    content_column = ft.Column(
        ref=content_ref,
        controls=[initial_fn(t)],
        scroll=ft.ScrollMode.AUTO,
    )

    content_container = ft.Container(
        content=ft.Container(
            content=content_column,
            padding=ft.padding.all(S.s8),
        ),
        bgcolor=t.bg,
        expand=True,
    )

    # ── Sidebar container ─────────────────────────────────────────────────────
    sidebar_container = ft.Container(
        ref=sidebar_ref,
        content=build_sidebar(t, active_section, on_nav_click).content,
        bgcolor=t.sidebar_bg,
        width=232,
    )

    # ── Root layout ───────────────────────────────────────────────────────────
    page.add(
        ft.Column(
            [
                topbar_container,
                ft.Row(
                    [sidebar_container, content_container],
                    spacing=0,
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ],
            spacing=0,
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
