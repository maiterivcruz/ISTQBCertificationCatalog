"""Study-chapter content, keyed by certification id (see CERTIFICATIONS in views.py)."""
from importlib import import_module

_CERT_MODULES = {
    'ctfl': 'ctfl',
    'ctal-at': 'ctal_at',
    'ctal-ta': 'ctal_ta',
    'ctal-tae': 'ctal_tae',
    'ctal-tm': 'ctal_tm',
    'ctal-tta': 'ctal_tta',
    'ct-ai': 'ct_ai',
    'ct-qdo': 'ct_qdo',
    'ct-genai': 'ct_genai',
    'ct-mat': 'ct_mat',
    'ct-mbt': 'ct_mbt',
    'ct-tas': 'ct_tas',
    'ct-atlas': 'ct_atlas',
    'ct-act': 'ct_act',
    'ct-pt': 'ct_pt',
    'ct-sec': 'ct_sec',
    'ct-ste': 'ct_ste',
    'ct-ut': 'ct_ut',
    'ct-ft': 'ct_ft',
    'ct-aut': 'ct_aut',
    'ct-game': 'ct_game',
    'ct-gt': 'ct_gt',
    'ctel-itp-atp': 'ctel_itp_atp',
    'ctel-itp-itpi': 'ctel_itp_itpi',
    'ctel-tm-sm': 'ctel_tm_sm',
    'ctel-tm-otm': 'ctel_tm_otm',
    'ctel-tm-mtt': 'ctel_tm_mtt',
}

CHAPTERS_BY_CERT = {
    cert_id: import_module(f'.{module}', __package__).CHAPTERS
    for cert_id, module in _CERT_MODULES.items()
}


def get_chapters(cert_id):
    return CHAPTERS_BY_CERT.get(cert_id, [])


def get_chapter(cert_id, number):
    return next((c for c in get_chapters(cert_id) if c['number'] == number), None)
