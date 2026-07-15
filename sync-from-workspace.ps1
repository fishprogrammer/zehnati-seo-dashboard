# Sync local dashboard + audit artifacts into this GitHub Pages repo
$ErrorActionPreference = "Stop"
$SrcDash = "D:\claude-seo\SEO\dashboard"
$SrcAudit = "D:\claude-seo\claude-seo\zehnati.ir-audit"
$Dest = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Sync -> $Dest"

Copy-Item "$SrcDash\index.html", "$SrcDash\data.js", "$SrcDash\audit.js" -Destination $Dest -Force

$auditDest = Join-Path $Dest "audit"
$findDest = Join-Path $auditDest "findings"
New-Item -ItemType Directory -Force -Path $findDest | Out-Null

foreach ($f in @("audit-data.json", "FULL-AUDIT-REPORT.md", "ACTION-PLAN.md")) {
  $p = Join-Path $SrcAudit $f
  if (Test-Path $p) { Copy-Item $p -Destination $auditDest -Force }
}

Get-ChildItem (Join-Path $SrcAudit "findings") -File -ErrorAction SilentlyContinue |
  Where-Object { $_.Extension -in ".md", ".json" -and $_.Name -notlike "_*" } |
  ForEach-Object { Copy-Item $_.FullName -Destination $findDest -Force }

# rebuild status.json for static audit cards
$py = Join-Path $env:LOCALAPPDATA "Programs\Python\Python312\python.exe"
if (-not (Test-Path $py)) { $py = "python" }
& $py -c @"
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
root = Path(r'$($Dest.Replace('\','\\'))')
names = [p.name for p in sorted((root/'audit').glob('*')) if p.is_file()]
names += [p.name for p in sorted((root/'audit'/'findings').glob('*')) if p.is_file()]
score = None
ap = root/'audit'/'audit-data.json'
if ap.exists():
    score = (json.loads(ap.read_text(encoding='utf-8')).get('summary') or {}).get('health_score')
status = {
  'ok': True,
  'mode': 'static',
  'generated_at': datetime.now(timezone(timedelta(hours=3, minutes=30))).isoformat(timespec='seconds'),
  'findings': names,
  'summary': {'health_score': score} if score is not None else None,
}
(root/'audit'/'status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding='utf-8')
print('status.json ok,', len(names), 'files, score=', score)
"@

Write-Host "Done. Next: git add -A && git commit && git push"
