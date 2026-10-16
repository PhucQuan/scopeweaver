@echo off
chcp 65001 >nul 2>&1
rem Run ScopeWeaver standalone with Qwen LLM API and dedicated PostgreSQL

echo ===================================================
echo   Starting ScopeWeaver (Autonomous AI Pentest System)
echo ===================================================

cd /d "%~dp0"

rem 1. Check & start dedicated PostgreSQL container (port 5433, isolated from VEASM/others)
echo [*] Checking ScopeWeaver database container...
docker start scopeweaver-postgres-1 >nul 2>&1
if errorlevel 1 (
    docker compose up -d postgres
)

rem 2. Configure environment variables for ScopeWeaver
set "SCOPEWEAVER_LANGUAGE=en"
set "ARTEX_PG_DSN=postgres://artex:scopeweaver_secret_2026@127.0.0.1:5433/artex?sslmode=disable"
set "OPENAI_API_KEY=sk-adjadni1429y8y81h4ufq9n"
set "ARTEX_LLM_PROVIDER=openai"
set "ARTEX_LLM_MODEL=Qwen/Qwen3.6-35B-A3B-FP8"
set "ARTEX_LLM_BASE_URL=http://117.1.29.208:8236/v1"
set "ARTEX_LLM_STREAM=false"
set "ARTEX_LLM_PROXY="

rem 3. Launch ScopeWeaver
echo [*] Starting ScopeWeaver on http://localhost:8787 ...
call start.bat -addr :8787 -proxy 127.0.0.1:8788 %*
