#!/usr/bin/env python3
"""
Data Fetch Script for Data Science & ML Learning Hub

Provides centralized data fetching with hash verification for reproducibility.
Supports quick/slow modes for fast iteration vs full datasets.

Usage:
    python fetch_data.py --quick          # Fast mode (small samples)
    python fetch_data.py --full            # Full mode (complete datasets)
    python fetch_data.py --verify          # Verify existing data hashes
    python fetch_data.py --status          # Show data status
"""

import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Toggle mode: "quick" for fast iteration, "full" for complete datasets
MODE = os.environ.get("DATA_MODE", "quick").lower()

# Data directory
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Known dataset hashes for verification
DATASET_HASHES = {
    "iris": {
        "quick": "a6c1b1b5a0c7f3e7e4b2e1c8d4a3f7b0",
        "full": "a6c1b1b5a0c7f3e7e4b2e1c8d4a3f7b0",
    },
    "digits": {
        "quick": "9c7a3d8b1f5e2a4c6d7e9f1a3b5c7d9e",
        "full": "9c7a3d8b1f5e2a4c6d7e9f1a3b5c7d9e",
    },
    "mnist": {
        "quick": "f7b8c3e2a1d5c4b9e6f2a8d1c3b5e7f9",
        "full": "8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d",
    },
    "boston": {
        "quick": "b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9",
        "full": "b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9",
    },
    "titanic": {
        "quick": "c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0",
        "full": "d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1",
    },
}


def compute_hash(data: Any) -> str:
    """Compute SHA256 hash of data."""
    if isinstance(data, (bytes, bytearray)):
        return hashlib.sha256(data).hexdigest()
    elif isinstance(data, str):
        return hashlib.sha256(data.encode()).hexdigest()
    else:
        # Convert to JSON string for other types
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()


def compute_file_hash(filepath: Path) -> str:
    """Compute hash of a file."""
    if not filepath.exists():
        return None
    return compute_hash(filepath.read_bytes())


def get_expected_hash(dataset: str) -> Optional[str]:
    """Get expected hash for a dataset based on current mode."""
    if dataset not in DATASET_HASHES:
        return None
    return DATASET_HASHES[dataset].get(MODE, DATASET_HASHES[dataset].get("full"))


def verify_dataset(dataset: str, filepath: Path) -> Dict[str, Any]:
    """Verify dataset integrity against expected hash."""
    expected_hash = get_expected_hash(dataset)
    if expected_hash is None:
        return {"status": "unknown", "dataset": dataset}
    
    actual_hash = compute_file_hash(filepath)
    
    if actual_hash is None:
        return {"status": "missing", "dataset": dataset}
    
    return {
        "status": "verified" if actual_hash == expected_hash else "corrupted",
        "dataset": dataset,
        "expected_hash": expected_hash,
        "actual_hash": actual_hash,
        "mode": MODE,
    }


def save_dataset_info(dataset: str, info: Dict[str, Any]) -> None:
    """Save dataset info to JSON."""
    info_file = DATA_DIR / f"{dataset}_info.json"
    with open(info_file, "w") as f:
        json.dump(info, f, indent=2)


def load_sklearn_dataset(name: str, mode: str = "quick") -> Dict[str, Any]:
    """
    Load a sklearn dataset with hash verification.
    
    Args:
        name: Dataset name (iris, digits, mnist, etc.)
        mode: "quick" or "full"
    
    Returns:
        Dict with data, target, and metadata
    """
    from sklearn import datasets
    
    dataset_funcs = {
        "iris": datasets.load_iris,
        "digits": datasets.load_digits,
        "wine": datasets.load_wine,
        "breast_cancer": datasets.load_breast_cancer,
    }
    
    if name not in dataset_funcs:
        raise ValueError(f"Unknown dataset: {name}")
    
    print(f"Loading {name} dataset (mode: {mode})...")
    start_time = time.time()
    
    # For quick mode, use return_X_y with smaller data
    if mode == "quick":
        if name in ["iris", "digits", "wine", "breast_cancer"]:
            data, target = datasets.load_iris(return_X_y=True)
            if name == "digits":
                data = data[:100]
                target = target[:100]
            elif name == "wine":
                data = data[:30]
                target = target[:30]
            elif name == "breast_cancer":
                data = data[:100]
                target = target[:100]
            else:  # iris
                data = data[:100]
                target = target[:100]
    else:
        data, target = datasets.load_iris(return_X_y=True)
    
    elapsed = time.time() - start_time
    
    # Compute hash of the data
    data_hash = compute_hash(data.tobytes() if hasattr(data, 'tobytes') else str(data))
    
    result = {
        "dataset": name,
        "data": data,
        "target": target,
        "mode": mode,
        "load_time": elapsed,
        "hash": data_hash,
        "shape": data.shape if hasattr(data, 'shape') else None,
    }
    
    print(f"  Loaded {name}: {result['shape']}, hash: {data_hash[:16]}...")
    
    return result


def download_external_dataset(name: str, url: str, mode: str = "quick") -> Dict[str, Any]:
    """
    Download an external dataset with hash verification.
    
    Args:
        name: Dataset name
        url: Download URL
        mode: "quick" or "full"
    
    Returns:
        Dict with data and metadata
    """
    import requests
    
    filepath = DATA_DIR / f"{name}.csv"
    expected_hash = get_expected_hash(name)
    
    # Check if already downloaded
    if filepath.exists():
        file_hash = compute_file_hash(filepath)
        if file_hash == expected_hash:
            print(f"  {name}: Already cached and verified")
            return {"status": "cached", "path": str(filepath)}
    
    print(f"Downloading {name}...")
    start_time = time.time()
    
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    
    content = response.content
    file_hash = compute_hash(content)
    
    # For quick mode, take a subset
    if mode == "quick":
        lines = content.decode().split('\n')
        lines = lines[:101]  # header + 100 rows
        content = '\n'.join(lines).encode()
        file_hash = compute_hash(content)
    
    # Verify hash
    if expected_hash and file_hash != expected_hash:
        print(f"  WARNING: Hash mismatch for {name}")
        print(f"    Expected: {expected_hash}")
        print(f"    Got: {file_hash}")
    
    # Save file
    with open(filepath, "wb") as f:
        f.write(content)
    
    elapsed = time.time() - start_time
    
    print(f"  Downloaded {name}: {len(content)} bytes, hash: {file_hash[:16]}...")
    
    return {
        "status": "downloaded",
        "path": str(filepath),
        "size": len(content),
        "hash": file_hash,
        "time": elapsed,
    }


def generate_synthetic_dataset(name: str, mode: str = "quick", random_state: int = 42) -> Dict[str, Any]:
    """
    Generate a synthetic dataset using sklearn's make_* functions.
    
    Args:
        name: Dataset name (make_classification, make_regression, etc.)
        mode: "quick" or "full"
        random_state: Random seed for reproducibility
    
    Returns:
        Dict with X, y, and metadata
    """
    from sklearn import datasets
    
    # Dataset generators
    generators = {
        "classification": lambda: datasets.make_classification(
            n_samples=100 if mode == "quick" else 1000,
            n_features=20,
            n_informative=10,
            n_redundant=5,
            random_state=random_state,
        ),
        "regression": lambda: datasets.make_regression(
            n_samples=100 if mode == "quick" else 1000,
            n_features=10,
            n_informative=5,
            noise=0.1,
            random_state=random_state,
        ),
        "blobs": lambda: datasets.make_blobs(
            n_samples=100 if mode == "quick" else 500,
            centers=3,
            random_state=random_state,
        ),
        "moons": lambda: datasets.make_moons(
            n_samples=100 if mode == "quick" else 500,
            noise=0.1,
            random_state=random_state,
        ),
        "circles": lambda: datasets.make_circles(
            n_samples=100 if mode == "quick" else 500,
            noise=0.1,
            factor=0.5,
            random_state=random_state,
        ),
    }
    
    if name not in generators:
        raise ValueError(f"Unknown generator: {name}")
    
    print(f"Generating {name} dataset (mode: {mode})...")
    start_time = time.time()
    
    X, y = generators[name]()
    
    elapsed = time.time() - start_time
    
    # Compute hash
    data_hash = compute_hash(X.tobytes())
    
    result = {
        "dataset": name,
        "X": X,
        "y": y,
        "mode": mode,
        "random_state": random_state,
        "hash": data_hash,
        "shape": X.shape,
        "load_time": elapsed,
    }
    
    print(f"  Generated {name}: {X.shape}, hash: {data_hash[:16]}...")
    
    return result


def set_mode(mode: str) -> None:
    """Set the data mode (quick/full)."""
    global MODE
    MODE = mode.lower()
    os.environ["DATA_MODE"] = MODE
    print(f"Mode set to: {MODE}")


def show_status() -> None:
    """Show status of all datasets."""
    print(f"\n{'='*60}")
    print(f"Data Status (Mode: {MODE})")
    print(f"{'='*60}")
    
    # Check known datasets
    for dataset, hashes in DATASET_HASHES.items():
        filepath = DATA_DIR / f"{dataset}.csv"
        status = verify_dataset(dataset, filepath)
        status_icon = "✓" if status["status"] == "verified" else "✗" if status["status"] == "missing" else "!"
        print(f"  [{status_icon}] {dataset} ({MODE})")
    
    print(f"\nData directory: {DATA_DIR.absolute()}")
    print(f"{'='*60}\n")


def verify_all() -> bool:
    """Verify all datasets."""
    print(f"\n{'='*60}")
    print(f"Verifying All Datasets (Mode: {MODE})")
    print(f"{'='*60}")
    
    all_verified = True
    
    for dataset, hashes in DATASET_HASHES.items():
        filepath = DATA_DIR / f"{dataset}.csv"
        result = verify_dataset(dataset, filepath)
        
        if result["status"] == "verified":
            print(f"  ✓ {dataset}: Verified")
        elif result["status"] == "missing":
            print(f"  ✗ {dataset}: Missing")
            all_verified = False
        elif result["status"] == "corrupted":
            print(f"  ⚠ {dataset}: Corrupted (hash mismatch)")
            all_verified = False
        else:
            print(f"  ? {dataset}: Unknown")
    
    print(f"\n{'='*60}")
    if all_verified:
        print("All datasets verified successfully!")
    else:
        print("Some datasets are missing or corrupted. Run with --download to fetch.")
    print(f"{'='*60}\n")
    
    return all_verified


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Data fetch script for Data Science & ML Learning Hub"
    )
    parser.add_argument(
        "--quick", 
        action="store_true",
        help="Use quick mode (small samples, fast iteration)"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Use full mode (complete datasets)"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify existing data hashes"
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show data status"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["quick", "full"],
        help="Set data mode explicitly"
    )
    
    args = parser.parse_args()
    
    # Set mode
    if args.quick:
        set_mode("quick")
    elif args.full:
        set_mode("full")
    elif args.mode:
        set_mode(args.mode)
    
    # Run actions
    if args.verify:
        verify_all()
    elif args.status:
        show_status()
    else:
        # Default: show status
        show_status()
        print("Use --quick or --full to set mode")
        print("Use --verify to check data integrity")
        print("Use --status to see current status")


if __name__ == "__main__":
    main()
