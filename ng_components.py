"""
Northrop Grumman Design System — Flet Component Library
=========================================================
v1.0 | Atomic Design — Atoms & Molecules

All factory functions accept an NGTheme instance as their first argument
so components are portable across light and dark mode without touching
global page state.

Atoms (single-purpose):
    ng_button          — Filled / Outlined / Tonal / Text / Secondary
    ng_text_field      — Standard text input with label, helper, error states
    ng_chip            — Filled / Outlined / Tonal / Semantic chips
    ng_alert_banner    — Info / Success / Warning / Error alert banners
    ng_badge           — Numeric notification badge
    ng_status_pill     — Online / Warning / Offline / Critical status indicators
    ng_divider         — Horizontal rule with optional label
    ng_label_text      — Overline / caption text
    ng_section_header  — Section title with optional badge

Molecules (composed from atoms):
    ng_card            — Surface container with optional header + body
    ng_kpi_card        — Metric card with label, value, delta, sparkline
    ng_nav_item        — Sidebar navigation row (active / hover / badge)
    ng_input_field     — Full form field: label + text_field + helper text
    ng_node_status_card — Network node card with status dot and metrics

Usage:
    from ng_theme import light_theme
    from ng_components import ng_button, ng_card, ng_alert_banner

    btn = ng_button(light_theme, "Deploy", variant="filled", on_click=handle_click)
"""

import flet as ft
from ng_theme import NGTheme
from ng_tokens import NGSpacingTokens as S, NGRadiusTokens as R, NGElevationTokens as E


# ═══════════════════════════════════════════════════════════════════════════════
# INTERNAL HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def _pad(v=None, h=None, t=None, b=None, l=None, r=None, all=None):
    """Convenience wrapper for ft.padding."""
    if all is not None:
        return ft.padding.all(all)
    return ft.padding.only(left=l or h or 0, right=r or h or 0,
                           top=t or v or 0, bottom=b or v or 0)


def _border_radius(value: int) -> ft.BorderRadius:
    return ft.border_radius.all(value)


def _border(color: str, width: float = 1.0) -> ft.Border:
    return ft.border.all(width, color)


# ═══════════════════════════════════════════════════════════════════════════════
# ATOMS
# ═══════════════════════════════════════════════════════════════════════════════

def ng_button(
    theme: NGTheme,
    text: str,
    *,
    variant: str = "filled",
    size: str = "md",
    on_click=None,
    icon: str | None = None,
    disabled: bool = False,
    width: int | None = None,
) -> ft.Control:
    """
    Button atom.

    variant: "filled" | "outlined" | "tonal" | "text" | "secondary"
    size:    "sm" | "md" | "lg"
    """
    _sizes = {
        "sm": (S.s1, S.s4, 12),   # (v_pad, h_pad, font_size)
        "md": (S.s3, S.s6, 14),
        "lg": (S.s4, S.s8, 16),
    }
    v_pad, h_pad, font_size = _sizes.get(size, _sizes["md"])

    base_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=R.full),
        padding=ft.padding.symmetric(vertical=v_pad, horizontal=h_pad),
        text_style=ft.TextStyle(size=font_size, weight=ft.FontWeight.W_500),
        animation_duration=200,
    )

    kwargs = dict(
        text=text,
        icon=icon,
        on_click=on_click,
        disabled=disabled,
        width=width,
    )

    if variant == "filled":
        return ft.FilledButton(
            **kwargs,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=R.full),
                bgcolor={
                    ft.ControlState.DEFAULT:  theme.primary,
                    ft.ControlState.HOVERED:  theme.primary_hover,
                    ft.ControlState.PRESSED:  theme.primary_active,
                    ft.ControlState.DISABLED: theme.outline,
                },
                color={
                    ft.ControlState.DEFAULT:  theme.on_primary,
                    ft.ControlState.DISABLED: theme.text_disabled,
                },
                elevation={"": 1, ft.ControlState.HOVERED: 3},
                padding=ft.padding.symmetric(vertical=v_pad, horizontal=h_pad),
                text_style=ft.TextStyle(size=font_size, weight=ft.FontWeight.W_500),
                animation_duration=200,
            ),
        )

    if variant == "secondary":
        return ft.FilledButton(
            **kwargs,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=R.full),
                bgcolor={
                    ft.ControlState.DEFAULT: theme.secondary,
                    ft.ControlState.HOVERED: theme.secondary_hover,
                    ft.ControlState.PRESSED: theme.secondary_active,
                },
                color=theme.on_secondary,
                elevation={"": 1, ft.ControlState.HOVERED: 3},
                padding=ft.padding.symmetric(vertical=v_pad, horizontal=h_pad),
                text_style=ft.TextStyle(size=font_size, weight=ft.FontWeight.W_500),
                animation_duration=200,
            ),
        )

    if variant == "outlined":
        return ft.OutlinedButton(
            **kwargs,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=R.full),
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(1.5, theme.primary),
                    ft.ControlState.HOVERED: ft.BorderSide(1.5, theme.primary_hover),
                },
                color={
                    ft.ControlState.DEFAULT: theme.primary,
                    ft.ControlState.HOVERED: theme.primary_hover,
                },
                bgcolor={
                    ft.ControlState.DEFAULT: "transparent",
                    ft.ControlState.HOVERED: theme.primary_subtle,
                },
                padding=ft.padding.symmetric(vertical=v_pad, horizontal=h_pad),
                text_style=ft.TextStyle(size=font_size, weight=ft.FontWeight.W_500),
                animation_duration=200,
            ),
        )

    if variant == "tonal":
        return ft.FilledTonalButton(
            **kwargs,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=R.full),
                bgcolor={
                    ft.ControlState.DEFAULT: theme.primary_container,
                    ft.ControlState.HOVERED: theme.primary_subtle,
                },
                color=theme.on_primary_container,
                padding=ft.padding.symmetric(vertical=v_pad, horizontal=h_pad),
                text_style=ft.TextStyle(size=font_size, weight=ft.FontWeight.W_500),
                animation_duration=200,
            ),
        )

    if variant == "text":
        return ft.TextButton(
            **kwargs,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=R.full),
                color={
                    ft.ControlState.DEFAULT: theme.primary,
                    ft.ControlState.HOVERED: theme.primary_hover,
                },
                bgcolor={
                    ft.ControlState.DEFAULT: "transparent",
                    ft.ControlState.HOVERED: theme.primary_subtle,
                },
                padding=ft.padding.symmetric(vertical=v_pad, horizontal=h_pad),
                text_style=ft.TextStyle(size=font_size, weight=ft.FontWeight.W_500),
                animation_duration=200,
            ),
        )

    raise ValueError(f"Unknown button variant: '{variant}'. "
                     "Use: filled | outlined | tonal | text | secondary")


def ng_text_field(
    theme: NGTheme,
    label: str = "",
    *,
    hint_text: str = "",
    helper_text: str = "",
    error_text: str = "",
    password: bool = False,
    multiline: bool = False,
    prefix_icon: str | None = None,
    suffix_icon: str | None = None,
    value: str = "",
    on_change=None,
    on_submit=None,
    width: int | None = None,
    expand: bool = False,
) -> ft.TextField:
    """Text field atom with full NG token styling."""
    return ft.TextField(
        label=label,
        hint_text=hint_text,
        helper_text=helper_text or None,
        error_text=error_text or None,
        password=password,
        multiline=multiline,
        prefix_icon=prefix_icon,
        suffix_icon=suffix_icon,
        value=value,
        on_change=on_change,
        on_submit=on_submit,
        width=width,
        expand=expand,
        border_color=theme.outline,
        focused_border_color=theme.primary,
        focused_color=theme.primary,
        error_style=ft.TextStyle(color=theme.error, size=12),
        helper_style=ft.TextStyle(color=theme.text_secondary, size=12),
        label_style=ft.TextStyle(color=theme.text_secondary, size=14),
        hint_style=ft.TextStyle(color=theme.text_disabled, size=14),
        text_style=ft.TextStyle(color=theme.text_primary, size=14),
        cursor_color=theme.primary,
        selection_color=theme.primary_subtle,
        border_radius=R.sm,
        border_width=1.5,
        focused_border_width=2,
        bgcolor=theme.surface,
    )


def ng_chip(
    theme: NGTheme,
    label: str,
    *,
    variant: str = "filled",
    severity: str | None = None,
    selected: bool = False,
    leading_icon: str | None = None,
    on_click=None,
    on_select=None,
) -> ft.Control:
    """
    Chip / tag atom.

    variant:  "filled" | "outlined" | "tonal"
    severity: "info" | "success" | "warning" | "error"
              (overrides variant with semantic colors)
    """
    if severity:
        fg = theme.semantic_color(severity)
        bg = theme.semantic_bg(severity)
        return ft.Container(
            content=ft.Row(
                [
                    *([] if not leading_icon else
                      [ft.Icon(leading_icon, size=14, color=fg)]),
                    ft.Text(label, size=12, weight=ft.FontWeight.W_500, color=fg),
                ],
                spacing=S.s1,
                tight=True,
            ),
            bgcolor=bg,
            border=_border(fg, 1),
            border_radius=_border_radius(R.full),
            padding=_pad(v=4, h=10),
            on_click=on_click,
        )

    if variant == "filled":
        return ft.Container(
            content=ft.Row(
                [
                    *([] if not leading_icon else
                      [ft.Icon(leading_icon, size=14, color=theme.on_primary)]),
                    ft.Text(label, size=12, weight=ft.FontWeight.W_500,
                            color=theme.on_primary),
                ],
                spacing=S.s1, tight=True,
            ),
            bgcolor=theme.primary,
            border_radius=_border_radius(R.full),
            padding=_pad(v=4, h=10),
            on_click=on_click,
        )

    if variant == "outlined":
        return ft.Container(
            content=ft.Row(
                [
                    *([] if not leading_icon else
                      [ft.Icon(leading_icon, size=14, color=theme.text_primary)]),
                    ft.Text(label, size=12, weight=ft.FontWeight.W_500,
                            color=theme.text_primary),
                ],
                spacing=S.s1, tight=True,
            ),
            bgcolor="transparent",
            border=_border(theme.outline, 1),
            border_radius=_border_radius(R.full),
            padding=_pad(v=4, h=10),
            on_click=on_click,
        )

    if variant == "tonal":
        return ft.Container(
            content=ft.Row(
                [
                    *([] if not leading_icon else
                      [ft.Icon(leading_icon, size=14,
                               color=theme.on_primary_container)]),
                    ft.Text(label, size=12, weight=ft.FontWeight.W_500,
                            color=theme.on_primary_container),
                ],
                spacing=S.s1, tight=True,
            ),
            bgcolor=theme.primary_container,
            border_radius=_border_radius(R.full),
            padding=_pad(v=4, h=10),
            on_click=on_click,
        )

    raise ValueError(f"Unknown chip variant: '{variant}'")


def ng_alert_banner(
    theme: NGTheme,
    message: str,
    *,
    title: str = "",
    severity: str = "info",
    dismissible: bool = False,
    on_dismiss=None,
) -> ft.Container:
    """
    Alert banner atom.
    severity: "info" | "success" | "warning" | "error"
    """
    _icons = {
        "info":    ft.icons.INFO_OUTLINE,
        "success": ft.icons.CHECK_CIRCLE_OUTLINE,
        "warning": ft.icons.WARNING_AMBER_OUTLINED,
        "error":   ft.icons.ERROR_OUTLINE,
    }
    fg = theme.semantic_color(severity)
    bg = theme.semantic_bg(severity)

    body_content = [
        ft.Icon(_icons.get(severity, ft.icons.INFO_OUTLINE), size=18, color=fg),
        ft.Column(
            [
                *([] if not title else
                  [ft.Text(title, size=13, weight=ft.FontWeight.W_600, color=fg)]),
                ft.Text(message, size=12, color=theme.text_primary),
            ],
            spacing=2,
            tight=True,
            expand=True,
        ),
    ]
    if dismissible:
        body_content.append(
            ft.IconButton(
                icon=ft.icons.CLOSE,
                icon_size=16,
                icon_color=fg,
                on_click=on_dismiss,
                style=ft.ButtonStyle(padding=ft.padding.all(0)),
            )
        )

    return ft.Container(
        content=ft.Row(body_content, spacing=S.s3, vertical_alignment=ft.CrossAxisAlignment.START),
        bgcolor=bg,
        border=ft.border.only(left=ft.BorderSide(4, fg)),
        border_radius=_border_radius(R.md),
        padding=_pad(v=S.s3, h=S.s4),
    )


def ng_badge(
    theme: NGTheme,
    count: int | str,
    *,
    color: str = "primary",
) -> ft.Container:
    """
    Numeric badge atom (notification dot).
    color: "primary" | "error" | "success" | "warning"
    """
    _bg = {
        "primary": theme.primary,
        "error":   theme.error,
        "success": theme.success,
        "warning": theme.warning,
    }.get(color, theme.primary)

    _fg = {
        "primary": theme.on_primary,
        "error":   theme.on_error,
        "success": theme.on_success,
        "warning": theme.on_warning,
    }.get(color, theme.on_primary)

    label = str(count)
    width = max(20, len(label) * 8 + 8)

    return ft.Container(
        content=ft.Text(label, size=10, weight=ft.FontWeight.W_700, color=_fg,
                        text_align=ft.TextAlign.CENTER),
        bgcolor=_bg,
        border_radius=_border_radius(R.full),
        width=width,
        height=20,
        alignment=ft.alignment.center,
    )


def ng_status_pill(
    theme: NGTheme,
    label: str,
    *,
    status: str = "online",
) -> ft.Container:
    """
    Status pill molecule.
    status: "online" | "warning" | "offline" | "critical"
    """
    _colors = {
        "online":   (theme.success, theme.success_subtle),
        "warning":  (theme.warning, theme.warning_subtle),
        "offline":  (theme.text_disabled, theme.surface_variant),
        "critical": (theme.error,   theme.error_subtle),
    }
    fg, bg = _colors.get(status, _colors["online"])

    return ft.Container(
        content=ft.Row(
            [
                ft.Container(width=6, height=6, bgcolor=fg,
                             border_radius=_border_radius(R.full)),
                ft.Text(label, size=11, weight=ft.FontWeight.W_500, color=fg),
            ],
            spacing=S.s1, tight=True,
        ),
        bgcolor=bg,
        border_radius=_border_radius(R.full),
        padding=_pad(v=3, h=S.s2),
    )


def ng_divider(
    theme: NGTheme,
    *,
    label: str = "",
    thickness: float = 1.0,
) -> ft.Control:
    """Horizontal divider with optional centered label."""
    if not label:
        return ft.Divider(thickness=thickness, color=theme.outline_variant)

    return ft.Row(
        [
            ft.Divider(thickness=thickness, color=theme.outline_variant, expand=True),
            ft.Text(label, size=11, color=theme.text_secondary,
                    weight=ft.FontWeight.W_500),
            ft.Divider(thickness=thickness, color=theme.outline_variant, expand=True),
        ],
        spacing=S.s3,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


def ng_label_text(
    theme: NGTheme,
    text: str,
    *,
    size: str = "md",
    uppercase: bool = False,
    color: str | None = None,
) -> ft.Text:
    """
    Label / caption text atom.
    size: "sm" | "md" | "lg"
    """
    _sizes = {"sm": 10, "md": 12, "lg": 14}
    return ft.Text(
        text.upper() if uppercase else text,
        size=_sizes.get(size, 12),
        weight=ft.FontWeight.W_500,
        color=color or theme.text_secondary,
    )


def ng_section_header(
    theme: NGTheme,
    title: str,
    *,
    badge_text: str = "",
    subtitle: str = "",
    action: ft.Control | None = None,
) -> ft.Column:
    """Section heading with optional badge, subtitle, and action control."""
    title_row_children = [
        ft.Text(title, size=18, weight=ft.FontWeight.W_700, color=theme.text_primary),
    ]
    if badge_text:
        title_row_children.append(
            ft.Container(
                content=ft.Text(badge_text, size=10, weight=ft.FontWeight.W_700,
                                color=theme.primary),
                bgcolor=theme.primary_subtle,
                border_radius=_border_radius(R.sm),
                padding=_pad(v=2, h=S.s2),
            )
        )
    if action:
        title_row_children.append(
            ft.Container(content=action, expand=True,
                         alignment=ft.alignment.center_right)
        )

    children = [
        ft.Row(title_row_children, spacing=S.s2,
               vertical_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Container(height=3, bgcolor=theme.primary,
                     border_radius=_border_radius(R.sm), width=48),
    ]
    if subtitle:
        children.append(
            ft.Text(subtitle, size=13, color=theme.text_secondary)
        )

    return ft.Column(children, spacing=S.s1, tight=True)


# ═══════════════════════════════════════════════════════════════════════════════
# MOLECULES
# ═══════════════════════════════════════════════════════════════════════════════

def ng_card(
    theme: NGTheme,
    *,
    header: ft.Control | None = None,
    body: ft.Control | None = None,
    footer: ft.Control | None = None,
    padding: int = S.s5,
    elevation: int = E.level_1,
    width: int | None = None,
    expand: bool = False,
) -> ft.Card:
    """
    Card molecule — surface container with optional header / body / footer.
    Supports elevation levels 0–5 from NGElevationTokens.
    """
    children = []
    if header:
        children.append(
            ft.Container(
                content=header,
                padding=_pad(h=S.s5, v=S.s4),
                border=ft.border.only(bottom=ft.BorderSide(1, theme.outline_variant)),
            )
        )
    if body:
        children.append(ft.Container(content=body, padding=ft.padding.all(padding)))
    if footer:
        children.append(
            ft.Container(
                content=footer,
                padding=_pad(h=S.s5, v=S.s4),
                border=ft.border.only(top=ft.BorderSide(1, theme.outline_variant)),
            )
        )

    return ft.Card(
        content=ft.Column(children, spacing=0, tight=True),
        color=theme.surface,
        elevation=elevation,
        shape=ft.RoundedRectangleBorder(radius=R.lg),
        width=width,
        expand=expand,
    )


def ng_kpi_card(
    theme: NGTheme,
    label: str,
    value: str,
    *,
    unit: str = "",
    delta: str = "",
    delta_positive: bool = True,
    subtitle: str = "",
    accent: str = "primary",
    icon: str | None = None,
    width: int | None = None,
) -> ft.Card:
    """
    KPI metric card molecule.

    accent: "primary" | "secondary" | "success" | "warning" | "error"
    """
    _accent_colors = {
        "primary":   theme.primary,
        "secondary": theme.secondary,
        "success":   theme.success,
        "warning":   theme.warning,
        "error":     theme.error,
    }
    _accent_bgs = {
        "primary":   theme.primary_subtle,
        "secondary": theme.secondary_subtle,
        "success":   theme.success_subtle,
        "warning":   theme.warning_subtle,
        "error":     theme.error_subtle,
    }
    accent_color = _accent_colors.get(accent, theme.primary)
    accent_bg    = _accent_bgs.get(accent, theme.primary_subtle)

    delta_color  = theme.success if delta_positive else theme.error
    delta_arrow  = "▲" if delta_positive else "▼"

    header_row = []
    header_row.append(
        ft.Column(
            [ft.Text(label.upper(), size=11, weight=ft.FontWeight.W_500,
                     color=theme.text_secondary, letter_spacing=0.8)],
            tight=True, expand=True,
        )
    )
    if icon:
        header_row.append(
            ft.Container(
                content=ft.Icon(icon, size=16, color=accent_color),
                bgcolor=accent_bg,
                border_radius=_border_radius(R.md),
                padding=ft.padding.all(S.s2),
            )
        )

    value_row = [
        ft.Text(value, size=28, weight=ft.FontWeight.W_700, color=theme.text_primary),
    ]
    if unit:
        value_row.append(
            ft.Text(unit, size=14, weight=ft.FontWeight.W_400, color=theme.text_secondary)
        )

    sub_row = []
    if delta:
        sub_row.append(
            ft.Text(f"{delta_arrow} {delta}", size=11, weight=ft.FontWeight.W_500,
                    color=delta_color)
        )
    if subtitle:
        sub_row.append(ft.Text(subtitle, size=11, color=theme.text_secondary))

    body = ft.Column(
        [
            ft.Row(header_row, spacing=S.s2,
                   vertical_alignment=ft.CrossAxisAlignment.START),
            ft.Row(value_row, spacing=S.s1,
                   vertical_alignment=ft.CrossAxisAlignment.BASELINE),
            *([] if not sub_row else [ft.Row(sub_row, spacing=S.s2)]),
        ],
        spacing=S.s2,
        tight=True,
    )

    return ft.Card(
        content=ft.Column(
            [
                # Color accent bar at top
                ft.Container(height=3, bgcolor=accent_color,
                             border_radius=ft.border_radius.only(
                                 top_left=R.lg, top_right=R.lg)),
                ft.Container(content=body, padding=ft.padding.all(S.s5)),
            ],
            spacing=0, tight=True,
        ),
        color=theme.surface,
        elevation=E.level_1,
        shape=ft.RoundedRectangleBorder(radius=R.lg),
        width=width,
    )


def ng_nav_item(
    theme: NGTheme,
    label: str,
    *,
    icon: str = ft.icons.CIRCLE_OUTLINED,
    active: bool = False,
    badge_count: int = 0,
    on_click=None,
) -> ft.Container:
    """
    Sidebar navigation item molecule.
    Renders differently for active vs. inactive state.
    Uses the always-dark sidebar color layer from NGTheme.
    """
    icon_color  = theme.sidebar_active if active else theme.sidebar_text
    label_color = theme.sidebar_active if active else theme.sidebar_text
    bg          = f"rgba(77,163,217,0.18)" if active else "transparent"

    row_children = [
        ft.Icon(icon, size=16, color=icon_color),
        ft.Text(label, size=13, weight=ft.FontWeight.W_500, color=label_color,
                expand=True),
    ]
    if badge_count > 0:
        row_children.append(
            ft.Container(
                content=ft.Text(str(badge_count), size=10, weight=ft.FontWeight.W_700,
                                color="white"),
                bgcolor=theme.error,
                border_radius=_border_radius(R.full),
                width=max(20, len(str(badge_count)) * 8 + 8),
                height=18,
                alignment=ft.alignment.center,
            )
        )

    return ft.Container(
        content=ft.Row(row_children, spacing=S.s3,
                       vertical_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=bg,
        border_radius=_border_radius(R.md),
        padding=_pad(v=S.s2, h=S.s3),
        margin=ft.margin.symmetric(vertical=1, horizontal=S.s2),
        on_click=on_click,
    )


def ng_input_field(
    theme: NGTheme,
    label: str,
    *,
    hint_text: str = "",
    helper_text: str = "",
    error_text: str = "",
    required: bool = False,
    password: bool = False,
    prefix_icon: str | None = None,
    value: str = "",
    on_change=None,
    width: int | None = None,
) -> ft.Column:
    """
    Full form field molecule: label row + text field + helper/error text.
    Composes ng_text_field with an explicit label control above it.
    """
    label_text = f"{label}{' *' if required else ''}"
    return ft.Column(
        [
            ft.Text(label_text, size=13, weight=ft.FontWeight.W_500,
                    color=theme.text_secondary),
            ng_text_field(
                theme,
                hint_text=hint_text,
                helper_text=helper_text,
                error_text=error_text,
                password=password,
                prefix_icon=prefix_icon,
                value=value,
                on_change=on_change,
                width=width,
            ),
        ],
        spacing=S.s1,
        tight=True,
    )


def ng_node_status_card(
    theme: NGTheme,
    name: str,
    ip: str,
    node_type: str,
    status: str = "online",
    *,
    cpu: str = "",
    memory: str = "",
    uptime: str = "",
    on_click=None,
) -> ft.Container:
    """
    Network node status card molecule.
    status: "online" | "warning" | "critical" | "offline"
    """
    _status_colors = {
        "online":   (theme.success,   theme.success_subtle, theme.outline_variant),
        "warning":  (theme.warning,   theme.warning_subtle, theme.warning),
        "critical": (theme.error,     theme.error_subtle,   theme.error),
        "offline":  (theme.text_disabled, theme.surface_variant, theme.outline),
    }
    dot_color, bg_color, border_color = _status_colors.get(status, _status_colors["online"])

    # Type badge
    type_badge = ft.Container(
        content=ft.Text(node_type.upper(), size=9, weight=ft.FontWeight.W_700,
                        color=theme.primary),
        bgcolor=theme.primary_subtle,
        border_radius=_border_radius(R.sm),
        padding=_pad(v=1, h=5),
    )
    if status == "critical":
        type_badge = ft.Container(
            content=ft.Text(node_type.upper(), size=9, weight=ft.FontWeight.W_700,
                            color=theme.error),
            bgcolor=theme.error_subtle,
            border_radius=_border_radius(R.sm),
            padding=_pad(v=1, h=5),
        )
    elif status == "warning":
        type_badge = ft.Container(
            content=ft.Text(node_type.upper(), size=9, weight=ft.FontWeight.W_700,
                            color=theme.warning),
            bgcolor=theme.warning_subtle,
            border_radius=_border_radius(R.sm),
            padding=_pad(v=1, h=5),
        )

    metrics = []
    if cpu:
        metrics.append(
            ft.Row([
                ft.Text("CPU", size=10, color=theme.text_secondary),
                ft.Text(cpu, size=10, weight=ft.FontWeight.W_500,
                        color=theme.text_primary, expand=True,
                        text_align=ft.TextAlign.RIGHT),
            ])
        )
    if memory:
        metrics.append(
            ft.Row([
                ft.Text("MEM", size=10, color=theme.text_secondary),
                ft.Text(memory, size=10, weight=ft.FontWeight.W_500,
                        color=theme.text_primary, expand=True,
                        text_align=ft.TextAlign.RIGHT),
            ])
        )
    if uptime:
        metrics.append(
            ft.Row([
                ft.Text("UP", size=10, color=theme.text_secondary),
                ft.Text(uptime, size=10, weight=ft.FontWeight.W_500,
                        color=theme.success, expand=True,
                        text_align=ft.TextAlign.RIGHT),
            ])
        )

    return ft.Container(
        content=ft.Column(
            [
                ft.Row([
                    ft.Container(width=8, height=8, bgcolor=dot_color,
                                 border_radius=_border_radius(R.full)),
                    ft.Container(content=type_badge, expand=True,
                                 alignment=ft.alignment.center_right),
                ], spacing=S.s2,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Text(name, size=12, weight=ft.FontWeight.W_500,
                        color=theme.text_primary),
                ft.Text(ip, size=10, color=theme.text_secondary,
                        font_family="Roboto Mono"),
                *([] if not metrics else [
                    ft.Divider(thickness=0.5, color=theme.outline_variant),
                    ft.Column(metrics, spacing=2, tight=True),
                ]),
            ],
            spacing=S.s2,
            tight=True,
        ),
        bgcolor=bg_color,
        border=_border(border_color),
        border_radius=_border_radius(R.md),
        padding=ft.padding.all(S.s3),
        on_click=on_click,
    )
