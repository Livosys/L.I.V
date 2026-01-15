from fpdf import FPDF
import json
from pathlib import Path


def generate_pdf(metrics: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "SHIX Enterprise RAG Evaluation", ln=True)

    for k, v in metrics.items():
        pdf.cell(0, 10, f"{k}: {v}", ln=True)

    Path("eval").mkdir(exist_ok=True)
    pdf.output("eval/shix_ragas_report.pdf")
