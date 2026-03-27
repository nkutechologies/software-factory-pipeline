#!/usr/bin/env python
import sys
import re
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

PIPELINE_DATA = Path(__file__).resolve().parent.parent.parent.parent / "pipeline_data"


def run():
    from step10_deployment.crew import Step10Deployment

    print("=" * 60)
    print("  STEP 10 - DEPLOYMENT")
    print("  Deploys application to Vercel")
    print("=" * 60)

    required = {
        "05_backend.md": "Step 05",
        "06_frontend.md": "Step 06",
    }
    for fname, step in required.items():
        if not (PIPELINE_DATA / fname).exists():
            print(f"❌ Required input not found: {fname}")
            print(f"   Please run {step} first.")
            sys.exit(1)

    inputs = {
        'backend_content': (PIPELINE_DATA / "05_backend.md").read_text(encoding="utf-8"),
        'frontend_content': (PIPELINE_DATA / "06_frontend.md").read_text(encoding="utf-8"),
    }
    print("📄 Loaded backend and frontend code for deployment")

    while True:
        print("\n🚀 Running deployment...\n")
        result = Step10Deployment().crew().kickoff(inputs=inputs)

        output_path = PIPELINE_DATA / "10_deployment.md"

        # Extract deployed URL
        raw_output = str(result)
        deployed_url = None
        for line in raw_output.split('\n'):
            if 'DEPLOYED_URL:' in line:
                deployed_url = line.split('DEPLOYED_URL:')[-1].strip()
                break
            elif 'vercel.app' in line:
                urls = re.findall(r'https://[\w.-]+\.vercel\.app[\w/.-]*', line)
                if urls:
                    deployed_url = urls[0]
                    break

        print("\n" + "=" * 60)
        print("✅ Step 10 Complete!")
        print(f"   Deployment Report: {output_path}")
        if deployed_url:
            print(f"\n🌐 DEPLOYED URL: {deployed_url}")
        print("=" * 60)

        print("\n" + "=" * 60)
        print("🎉 PIPELINE COMPLETE!")
        print("=" * 60)
        print("All 10 steps have been executed.")
        print(f"All outputs saved in: {PIPELINE_DATA}")
        if deployed_url:
            print(f"Live app: {deployed_url}")
        print("=" * 60)

        choice = input("\n🔍 Review the output. Press Enter to finish, or 'r' to re-run: ").strip().lower()
        if choice != 'r':
            print("\n✅ Pipeline complete! All steps approved.")
            break
        print("\n🔄 Re-running Step 10...")
