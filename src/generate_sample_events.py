from __future__ import annotations

import random
from pathlib import Path
from datetime import datetime

import pandas as pd


def generate_events(n: int = 500, seed: int = 42) -> pd.DataFrame:
    random.seed(seed)

    players = [
        ("P01", "Carlos", "MID"),
        ("P02", "Nico", "DEF"),
        ("P03", "Bastián", "FWD"),
        ("P04", "Matías", "MID"),
        ("P05", "Javi", "WNG"),
    ]

    actions = [
        ("PASS", "Complete"),
        ("PASS", "Incomplete"),
        ("SHOT", "On target"),
        ("SHOT", "Off target"),
        ("RECOVERY", "Won"),
        ("DUEL", "Won"),
        ("DUEL", "Lost"),
    ]

    zones = ["Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9"]

    # 2 partidos ficticios
    sessions = [
        ("S001", "U10", "Rival_01", "2025-10-25"),
        ("S002", "U10", "Rival_02", "2025-11-08"),
    ]

    rows = []
    for i in range(1, n + 1):
        session_id, category, opponent, date_str = random.choice(sessions)
        player_id, player_name, position = random.choice(players)
        action, result = random.choice(actions)

        minute = random.randint(1, 60)
        second = random.randint(0, 59)

        zone = random.choice(zones)

        # métricas simples por evento (ejemplo)
        is_positive = 1 if result in ("Complete", "On target", "Won") else 0

        rows.append(
            {
                "event_id": i,
                "session_id": session_id,
                "category": category,
                "opponent": opponent,
                "date": date_str,
                "player_id": player_id,
                "player_name": player_name,
                "position": position,
                "minute": minute,
                "second": second,
                "action": action,
                "result": result,
                "zone": zone,
                "is_positive": is_positive,
            }
        )

    df = pd.DataFrame(rows)

    # ordenar como si viniera de un sistema de tagging
    df = df.sort_values(["date", "session_id", "minute", "second", "event_id"]).reset_index(drop=True)

    return df


def main() -> None:
    out_dir = Path("data") / "sample"
    out_dir.mkdir(parents=True, exist_ok=True)

    df = generate_events(n=500, seed=42)

    out_path = out_dir / "events_sample.csv"
    df.to_csv(out_path, index=False, encoding="utf-8")

    print(f"[OK] Generated: {out_path} ({len(df)} rows) at {datetime.now().isoformat(timespec='seconds')}")


if __name__ == "__main__":
    main()
