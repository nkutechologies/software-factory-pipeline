#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step06_frontend.crew import Step06Frontend

    print("=" * 60)
    print("  STEP 06 - FRONTEND DEVELOPMENT")
    print("  Generates React UI components")
    print("=" * 60)

    required = {
        "02_architecture.md": "Step 02",
        "03_task_plan.json": "Step 03",
        "05_backend.md": "Step 05",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    architecture_content = (PIPELINE_DATA / "02_architecture.md").read_text(encoding="utf-8")
    task_plan_content = (PIPELINE_DATA / "03_task_plan.json").read_text(encoding="utf-8")
    backend_content = (PIPELINE_DATA / "05_backend.md").read_text(encoding="utf-8")
    print("📄 Loaded architecture, task plan, and backend code")

    inputs = {
        'architecture_content': architecture_content,
        'task_plan_content': task_plan_content,
        'backend_content': backend_content,
    }

    while True:
        print("\n🚀 Running frontend development...\n")
        Step06Frontend().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "06_frontend.md"
        print("\n" + "=" * 60)
        print("✅ Step 06 Complete!")
        print(f"   Frontend Code: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 07, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 06 approved. Run step07_qa next.")
            break
        print("\n🔄 Re-running Step 06...")
