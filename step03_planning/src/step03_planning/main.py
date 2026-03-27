#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step03_planning.crew import Step03Planning

    print("=" * 60)
    print("  STEP 03 - TASK PLANNING")
    print("  Breaks architecture into development tasks")
    print("=" * 60)

    arch_path = PIPELINE_DATA / "02_architecture.md"
    if not arch_path.exists():
        print(f"❌ Required input not found: {arch_path}")
        print("   Please run Step 02 first.")
        sys.exit(1)

    architecture_content = arch_path.read_text(encoding="utf-8")
    print(f"📄 Loaded architecture from: {arch_path}")

    inputs = {'architecture_content': architecture_content}

    while True:
        print("\n🚀 Running task planning...\n")
        result = Step03Planning().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "03_task_plan.json"
        output_path.write_text(str(result), encoding="utf-8")
        print("\n" + "=" * 60)
        print("✅ Step 03 Complete!")
        print(f"   Task Plan: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 04, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 03 approved. Run step04_database next.")
            break
        print("\n🔄 Re-running Step 03...")
