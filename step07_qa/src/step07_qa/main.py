#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step07_qa.crew import Step07Qa

    print("=" * 60)
    print("  STEP 07 - QA ENGINEERING")
    print("  Generates test suites for all code")
    print("=" * 60)

    required = {
        "04_database.sql": "Step 04",
        "05_backend.md": "Step 05",
        "06_frontend.md": "Step 06",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    database_content = (PIPELINE_DATA / "04_database.sql").read_text(encoding="utf-8")
    backend_content = (PIPELINE_DATA / "05_backend.md").read_text(encoding="utf-8")
    frontend_content = (PIPELINE_DATA / "06_frontend.md").read_text(encoding="utf-8")
    print("📄 Loaded database schema, backend, and frontend code")

    inputs = {
        'database_content': database_content,
        'backend_content': backend_content,
        'frontend_content': frontend_content,
    }

    while True:
        print("\n🚀 Running QA engineering...\n")
        result = Step07Qa().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "07_tests.md"
        output_path.write_text(str(result), encoding="utf-8")
        print("\n" + "=" * 60)
        print("✅ Step 07 Complete!")
        print(f"   Test Suites: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 08, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 07 approved. Run step08_evaluation next.")
            break
        print("\n🔄 Re-running Step 07...")
