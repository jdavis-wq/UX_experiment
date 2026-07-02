"""
Northrop Grumman Design System — Theme
=======================================
v1.0

Provides:
  NGTheme      — semantic token dataclass for light or dark mode.
                 Pass an instance into every component factory.
  light_theme  — pre-built NGTheme for light mode
  dark_theme   — pre-built NGTheme for dark mode
  get_flet_light_theme() — returns ft.Theme wired to NG color scheme
  get_flet_dark_theme()  — returns ft.Theme wired to NG dark color scheme

Usage:
    import flet as ft
    from ng_theme import light_theme, dark_theme, get_flet_light_theme, get_flet_dark_theme

    def main(page: ft.Page):
        page.theme      = get_flet_light_theme()
        page.dark_theme = get_flet_dark_theme()
        page.theme_mode = ft.ThemeMode.LIGHT
"""

from dataclasses import dataclass
from ng_tokens import NGColorTokens as C

try:
    import flet as ft
    _FLET_AVAILABLE = True
except ImportError:
    _FLET_AVAILABLE = False


@dataclass
class NGTheme:
    """
    Semantic color aliases for a single theme mode.
    Components accept an NGTheme instance so they remain
    decoupled from global page state.

    Attributes follow a  role_variant  naming convention matching
    the Material Design 3 color-role system.
    """
    mode: str  # "light" | "dark"

    # ── Surfaces ─────────────────────────────────────────────────────────────
    bg:              str = C.white
    bg_variant:      str = C.gray_100
    surface:         str = C.white
    surface_variant: str = "#EFF2F7"
    surface_raised:  str = C.white
    overlay:         str = "rgba(0,105,176,0.05)"

    # ── Primary (NG Blue) ─────────────────────────────────────────────────────
    primary:                  str = C.blue_500
    primary_hover:            str = C.blue_600
    primary_active:           str = C.blue_700
    primary_subtle:           str = C.blue_50
    on_primary:               str = C.white
    primary_container:        str = C.blue_100
    on_primary_container:     str = C.blue_900

    # ── Secondary (NG Navy) ───────────────────────────────────────────────────
    secondary:                str = C.navy_500
    secondary_hover:          str = C.navy_600
    secondary_active:         str = C.navy_700
    secondary_subtle:         str = C.navy_50
    on_secondary:             str = C.white
    secondary_container:      str = C.navy_100
    on_secondary_container:   str = C.navy_900

    # ── Sidebar (always dark-navy regardless of mode) ─────────────────────────
    sidebar_bg:     str = C.navy_800
    sidebar_text:   str = "rgba(255,255,255,0.7)"
    sidebar_active: str = C.white
    sidebar_accent: str = C.blue_300
    sidebar_hover:  str = "rgba(255,255,255,0.08)"

    # ── Text ──────────────────────────────────────────────────────────────────
    text_primary:   str = C.gray_900
    text_secondary: str = C.gray_700
    text_disabled:  str = C.gray_400
    text_inverse:   str = C.white
    text_brand:     str = C.blue_500

    # ── Borders ───────────────────────────────────────────────────────────────
    outline:         str = C.gray_300
    outline_variant: str = C.gray_200

    # ── Semantic States ───────────────────────────────────────────────────────
    error:          str = C.error_700
    error_subtle:   str = C.error_50
    on_error:       str = C.white

    warning:        str = C.warning_700
    warning_subtle: str = C.warning_50
    on_warning:     str = C.white

    success:        str = C.success_700
    success_subtle: str = C.success_50
    on_success:     str = C.white

    info:           str = C.info_500
    info_subtle:    str = C.info_50
    on_info:        str = C.white

    # ── Convenience helpers ───────────────────────────────────────────────────
    def is_dark(self) -> bool:
        return self.mode == "dark"

    def semantic_color(self, severity: str) -> str:
        """Return foreground color for a severity label."""
        return {
            "error":   self.error,
            "warning": self.warning,
            "success": self.success,
            "info":    self.info,
        }.get(severity, self.primary)

    def semantic_bg(self, severity: str) -> str:
        """Return background color for a severity label."""
        return {
            "error":   self.error_subtle,
            "warning": self.warning_subtle,
            "success": self.success_subtle,
            "info":    self.info_subtle,
        }.get(severity, self.primary_subtle)


# ── Pre-built light theme ─────────────────────────────────────────────────────
light_theme = NGTheme(
    mode            = "light",
    bg              = C.white,
    bg_variant      = "#F5F7FA",
    surface         = C.white,
    surface_variant = "#EFF2F7",
    surface_raised  = C.white,
    overlay         = "rgba(0,105,176,0.05)",

    primary               = C.blue_500,
    primary_hover         = C.blue_600,
    primary_active        = C.blue_700,
    primary_subtle        = C.blue_50,
    on_primary            = C.white,
    primary_container     = C.blue_100,
    on_primary_container  = C.blue_900,

    secondary               = C.navy_500,
    secondary_hover         = C.navy_600,
    secondary_active        = C.navy_700,
    secondary_subtle        = C.navy_50,
    on_secondary            = C.white,
    secondary_container     = C.navy_100,
    on_secondary_container  = C.navy_900,

    sidebar_bg     = C.navy_800,
    sidebar_text   = "rgba(255,255,255,0.70)",
    sidebar_active = C.white,
    sidebar_accent = C.blue_300,
    sidebar_hover  = "rgba(255,255,255,0.08)",

    text_primary   = C.gray_900,
    text_secondary = C.gray_700,
    text_disabled  = C.gray_400,
    text_inverse   = C.white,
    text_brand     = C.blue_500,

    outline         = C.gray_300,
    outline_variant = C.gray_200,

    error          = C.error_700,
    error_subtle   = C.error_50,
    on_error       = C.white,
    warning        = C.warning_700,
    warning_subtle = C.warning_50,
    on_warning     = C.white,
    success        = C.success_700,
    success_subtle = C.success_50,
    on_success     = C.white,
    info           = C.info_500,
    info_subtle    = C.info_50,
    on_info        = C.white,
)

# ── Pre-built dark theme ──────────────────────────────────────────────────────
dark_theme = NGTheme(
    mode            = "dark",
    bg              = "#0D1117",
    bg_variant      = "#161B22",
    surface         = "#1C2230",
    surface_variant = "#21293A",
    surface_raised  = "#252D3D",
    overlay         = "rgba(77,163,217,0.08)",

    primary               = "#4DA3D9",
    primary_hover         = "#6BB5E3",
    primary_active        = "#80BDE7",
    primary_subtle        = "rgba(0,105,176,0.15)",
    on_primary            = "#00243A",
    primary_container     = C.blue_800,
    on_primary_container  = C.blue_100,

    secondary               = "#6A81C8",
    secondary_hover         = "#8497D3",
    secondary_active        = "#94A5D8",
    secondary_subtle        = "rgba(0,38,154,0.15)",
    on_secondary            = "#000D47",
    secondary_container     = C.navy_800,
    on_secondary_container  = C.navy_100,

    sidebar_bg     = "#0A0F1A",
    sidebar_text   = "rgba(255,255,255,0.60)",
    sidebar_active = C.white,
    sidebar_accent = "#4DA3D9",
    sidebar_hover  = "rgba(255,255,255,0.06)",

    text_primary   = "#E8EDF5",
    text_secondary = "#8A9AB5",
    text_disabled  = "#4A5568",
    text_inverse   = "#0D1117",
    text_brand     = "#4DA3D9",

    outline         = "#1E2A3D",
    outline_variant = "#172030",

    error          = "#F47D7D",
    error_subtle   = "rgba(244,125,125,0.12)",
    on_error       = "#4A0000",
    warning        = "#FFBA57",
    warning_subtle = "rgba(255,186,87,0.10)",
    on_warning     = "#3D1F00",
    success        = "#6DC86F",
    success_subtle = "rgba(109,200,111,0.12)",
    on_success     = "#003300",
    info           = "#4DA3D9",
    info_subtle    = "rgba(77,163,217,0.12)",
    on_info        = "#00243A",
)


# ── Flet ft.Theme factories ───────────────────────────────────────────────────
def get_flet_light_theme() -> "ft.Theme":
    """
    Returns a Flet ft.Theme configured with the NG light color scheme.
    Assign to page.theme.
    """
    if not _FLET_AVAILABLE:
        raise ImportError("flet is not installed. Run: pip install flet")

    return ft.Theme(
        color_scheme_seed=C.blue_500,
        use_material3=True,
        font_family="Roboto",
        color_scheme=ft.ColorScheme(
            brightness=ft.Brightness.LIGHT,
            primary=C.blue_500,
            on_primary=C.white,
            primary_container=C.blue_100,
            on_primary_container=C.blue_900,
            secondary=C.navy_500,
            on_secondary=C.white,
            secondary_container=C.navy_100,
            on_secondary_container=C.navy_900,
            surface=C.white,
            on_surface=C.gray_900,
            surface_variant="#EFF2F7",
            on_surface_variant=C.gray_700,
            background=C.white,
            on_background=C.gray_900,
            error=C.error_700,
            on_error=C.white,
            error_container=C.error_50,
            on_error_container=C.error_700,
            outline=C.gray_300,
            outline_variant=C.gray_200,
            tertiary=C.blue_300,
            on_tertiary=C.blue_900,
        ),
        elevated_button_theme=ft.ElevatedButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
                elevation={"": 1, "hovered": 3},
            )
        ),
        filled_button_theme=ft.FilledButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        outlined_button_theme=ft.OutlinedButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        text_button_theme=ft.TextButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        card_theme=ft.CardTheme(
            elevation=1,
            shape=ft.RoundedRectangleBorder(radius=12),
            color=C.white,
        ),
        input_decoration_theme=ft.InputDecorationTheme(
            border=ft.OutlineInputBorder(
                border_radius=ft.BorderRadius(4, 4, 4, 4),
                border_side=ft.BorderSide(1.5, C.gray_300),
            ),
            focused_border=ft.OutlineInputBorder(
                border_radius=ft.BorderRadius(4, 4, 4, 4),
                border_side=ft.BorderSide(2, C.blue_500),
            ),
            error_border=ft.OutlineInputBorder(
                border_radius=ft.BorderRadius(4, 4, 4, 4),
                border_side=ft.BorderSide(1.5, C.error_700),
            ),
            label_style=ft.TextStyle(color=C.gray_700, size=14),
            hint_style=ft.TextStyle(color=C.gray_400, size=14),
            helper_style=ft.TextStyle(color=C.gray_600, size=12),
            error_style=ft.TextStyle(color=C.error_700, size=12),
        ),
        chip_theme=ft.ChipTheme(
            shape=ft.RoundedRectangleBorder(radius=9999),
        ),
    )


def get_flet_dark_theme() -> "ft.Theme":
    """
    Returns a Flet ft.Theme configured with the NG dark color scheme.
    Assign to page.dark_theme.
    """
    if not _FLET_AVAILABLE:
        raise ImportError("flet is not installed. Run: pip install flet")

    return ft.Theme(
        color_scheme_seed=C.blue_500,
        use_material3=True,
        font_family="Roboto",
        color_scheme=ft.ColorScheme(
            brightness=ft.Brightness.DARK,
            primary="#4DA3D9",
            on_primary="#00243A",
            primary_container=C.blue_800,
            on_primary_container=C.blue_100,
            secondary="#6A81C8",
            on_secondary="#000D47",
            secondary_container=C.navy_800,
            on_secondary_container=C.navy_100,
            surface="#1C2230",
            on_surface="#E8EDF5",
            surface_variant="#21293A",
            on_surface_variant="#8A9AB5",
            background="#0D1117",
            on_background="#E8EDF5",
            error="#F47D7D",
            on_error="#4A0000",
            error_container="rgba(244,125,125,0.12)",
            on_error_container="#F47D7D",
            outline="#1E2A3D",
            outline_variant="#172030",
            tertiary="#4DA3D9",
            on_tertiary="#00243A",
        ),
        elevated_button_theme=ft.ElevatedButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        filled_button_theme=ft.FilledButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        outlined_button_theme=ft.OutlinedButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        text_button_theme=ft.TextButtonTheme(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=9999),
            )
        ),
        card_theme=ft.CardTheme(
            elevation=2,
            shape=ft.RoundedRectangleBorder(radius=12),
            color="#1C2230",
        ),
        input_decoration_theme=ft.InputDecorationTheme(
            border=ft.OutlineInputBorder(
                border_radius=ft.BorderRadius(4, 4, 4, 4),
                border_side=ft.BorderSide(1.5, "#1E2A3D"),
            ),
            focused_border=ft.OutlineInputBorder(
                border_radius=ft.BorderRadius(4, 4, 4, 4),
                border_side=ft.BorderSide(2, "#4DA3D9"),
            ),
            error_border=ft.OutlineInputBorder(
                border_radius=ft.BorderRadius(4, 4, 4, 4),
                border_side=ft.BorderSide(1.5, "#F47D7D"),
            ),
            label_style=ft.TextStyle(color="#8A9AB5", size=14),
            hint_style=ft.TextStyle(color="#4A5568", size=14),
            helper_style=ft.TextStyle(color="#8A9AB5", size=12),
            error_style=ft.TextStyle(color="#F47D7D", size=12),
        ),
        chip_theme=ft.ChipTheme(
            shape=ft.RoundedRectangleBorder(radius=9999),
        ),
    )
