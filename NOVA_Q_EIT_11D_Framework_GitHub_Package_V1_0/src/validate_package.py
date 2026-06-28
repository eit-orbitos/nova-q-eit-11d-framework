from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
required=["README.md","paper/NOVA_Q_EIT_11D_Framework_V1_0.md","paper/REFERENCES_V1_1.md","framework/article_7_safety_boundary.json","src/nova_q_eit_framework.py"]
missing=[p for p in required if not (root/p).exists()]
if missing:
    print("Missing:", missing); raise SystemExit(1)
article=json.loads((root/"framework/article_7_safety_boundary.json").read_text())
assert article["active"] is True
print("Package validation passed. Article 7 active.")
