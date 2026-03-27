#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step02_architecture.crew import Step02Architecture

    print("=" * 60)
    print("  STEP 02 - ARCHITECTURE DESIGN")
    print("  Generates system architecture from SRS")
    print("=" * 60)

    srs_path = PIPELINE_DATA / "01_srs.md"
    if not srs_path.exists():
        print(f"❌ Required input not found: {srs_path}")
        print("   Please run Step 01 first.")
        sys.exit(1)

    srs_content = srs_path.read_text(encoding="utf-8")
    print(f"📄 Loaded SRS from: {srs_path}")

    inputs = {'srs_content': srs_content}

    while True:
        print("\n🚀 Running architecture design...\n")
        result = Step02Architecture().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "02_architecture.md"
        output_path.write_text(str(result), encoding="utf-8")
        print("\n" + "=" * 60)
        print("✅ Step 02 Complete!")
        print(f"   Architecture: {output_path}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to proceed to Step 03, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Step 02 approved. Run step03_planning next.")
            break
        print("\n🔄 Re-running Step 02...")
