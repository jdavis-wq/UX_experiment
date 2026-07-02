"""
Northrop Grumman Design System — Design Tokens
===============================================
v1.0 | Material UI · Atomic Design Principles

Brand color sources:
  Primary   : Honolulu Blue  #0069B0  PMS 2196 C  RGB(0, 105, 176)
  Secondary : Navy Blue      #00269A  PMS 2736 C  RGB(0, 38, 154)

Token layers (use the outermost layer in components):
  Raw Palette  →  NGColorTokens
  Semantic     →  NGLightTokens / NGDarkTokens  (in ng_theme.py)
  Component    →  ng_components.py
"""


class NGColorTokens:
    """Raw color palette — do not reference directly in components.
    Use NGTheme semantic aliases instead."""

    # ─── NG Blue Scale — Primary Brand (Honolulu Blue PMS 2196 C) ───────────
    blue_50  = "#E0F0FB"
    blue_100 = "#B3D5F4"
    blue_200 = "#80B9EC"
    blue_300 = "#4D9CE3"
    blue_400 = "#2685D9"
    blue_500 = "#0069B0"  # ★ Brand primary
    blue_600 = "#005EA0"
    blue_700 = "#00508C"
    blue_800 = "#004378"
    blue_900 = "#002C52"

    # ─── NG Navy Scale — Secondary Brand (PMS 2736 C) ───────────────────────
    navy_50  = "#E5E9F5"
    navy_100 = "#BEC8E7"
    navy_200 = "#94A5D8"
    navy_300 = "#6A81C8"
    navy_400 = "#4866BC"
    navy_500 = "#00269A"  # ★ Brand secondary
    navy_600 = "#00228A"
    navy_700 = "#001C77"
    navy_800 = "#001665"
    navy_900 = "#000D47"

    # ─── Neutral Gray Scale ──────────────────────────────────────────────────
    gray_50  = "#FAFAFA"
    gray_100 = "#F5F5F5"
    gray_200 = "#EEEEEE"
    gray_300 = "#E0E0E0"
    gray_400 = "#BDBDBD"
    gray_500 = "#9E9E9E"
    gray_600 = "#757575"
    gray_700 = "#616161"
    gray_800 = "#424242"
    gray_900 = "#212121"

    # ─── Absolute ───────────────────────────────────────────────────────────
    white = "#FFFFFF"
    black = "#000000"

    # ─── Semantic State Colors ───────────────────────────────────────────────
    error_50  = "#FFEBEE"
    error_500 = "#F44336"
    error_700 = "#D32F2F"

    warning_50  = "#FFF3E0"
    warning_500 = "#FF9800"
    warning_700 = "#E65100"

    success_50  = "#E8F5E9"
    success_500 = "#4CAF50"
    success_700 = "#2E7D32"

    info_50  = "#E0F0FB"
    info_500 = "#0069B0"
    info_700 = "#004378"


class NGTypographyTokens:
    """
    Material Design 3 type scale.
    Values: (size_px, line_height_px, letter_spacing_px, weight)
    Use with Flet ft.TextStyle.
    """
    font_family      = "Roboto"
    font_family_mono = "Roboto Mono"

    # font weight constants (match ft.FontWeight values)
    weight_light   = "w300"
    weight_regular = "w400"
    weight_medium  = "w500"
    weight_bold    = "w700"
    weight_black   = "w900"

    # ─── Type Scale ─────────────────────────────────────────────────────────
    # (size, line_height, letter_spacing, weight)
    display_lg = (57, 64, -0.25, "w400")
    display_md = (45, 52,  0.00, "w400")
    display_sm = (36, 44,  0.00, "w400")

    headline_lg = (32, 40, 0.00, "w400")
    headline_md = (28, 36, 0.00, "w400")
    headline_sm = (24, 32, 0.00, "w400")

    title_lg = (22, 28, 0.00,  "w500")
    title_md = (16, 24, 0.15,  "w500")
    title_sm = (14, 20, 0.10,  "w500")

    body_lg = (16, 24, 0.50, "w400")
    body_md = (14, 20, 0.25, "w400")
    body_sm = (12, 16, 0.40, "w400")

    label_lg = (14, 20, 0.10, "w500")
    label_md = (12, 16, 0.50, "w500")
    label_sm = (11, 16, 0.50, "w500")


class NGSpacingTokens:
    """
    4px base grid spacing tokens.
    Use as padding/margin integer values in Flet.
    """
    s0  = 0
    s1  = 4
    s2  = 8
    s3  = 12
    s4  = 16
    s5  = 20
    s6  = 24
    s7  = 28
    s8  = 32
    s10 = 40
    s12 = 48
    s16 = 64
    s20 = 80
    s24 = 96

    # Semantic aliases
    xs   = s1   # 4   — icon gap, tight nudge
    sm   = s2   # 8   — inline item gap
    md   = s4   # 16  — card padding
    lg   = s6   # 24  — section gap
    xl   = s8   # 32  — page padding
    xxl  = s12  # 48  — section breaks


class NGRadiusTokens:
    """Border radius tokens."""
    none = 0
    xs   = 2
    sm   = 4
    md   = 8
    lg   = 12
    xl   = 16
    xxl  = 24
    full = 9999  # pill shape


class NGElevationTokens:
    """
    Flet elevation levels.
    Higher values = larger shadow.
    """
    level_0 = 0
    level_1 = 1
    level_2 = 2
    level_3 = 4
    level_4 = 6
    level_5 = 8


class NGDurationTokens:
    """Animation duration tokens (milliseconds)."""
    fast   = 100
    normal = 200
    slow   = 300
    xslow  = 500


# ── Convenience re-exports ───────────────────────────────────────────────────
C = NGColorTokens
T = NGTypographyTokens
S = NGSpacingTokens
R = NGRadiusTokens
E = NGElevationTokens
