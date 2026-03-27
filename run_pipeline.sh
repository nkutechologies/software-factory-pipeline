#!/bin/bash
# ============================================================
#  AI Software Factory Pipeline - Manual Step-by-Step Runner
# ============================================================
#  Run each step individually, review output, then proceed.
#
#  Usage:
#    ./run_pipeline.sh          # Start from Step 01
#    ./run_pipeline.sh 5        # Start from Step 05
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
START_STEP="${1:-1}"

STEPS=(
    "step01_requirements:Step 01 - Requirements Analysis"
    "step02_architecture:Step 02 - Architecture Design"
    "step03_planning:Step 03 - Task Planning"
    "step04_database:Step 04 - Database Engineering"
    "step05_backend:Step 05 - Backend Development"
    "step06_frontend:Step 06 - Frontend Development"
    "step07_qa:Step 07 - QA Engineering"
    "step08_evaluation:Step 08 - Code Evaluation"
    "step09_git_integration:Step 09 - Git Integration"
    "step10_deployment:Step 10 - Deployment"
)

echo "============================================================"
echo "  AI SOFTWARE FACTORY - MANUAL PIPELINE"
echo "============================================================"
echo "  Pipeline Data: $SCRIPT_DIR/pipeline_data/"
echo "  Starting from: Step $START_STEP"
echo "============================================================"
echo ""

for i in "${!STEPS[@]}"; do
    STEP_NUM=$((i + 1))
    if [ "$STEP_NUM" -lt "$START_STEP" ]; then
        continue
    fi

    IFS=':' read -r STEP_DIR STEP_NAME <<< "${STEPS[$i]}"

    echo ""
    echo "============================================================"
    echo "  $STEP_NAME"
    echo "============================================================"

    cd "$SCRIPT_DIR/$STEP_DIR"

    # Check if venv exists, if not install
    if [ ! -d ".venv" ]; then
        echo "📦 Installing dependencies for $STEP_DIR..."
        crewai install
    fi

    # Run the step
    crewai run

    echo ""
    echo "============================================================"
    if [ "$STEP_NUM" -lt 10 ]; then
        NEXT_STEP=$((STEP_NUM + 1))
        echo "  Ready for Step $NEXT_STEP"
        echo "  You can also re-run this step: cd $STEP_DIR && crewai run"
    else
        echo "  🎉 PIPELINE COMPLETE!"
    fi
    echo "============================================================"

    cd "$SCRIPT_DIR"
done

echo ""
echo "============================================================"
echo "  All pipeline outputs are in: $SCRIPT_DIR/pipeline_data/"
echo "============================================================"
