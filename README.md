# AI Software Factory Pipeline
# Manual step-by-step execution: Idea → Working Deployed App

A multi-agent AI pipeline split into **10 independent CrewAI projects**. Each step runs separately so you can review, improve, and approve output before proceeding.

## Pipeline Flow

```
Step 01: Requirements → SRS Document (IEEE 830)
Step 02: Architecture → System Architecture Design
Step 03: Planning    → Task Breakdown (JSON)
Step 04: Database    → PostgreSQL Schemas
Step 05: Backend     → Node.js/Express API Code
Step 06: Frontend    → React UI Components
Step 07: QA          → Test Suites
Step 08: Evaluation  → Quality Score Report
Step 09: Git         → PR & Commit Plan
Step 10: Deployment  → Live Vercel Deployment
```

## Quick Start

### 1. Set up environment
```bash
# Copy .env to each step (or use the shared one)
cp .env.example step01_requirements/.env
# ... repeat for each step, or run:
for d in step*/; do cp .env.example "$d/.env"; done
```

### 2. Run step-by-step
```bash
# Option A: Use the master script
chmod +x run_pipeline.sh
./run_pipeline.sh

# Option B: Run each step manually
cd step01_requirements
crewai install
crewai run
# Review pipeline_data/01_srs.md
# If good, proceed to step 02

cd ../step02_architecture
crewai install
crewai run
# Review pipeline_data/02_architecture.md
# ...continue for each step
```

### 3. Resume from a specific step
```bash
./run_pipeline.sh 5   # Start from Step 05
```

## Shared Data

All steps read/write to `pipeline_data/`:

| File | Step | Description |
|------|------|-------------|
| `00_project_idea.txt` | 01 | Original project idea |
| `01_srs.md` / `.docx` | 01 | SRS Document |
| `02_architecture.md` | 02 | Architecture Design |
| `03_task_plan.json` | 03 | Task Breakdown |
| `04_database.sql` | 04 | Database Schemas |
| `05_backend.md` | 05 | Backend API Code |
| `06_frontend.md` | 06 | Frontend Components |
| `07_tests.md` | 07 | Test Suites |
| `08_evaluation.json` | 08 | Quality Scores |
| `09_pull_request.md` | 09 | PR Description |
| `10_deployment.md` | 10 | Deployment Report |

## Requirements

- Python 3.10-3.13
- [uv](https://docs.astral.sh/uv/) package manager
- [CrewAI CLI](https://docs.crewai.com/) v1.11+
- OpenAI API key
- Vercel token (for Step 10)
