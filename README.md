Here's the breakdown of what each file does:
ng_tokens.py — pure Python constants, no Flet dependency. Five token classes: NGColorTokens (full blue + navy + gray scales, semantic states), NGTypographyTokens (all 15 MD3 type roles), NGSpacingTokens (4px grid, 14 steps), NGRadiusTokens, and NGElevationTokens. Convenience aliases C, T, S, R, E for terse imports.
ng_theme.py — NGTheme dataclass holding ~40 semantic token aliases (surfaces, primary, secondary, text, border, semantic states). Pre-built light_theme and dark_theme instances, plus get_flet_light_theme() and get_flet_dark_theme() factory functions that return wired ft.Theme objects with Material 3 enabled, button shapes, card radii, and InputDecorationTheme all configured.
ng_components.py — 12 factory functions, all taking theme: NGTheme as their first argument so they're fully portable:

Atoms: ng_button (5 variants, 3 sizes), ng_text_field, ng_chip (3 variants + semantic), ng_alert_banner (4 severities, dismissible), ng_badge, ng_status_pill, ng_divider, ng_label_text, ng_section_header
Molecules: ng_card (header/body/footer slots), ng_kpi_card, ng_nav_item (sidebar), ng_input_field (label+field+helper combo), ng_node_status_card

ng_demo.py — full Flet showcase app with a dark-navy sidebar, topbar, live theme toggle, and 14 navigable sections — one per component type plus color and spacing token viewers.
