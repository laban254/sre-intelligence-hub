#!/usr/bin/env python3
"""
Quick/Slow Toggle for Jupyter Notebooks

Provides a consistent way to toggle between quick mode (fast iteration)
and full mode (complete runs) in Jupyter notebooks.

Usage in notebooks:
    from notebook_toggle import toggle_mode, get_mode
    
    # Check current mode
    mode = get_mode()  # Returns "quick" or "full"
    
    # Toggle mode (use in cell with mode selector)
    toggle_mode("quick")  # or "full"
    
    # Use in code:
    if get_mode() == "quick":
        n_samples = 100
        n_iter = 10
    else:
        n_samples = 1000
        n_iter = 100
"""

import os
from enum import Enum
from typing import Any, Dict, Optional


class Mode(Enum):
    QUICK = "quick"
    FULL = "full"


# Environment variable key
MODE_KEY = "NOTEBOOK_MODE"

# Default mode
DEFAULT_MODE = Mode.QUICK

# Quick mode settings (fast iteration)
QUICK_SETTINGS = {
    "n_samples": 100,
    "n_iter": 10,
    "test_size": 0.2,
    "n_folds": 2,
    "n_jobs": 1,
    "max_samples": 100,
    "cache_data": False,
    "verbose": False,
}

# Full mode settings (complete runs)
FULL_SETTINGS = {
    "n_samples": 1000,
    "n_iter": 100,
    "test_size": 0.2,
    "n_folds": 5,
    "n_jobs": -1,
    "max_samples": None,
    "cache_data": True,
    "verbose": True,
}


def get_mode() -> str:
    """
    Get the current notebook mode.
    
    Returns:
        "quick" or "full"
    """
    mode = os.environ.get(MODE_KEY, DEFAULT_MODE.value).lower()
    return mode


def set_mode(mode: str) -> None:
    """
    Set the notebook mode.
    
    Args:
        mode: "quick" or "full"
    """
    valid_modes = [m.value for m in Mode]
    if mode.lower() not in valid_modes:
        raise ValueError(f"Invalid mode: {mode}. Must be 'quick' or 'full'")
    
    os.environ[MODE_KEY] = mode.lower()
    print(f"Mode set to: {mode.lower()}")
    
    # Reload any cached settings
    _clear_cache()


def toggle_mode(new_mode: Optional[str] = None) -> str:
    """
    Toggle between quick and full mode.
    
    Args:
        new_mode: Optional mode to set (toggles if not provided)
    
    Returns:
        The new mode
    """
    if new_mode is None:
        current = get_mode()
        new_mode = Mode.FULL.value if current == Mode.QUICK.value else Mode.QUICK.value
    
    set_mode(new_mode)
    return new_mode


def get_quick_setting(key: str, default: Any = None) -> Any:
    """
    Get a quick mode setting value.
    
    Args:
        key: Setting key
        default: Default value if key not found
    
    Returns:
        Setting value
    """
    return QUICK_SETTINGS.get(key, default)


def get_full_setting(key: str, default: Any = None) -> Any:
    """
    Get a full mode setting value.
    
    Args:
        key: Setting key
        default: Default value if key not found
    
    Returns:
        Setting value
    """
    return FULL_SETTINGS.get(key, default)


def get_setting(key: str, default: Any = None) -> Any:
    """
    Get the current mode's setting value.
    
    Args:
        key: Setting key
        default: Default value if key not found
    
    Returns:
        Setting value based on current mode
    """
    current_mode = get_mode()
    settings = QUICK_SETTINGS if current_mode == Mode.QUICK.value else FULL_SETTINGS
    return settings.get(key, default)


def get_all_settings() -> Dict[str, Any]:
    """
    Get all settings for the current mode.
    
    Returns:
        Dict of settings
    """
    current_mode = get_mode()
    return QUICK_SETTINGS.copy() if current_mode == Mode.QUICK.value else FULL_SETTINGS.copy()


def describe_mode() -> str:
    """
    Get a description of the current mode.
    
    Returns:
        Description string
    """
    mode = get_mode()
    settings = get_all_settings()
    
    desc = f"Mode: {mode.upper()}\n"
    desc += f"{'='*40}\n"
    desc += "Settings:\n"
    for key, value in settings.items():
        desc += f"  {key}: {value}\n"
    return desc


# Cache for tracking cell execution
_cell_cache: Dict[int, bool] = {}


def cache_cell(cell_id: int) -> bool:
    """
    Mark a cell as cached (executed).
    
    Args:
        cell_id: Cell ID or index
    
    Returns:
        True if newly cached, False if already cached
    """
    if cell_id in _cell_cache:
        return False
    _cell_cache[cell_id] = True
    return True


def is_cell_cached(cell_id: int) -> bool:
    """
    Check if a cell has been executed.
    
    Args:
        cell_id: Cell ID or index
    
    Returns:
        True if cell was executed
    """
    return cell_id in _cell_cache


def _clear_cache() -> None:
    """Clear the cell cache."""
    global _cell_cache
    _cell_cache = {}


# Quick/Fixed settings for reproducibility
QUICK_FIXED = {
    "random_state": 42,
    "np_random_seed": 42,
    "tf_random_seed": 42,
}

# Full/Fixed settings for reproducibility  
FULL_FIXED = {
    "random_state": 42,
    "np_random_seed": 42,
    "tf_random_seed": 42,
}


def get_fixed_setting(key: str, default: Any = None) -> Any:
    """
    Get a fixed setting value (same for both modes).
    
    Args:
        key: Setting key
        default: Default value if key not found
    
    Returns:
        Setting value
    """
    return QUICK_FIXED.get(key, FULL_FIXED.get(key, default))


# Notebook metadata helpers
NOTEBOOK_META = {
    "version": "1.0",
    "last_updated": None,
    "tested_date": None,
    "python_version": None,
    "runtime_minutes": None,
}


def set_notebook_meta(key: str, value: Any) -> None:
    """
    Set notebook metadata.
    
    Args:
        key: Metadata key
        value: Value to set
    """
    NOTEBOOK_META[key] = value


def get_notebook_meta(key: str, default: Any = None) -> Any:
    """
    Get notebook metadata.
    
    Args:
        key: Metadata key
        default: Default value if key not found
    
    Returns:
        Metadata value
    """
    return NOTEBOOK_META.get(key, default)


# Widget for mode toggle (for use in notebooks with ipywidgets)
def create_mode_widget():
    """
    Create a mode toggle widget for Jupyter notebooks.
    
    Usage:
        from notebook_toggle import create_mode_widget
        widget = create_mode_widget()
        display(widget)
    """
    try:
        import ipywidgets as widgets
    except ImportError:
        print("ipywidgets not installed. Install with: pip install ipywidgets")
        return None
    
    mode_dropdown = widgets.Dropdown(
        options=["quick", "full"],
        value=get_mode(),
        description="Mode:",
        disabled=False,
    )
    
    def on_mode_change(change):
        if change["type"] == "change" and change["name"] == "value":
            set_mode(change["new"])
    
    mode_dropdown.observe(on_mode_change, names="value")
    
    return mode_dropdown


# Display mode info in notebook
def display_mode_info():
    """Display current mode information (for Jupyter notebooks)."""
    from IPython.display import display, HTML
    
    mode = get_mode()
    settings = get_all_settings()
    
    color = "#4CAF50" if mode == "quick" else "#2196F3"
    
    html = f"""
    <div style="
        border: 2px solid {color};
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f5f5f5;
    ">
        <h3 style="color: {color}; margin-top: 0;">
            📊 Current Mode: {mode.upper()}
        </h3>
        <table style="width: 100%;">
    """
    
    for key, value in settings.items():
        html += f"""
            <tr>
                <td style="padding: 5px; font-weight: bold;">{key}:</td>
                <td style="padding: 5px;">{value}</td>
            </tr>
        """
    
    html += """
        </table>
    </div>
    """
    
    display(HTML(html))


# Main execution
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Notebook mode toggle utility"
    )
    parser.add_argument(
        "--mode",
        choices=["quick", "full"],
        help="Set the notebook mode"
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Show current mode and settings"
    )
    
    args = parser.parse_args()
    
    if args.mode:
        set_mode(args.mode)
    
    if args.show or args.mode is None:
        print(describe_mode())
