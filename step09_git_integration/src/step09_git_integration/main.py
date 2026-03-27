#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step09_git_integration.crew import Step09GitIntegration

    print("=" * 60)
    print("  STEP 09 - GIT INTEGRATION")
    print("  Prepares PR and commit plan")
    print("=" * 60)

    required = {
        "00_project_idea.txt": "Step 01",
        "04_database.sql": "Step 04",
        "05_backend.md": "Step 05",
        "06_frontend.md": "Step 06",
        "08_evaluation.json": "Step 08",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    inputs = {
        'project_idea': (PIPELINE_DATA / "00_project_idea.txt").read_text(encoding="utf-8"),
        'evaluation_content': (PIPELINE_DATA / "08_evaluation.json").read_text(encoding="utf-8"),
        'backend_content': (PIPELINE_DATA / "05_backend.md").read_text(encoding="utf-8"),
        'frontend_content': (PIPELINE_DATA / "06_frontend.md").read_text(encoding="utf-8"),
        'database_content': (PIPELINE_DATA / "04_database.sql").read_text(encoding="utf-8"),
    }
    print("📄 Loaded all artifacts for Git integration plan")

    while True:
        print("\n🚀 Running Git integration planning...\n")
        result = Step09GitIntegration().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "09_pull_request.md"
        output_path.write_text(str(result), encoding="utf-8")
        print("\n" + "=" * 60)
        print("✅ Step 09 Complete!")
        print(f"   PR Plan: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 10, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 09 approved. Run step10_deployment next.")
            break
        print("\n🔄 Re-running Step 09...")
