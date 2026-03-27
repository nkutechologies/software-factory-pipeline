#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step04_database.crew import Step04Database

    print("=" * 60)
    print("  STEP 04 - DATABASE ENGINEERING")
    print("  Generates PostgreSQL schemas from architecture")
    print("=" * 60)

    required = {
        "02_architecture.md": "Step 02",
        "03_task_plan.json": "Step 03",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    architecture_content = (PIPELINE_DATA / "02_architecture.md").read_text(encoding="utf-8")
    task_plan_content = (PIPELINE_DATA / "03_task_plan.json").read_text(encoding="utf-8")
    print("📄 Loaded architecture and task plan")

    inputs = {
        'architecture_content': architecture_content,
        'task_plan_content': task_plan_content,
    }

    while True:
        print("\n🚀 Running database engineering...\n")
        Step04Database().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "04_database.sql"
        print("\n" + "=" * 60)
        print("✅ Step 04 Complete!")
        print(f"   Database Schema: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 05, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 04 approved. Run step05_backend next.")
            break
        print("\n🔄 Re-running Step 04...")
