#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step05_backend.crew import Step05Backend

    print("=" * 60)
    print("  STEP 05 - BACKEND DEVELOPMENT")
    print("  Generates Node.js/Express API code")
    print("=" * 60)

    required = {
        "02_architecture.md": "Step 02",
        "03_task_plan.json": "Step 03",
        "04_database.sql": "Step 04",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    architecture_content = (PIPELINE_DATA / "02_architecture.md").read_text(encoding="utf-8")
    task_plan_content = (PIPELINE_DATA / "03_task_plan.json").read_text(encoding="utf-8")
    database_content = (PIPELINE_DATA / "04_database.sql").read_text(encoding="utf-8")
    print("📄 Loaded architecture, task plan, and database schema")

    inputs = {
        'architecture_content': architecture_content,
        'task_plan_content': task_plan_content,
        'database_content': database_content,
    }

    while True:
        print("\n🚀 Running backend development...\n")
        Step05Backend().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "05_backend.md"
        print("\n" + "=" * 60)
        print("✅ Step 05 Complete!")
        print(f"   Backend Code: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 06, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 05 approved. Run step06_frontend next.")
            break
        print("\n🔄 Re-running Step 05...")
