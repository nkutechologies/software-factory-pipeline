#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step08_evaluation.crew import Step08Evaluation

    print("=" * 60)
    print("  STEP 08 - CODE EVALUATION")
    print("  Scores quality, security, and compliance")
    print("=" * 60)

    required = {
        "01_srs.md": "Step 01",
        "02_architecture.md": "Step 02",
        "04_database.sql": "Step 04",
        "05_backend.md": "Step 05",
        "06_frontend.md": "Step 06",
        "07_tests.md": "Step 07",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    inputs = {
        'srs_content': (PIPELINE_DATA / "01_srs.md").read_text(encoding="utf-8"),
        'architecture_content': (PIPELINE_DATA / "02_architecture.md").read_text(encoding="utf-8"),
        'database_content': (PIPELINE_DATA / "04_database.sql").read_text(encoding="utf-8"),
        'backend_content': (PIPELINE_DATA / "05_backend.md").read_text(encoding="utf-8"),
        'frontend_content': (PIPELINE_DATA / "06_frontend.md").read_text(encoding="utf-8"),
        'tests_content': (PIPELINE_DATA / "07_tests.md").read_text(encoding="utf-8"),
    }
    print("📄 Loaded all pipeline artifacts for evaluation")

    while True:
        print("\n🚀 Running code evaluation...\n")
        Step08Evaluation().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "08_evaluation.json"
        print("\n" + "=" * 60)
        print("✅ Step 08 Complete!")
        print(f"   Evaluation Report: {output_path}")
        if output_path.exists():
            print(f"\n📊 Report Preview:")
            print(output_path.read_text(encoding="utf-8")[:500])
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 09, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 08 approved. Run step09_git_integration next.")
            break
        print("\n🔄 Re-running Step 08...")
