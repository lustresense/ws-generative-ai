"""Automated terminal executor and window cropper for Tugas 2.
Takes screenshot of active terminal window after each section,
saving directly to module-XX/output/.
"""
from __future__ import annotations
import os
import subprocess
import sys
import time
from pathlib import Path
from PIL import Image, ImageGrab
import pygetwindow as gw

ROOT = Path(__file__).resolve().parent

SECTIONS = [
    {
        "module": 6,
        "name": "6.1 - 6.3",
        "output": ROOT / "module-06" / "output" / "6.1 - 6.3.png",
        "dir": ROOT / "module-06" / "src",
        "scripts": [
            ("6_1_print_env_config.py", []),
            ("6_2a_anthropic_basic_message.py", []),
            ("6_2b_anthropic_system_prompt.py", []),
            ("6_2c_anthropic_multiturn.py", ["--demo"]),
            ("6_2d_anthropic_streaming.py", []),
            ("6_3a_openai_basic_message.py", []),
            ("6_3b_openai_streaming.py", []),
        ],
    },
    {
        "module": 6,
        "name": "6.4 - 6.7",
        "output": ROOT / "module-06" / "output" / "6.4 - 6.7.png",
        "dir": ROOT / "module-06" / "src",
        "scripts": [
            ("6_4a_anthropic_tool_calling.py", []),
            ("6_4b_openai_tool_calling.py", []),
            ("6_5_vision_inputs.py", []),
            ("6_6_token_management.py", []),
            ("6_7_provider_agnostic_client.py", []),
        ],
    },
    {
        "module": 6,
        "name": "6.8 Exercise",
        "output": ROOT / "module-06" / "output" / "exercise.png",
        "dir": ROOT / "module-06" / "src",
        "scripts": [
            ("6_8_exercise_01.py", []),
            ("6_8_exercise_02.py", []),
            ("6_8_exercise_03.py", []),
            ("6_8_exercise_04.py", []),
        ],
    },
    {
        "module": 7,
        "name": "7.2 - 7.5",
        "output": ROOT / "module-07" / "output" / "7.2 - 7.5.png",
        "dir": ROOT / "module-07" / "src",
        "scripts": [
            ("7_2_system_prompts.py", []),
            ("7_3_few_shot_prompting.py", []),
            ("7_4a_chain_of_thought.py", []),
            ("7_4b_structured_cot_xml.py", []),
            ("7_5a_prompt_enforced_json.py", []),
            ("7_5b_openai_json_mode.py", []),
        ],
    },
    {
        "module": 7,
        "name": "7.6 - 7.7",
        "output": ROOT / "module-07" / "output" / "7.6 - 7.7.png",
        "dir": ROOT / "module-07" / "src",
        "scripts": [
            ("7_6_prompt_template.py", []),
            ("7_7_prompt_evaluation.py", []),
        ],
    },
    {
        "module": 7,
        "name": "7.8 Exercise",
        "output": ROOT / "module-07" / "output" / "exercise.png",
        "dir": ROOT / "module-07" / "src",
        "scripts": [
            ("7_8_exercise_01.py", []),
            ("7_8_exercise_02.py", []),
            ("7_8_exercise_03.py", []),
            ("7_8_exercise_04.py", []),
        ],
    },
    {
        "module": 8,
        "name": "8.2 - 8.4",
        "output": ROOT / "module-08" / "output" / "8.2 - 8.4.png",
        "dir": ROOT / "module-08" / "src",
        "scripts": [
            ("8_2a_openai_embeddings.py", []),
            ("8_2b_voyage_embeddings.py", []),
            ("8_3_cosine_similarity.py", []),
            ("8_4_semantic_search_vector_store.py", []),
        ],
    },
    {
        "module": 8,
        "name": "8.5 - 8.7",
        "output": ROOT / "module-08" / "output" / "8.5 - 8.7.png",
        "dir": ROOT / "module-08" / "src",
        "scripts": [
            ("8_5_sentence_chunking.py", []),
            ("8_6_retrieval_evaluation.py", []),
            ("8_7_metadata_filtering.py", []),
        ],
    },
    {
        "module": 8,
        "name": "8.8 Exercise",
        "output": ROOT / "module-08" / "output" / "exercise.png",
        "dir": ROOT / "module-08" / "src",
        "scripts": [
            ("8_8_exercise_01.py", []),
            ("8_8_exercise_02.py", []),
            ("8_8_exercise_03.py", []),
            ("8_8_exercise_04.py", []),
        ],
    },
]


def capture_active_window(target_path: Path):
    target_path.parent.mkdir(parents=True, exist_ok=True)
    time.sleep(0.5)
    win = gw.getActiveWindow()
    if win:
        bbox = (win.left, win.top, win.right, win.bottom)
        img = ImageGrab.grab(bbox=bbox)
    else:
        img = ImageGrab.grab()
    img.save(target_path)
    print(f"[SCREENSHOT SAVED] -> {target_path.relative_to(ROOT)} ({img.width}x{img.height})")


def run():
    py_exe = sys.executable
    print("Mulai eksekusi otomatis + screenshot...\n")

    for s_idx, sec in enumerate(SECTIONS, start=1):
        work_dir = sec["dir"]
        print(f"\n# ============================================================")
        print(f"# BAGIAN [{s_idx}/{len(SECTIONS)}]: {sec['name']}")
        print(f"# ============================================================\n")

        for script_name, args in sec["scripts"]:
            cmd_display = f"python .\\{script_name}" + (" " + " ".join(args) if args else "")
            print(f"(.venv) PS {work_dir}> {cmd_display}", flush=True)

            script_path = work_dir / script_name
            full_cmd = [py_exe, str(script_path)] + args
            subprocess.run(full_cmd, cwd=work_dir)
            print()

        capture_active_window(sec["output"])

    print("\nSemua 9 bagian selesai dan screenshot sudah tersimpan rapi.")


if __name__ == "__main__":
    run()
