from __future__ import annotations
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent

SOURCES = {
    6: [
        "6_1_print_env_config.py",
        "6_2a_anthropic_basic_message.py",
        "6_2b_anthropic_system_prompt.py",
        "6_2c_anthropic_multiturn.py",
        "6_2d_anthropic_streaming.py",
        "6_3a_openai_basic_message.py",
        "6_3b_openai_streaming.py",
        "6_4a_anthropic_tool_calling.py",
        "6_4b_openai_tool_calling.py",
        "6_5_vision_inputs.py",
        "6_6_token_management.py",
        "6_7_provider_agnostic_client.py",
        "6_8_exercise_01.py",
        "6_8_exercise_02.py",
        "6_8_exercise_03.py",
        "6_8_exercise_04.py",
    ],
    7: [
        "7_2_system_prompts.py",
        "7_3_few_shot_prompting.py",
        "7_4a_chain_of_thought.py",
        "7_4b_structured_cot_xml.py",
        "7_5a_prompt_enforced_json.py",
        "7_5b_openai_json_mode.py",
        "7_6_prompt_template.py",
        "7_7_prompt_evaluation.py",
        "7_8_exercise_01.py",
        "7_8_exercise_02.py",
        "7_8_exercise_03.py",
        "7_8_exercise_04.py",
    ],
    8: [
        "8_2a_openai_embeddings.py",
        "8_2b_voyage_embeddings.py",
        "8_3_cosine_similarity.py",
        "8_4_semantic_search_vector_store.py",
        "8_5_sentence_chunking.py",
        "8_6_retrieval_evaluation.py",
        "8_7_metadata_filtering.py",
        "8_8_exercise_01.py",
        "8_8_exercise_02.py",
        "8_8_exercise_03.py",
        "8_8_exercise_04.py",
    ],
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def screenshot_dirs() -> list[Path]:
    home = Path.home()
    candidates = [
        home / "Pictures" / "Screenshots",
        home / "OneDrive" / "Pictures" / "Screenshots",
    ]
    onedrive = os.getenv("OneDrive")
    if onedrive:
        candidates.append(Path(onedrive) / "Pictures" / "Screenshots")
    # Keep order but remove duplicates.
    out = []
    for p in candidates:
        if p not in out:
            out.append(p)
    return out

def import_latest_screenshot(started_at: float, target: Path) -> bool:
    matches = []
    for folder in screenshot_dirs():
        if not folder.exists():
            continue
        for path in folder.glob("*.png"):
            try:
                if path.stat().st_mtime >= started_at - 2:
                    matches.append(path)
            except OSError:
                pass
    if not matches:
        return False
    newest = max(matches, key=lambda p: p.stat().st_mtime)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(newest, target)
    return True

def run_one(module: int, filename: str, index: int, total: int, pause: bool, screenshot_import: bool) -> bool:
    src = ROOT / f"module-{module:02d}" / "src" / filename
    output = ROOT / f"module-{module:02d}" / "output" / (src.stem + ".png")
    clear_screen()
    print("=" * 76)
    print(f"[{index:02d}/{total:02d}] MODULE {module:02d} | {filename}")
    print("=" * 76)
    cmd = [sys.executable, str(src)]
    if filename == "6_2c_anthropic_multiturn.py":
        cmd.append("--demo")
    print("RUN:", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    print("-" * 76, flush=True)
    result = subprocess.run(cmd, cwd=src.parent)
    print("-" * 76)
    status = "SUCCESS" if result.returncode == 0 else f"FAILED (exit={result.returncode})"
    print("STATUS:", status)
    print("SCREENSHOT TARGET:", output.relative_to(ROOT))

    if not pause:
        return result.returncode == 0

    started = time.time()
    print("\nSCREENSHOT NOW: Win + Shift + S -> crop terminal -> wait autosave -> Enter")
    input()
    if screenshot_import:
        if import_latest_screenshot(started, output):
            print("[OK] Screenshot copied/renamed to:", output.relative_to(ROOT))
        else:
            print("[WARN] Screenshot autosave tidak ditemukan. Simpan/pindahkan manual ke target di atas.")
            time.sleep(1.2)
    return result.returncode == 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", type=int, choices=[6,7,8])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--no-pause", action="store_true")
    parser.add_argument("--no-screenshot-import", action="store_true")
    args = parser.parse_args()

    modules = [args.module] if args.module else [6,7,8]
    jobs = [(m, f) for m in modules for f in SOURCES[m]]
    total = len(jobs)
    print(f"Preparing to run {total} source(s).")
    if not args.no_pause:
        print("Runner will pause after each source for screenshot capture.")
        input("Press Enter to start...")

    for idx, (module, filename) in enumerate(jobs, start=1):
        ok = run_one(module, filename, idx, total, not args.no_pause, not args.no_screenshot_import)
        if not ok:
            print("\nExecution stopped on failure so the error can be fixed before continuing.")
            sys.exit(1)

    clear_screen()
    print("=" * 76)
    print(f"DONE — {total}/{total} source(s) completed successfully.")
    print("Check module-06/output, module-07/output, and module-08/output.")
    print("=" * 76)

if __name__ == "__main__":
    main()
