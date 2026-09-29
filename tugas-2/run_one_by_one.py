"""Runner for Tugas 2 with clean, authentic terminal appearance.
Simulates natural PowerShell prompt:
  (.venv) PS E:\College\Sem 7 - Gen AI\tugas-2\module-XX\src> python .\script.py
Groups scripts by section, allowing easy screenshots per section.
"""
from __future__ import annotations
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SECTIONS = [
    # Module 06
    {
        "module": 6,
        "title": "MODULE 06 (6.1 - 6.3: Basic & Streaming)",
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
        "title": "MODULE 06 (6.4 - 6.7: Tools, Vision, Token, Client)",
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
        "title": "MODULE 06 (6.8: Exercises 01 - 04)",
        "dir": ROOT / "module-06" / "src",
        "scripts": [
            ("6_8_exercise_01.py", []),
            ("6_8_exercise_02.py", []),
            ("6_8_exercise_03.py", []),
            ("6_8_exercise_04.py", []),
        ],
    },
    # Module 07
    {
        "module": 7,
        "title": "MODULE 07 (7.2 - 7.5: Prompts, Few-shot, CoT, JSON)",
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
        "title": "MODULE 07 (7.6 - 7.7: Templates & Evaluation)",
        "dir": ROOT / "module-07" / "src",
        "scripts": [
            ("7_6_prompt_template.py", []),
            ("7_7_prompt_evaluation.py", []),
        ],
    },
    {
        "module": 7,
        "title": "MODULE 07 (7.8: Exercises 01 - 04)",
        "dir": ROOT / "module-07" / "src",
        "scripts": [
            ("7_8_exercise_01.py", []),
            ("7_8_exercise_02.py", []),
            ("7_8_exercise_03.py", []),
            ("7_8_exercise_04.py", []),
        ],
    },
    # Module 08
    {
        "module": 8,
        "title": "MODULE 08 (8.2 - 8.4: Embeddings & Similarity)",
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
        "title": "MODULE 08 (8.5 - 8.7: Chunking, Retrieval & Filtering)",
        "dir": ROOT / "module-08" / "src",
        "scripts": [
            ("8_5_sentence_chunking.py", []),
            ("8_6_retrieval_evaluation.py", []),
            ("8_7_metadata_filtering.py", []),
        ],
    },
    {
        "module": 8,
        "title": "MODULE 08 (8.8: Exercises 01 - 04)",
        "dir": ROOT / "module-08" / "src",
        "scripts": [
            ("8_8_exercise_01.py", []),
            ("8_8_exercise_02.py", []),
            ("8_8_exercise_03.py", []),
            ("8_8_exercise_04.py", []),
        ],
    },
]


def run():
    py_exe = sys.executable
    total_sections = len(SECTIONS)

    for s_idx, sec in enumerate(SECTIONS, start=1):
        work_dir = sec["dir"]
        print(f"\n# ============================================================")
        print(f"# SECTION [{s_idx}/{total_sections}]: {sec['title']}")
        print(f"# ============================================================\n")

        for script_name, args in sec["scripts"]:
            cmd_display = f"python .\\{script_name}" + (" " + " ".join(args) if args else "")
            prompt_line = f"(.venv) PS {work_dir}> {cmd_display}"
            print(prompt_line, flush=True)

            script_path = work_dir / script_name
            full_cmd = [py_exe, str(script_path)] + args

            proc = subprocess.run(full_cmd, cwd=work_dir)
            if proc.returncode != 0:
                print(f"[!] Warning: {script_name} exited with code {proc.returncode}\n")
            print()

        if s_idx < total_sections:
            print("------------------------------------------------------------")
            print(f">> Bagian {s_idx} selesai. Silakan screenshot terminal sekarang (Win + Shift + S).")
            print(">> Tekan [ENTER] jika sudah siap lanjut ke bagian berikutnya...")
            print("------------------------------------------------------------", flush=True)
            try:
                input()
            except (KeyboardInterrupt, EOFError):
                print("\nDihentikan pengguna.")
                return

    print("============================================================")
    print("Semua bagian (Module 06, 07, 08) sudah selesai dijalankan!")
    print("============================================================")


if __name__ == "__main__":
    run()
