$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")

$files = Get-ChildItem -LiteralPath $root -Recurse -File -Force | Where-Object { $_.FullName -notmatch '\\.git(\\|$)' }
$dirs = Get-ChildItem -LiteralPath $root -Recurse -Directory -Force | Where-Object { $_.FullName -notmatch '\\.git(\\|$)' }

$requiredFiles = @(
    "AGENTS.md",
    "README.md",
    "RUNBOOK.md",
    "CURRENT_STATE.md",
    "NEXT_MISSION.md",
    "HANDOFF.md",
    "LICENSE",
    ".gitignore",
    ".github\workflows\validate-workspace.yml",
    "doctrine\CORE.md",
    "doctrine\MEMORY_HIERARCHY.md",
    "doctrine\INGESTION.md",
    "memory\INDEX.n3",
    "memory\FORMAT.n3.md",
    "templates\source.n1.md",
    "templates\note.n2.md",
    "templates\card.n3.md",
    "templates\mission.md",
    "sources\.gitkeep",
    "repos\.gitkeep",
    ".codex\skills\caveman-final-only\SKILL.md"
)

$allowedRootFiles = @(
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "RUNBOOK.md",
    "CURRENT_STATE.md",
    "NEXT_MISSION.md",
    "HANDOFF.md",
    "LICENSE"
)

$forbiddenPaths = @(
    ".agents",
    "skills",
    ("de" + "mos"),
    "_archive",
    "inbox",
    "experiments",
    (Join-Path "repos" "cloned"),
    (Join-Path "repos" "archived"),
    "themes",
    "logs"
)

$badNameTerms = @("k" + "ey", "se" + "cret", "to" + "ken", "cl" + [char]0x00E9)
$failures = [System.Collections.Generic.List[string]]::new()

function Join-WorkspacePath([string]$relativePath) {
    Join-Path $root $relativePath
}

if ($files.Count -ge 100) {
    $failures.Add("Too many files: $($files.Count)")
}

if ($dirs.Count -ge 25) {
    $failures.Add("Too many directories: $($dirs.Count)")
}

foreach ($file in $requiredFiles) {
    $path = Join-WorkspacePath $file
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        $failures.Add("Missing file: $file")
        continue
    }

    if ($file -notlike "*.gitkeep" -and [string]::IsNullOrWhiteSpace((Get-Content -LiteralPath $path -Raw))) {
        $failures.Add("Empty file: $file")
    }
}

$rootFiles = Get-ChildItem -LiteralPath $root -Force -File | Where-Object { $_.Name -notin $allowedRootFiles }
foreach ($file in $rootFiles) {
    $failures.Add("Unexpected root file: $($file.Name)")
}

foreach ($path in $forbiddenPaths) {
    if (Test-Path -LiteralPath (Join-WorkspacePath $path)) {
        $failures.Add("Forbidden legacy artifact exists: $path")
    }
}

$agents = Get-Content -LiteralPath (Join-WorkspacePath "AGENTS.md") -Raw
foreach ($needle in @("N3 -> N2 -> N1", "final-only", "agent minimalism", "source -> synthesis -> decision")) {
    if ($agents -notmatch [regex]::Escape($needle)) {
        $failures.Add("AGENTS.md missing doctrine: $needle")
    }
}

$index = Get-Content -LiteralPath (Join-WorkspacePath "memory\INDEX.n3") -Raw
foreach ($needle in @("ID=egx-ingestion-index", "TYPE=mission", "V=ACTIVE", "NEXT=add-card-at-memory/<source-id>.n3")) {
    if ($index -notmatch [regex]::Escape($needle)) {
        $failures.Add("Invalid N3 index: missing $needle")
    }
}

$format = Get-Content -LiteralPath (Join-WorkspacePath "memory\FORMAT.n3.md") -Raw
foreach ($needle in @("ID=<stable-id>", "TYPE=<source|theme|decision|risk|candidate|mission>", "N2=<path-or-none>", "N1=<path-or-none>")) {
    if ($format -notmatch [regex]::Escape($needle)) {
        $failures.Add("Invalid N3 format: missing $needle")
    }
}

$card = Get-Content -LiteralPath (Join-WorkspacePath "templates\card.n3.md") -Raw
foreach ($needle in @("ID=<stable-id>", "V=<KEEP|ADAPT|REJECT|WATCH|ACTIVE|BLOCKED>", "NEXT=<short-action>")) {
    if ($card -notmatch [regex]::Escape($needle)) {
        $failures.Add("Invalid N3 card template: missing $needle")
    }
}

$unexpectedRepoFiles = Get-ChildItem -LiteralPath (Join-WorkspacePath "repos") -Force -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne ".gitkeep" }
if ($unexpectedRepoFiles.Count -gt 0) {
    $failures.Add("Unexpected retained repo evidence")
}

$unexpectedSourceFiles = Get-ChildItem -LiteralPath (Join-WorkspacePath "sources") -Force -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne ".gitkeep" }
if ($unexpectedSourceFiles.Count -gt 0) {
    $failures.Add("Unexpected retained source notes")
}

foreach ($file in $files) {
    foreach ($term in $badNameTerms) {
        if ($file.Name.IndexOf($term, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
            $failures.Add("Suspicious filename: $($file.FullName.Substring($root.Path.Length + 1))")
        }
    }
}

$requiredDoctrine = Get-Content -LiteralPath (Join-WorkspacePath "doctrine\CORE.md") -Raw
foreach ($needle in @("CAVEMAN", "Token Saving", "Agent-First", "Minimalism")) {
    if ($requiredDoctrine -notmatch [regex]::Escape($needle)) {
        $failures.Add("CORE.md missing doctrine: $needle")
    }
}

$requiredMemory = Get-Content -LiteralPath (Join-WorkspacePath "doctrine\MEMORY_HIERARCHY.md") -Raw
foreach ($needle in @("N1 = full proof", "N2 = verifiable synthesis", "N3 = compact operational knowledge", "N3 -> N2 -> N1")) {
    if ($requiredMemory -notmatch [regex]::Escape($needle)) {
        $failures.Add("MEMORY_HIERARCHY.md missing doctrine: $needle")
    }
}

$requiredIngestion = Get-Content -LiteralPath (Join-WorkspacePath "doctrine\INGESTION.md") -Raw
foreach ($needle in @("one source", "N1 proof", "one N2 note", "one N3 card", "source -> synthesis -> decision")) {
    if ($requiredIngestion -notmatch [regex]::Escape($needle)) {
        $failures.Add("INGESTION.md missing doctrine: $needle")
    }
}

if ((Test-Path -LiteralPath (Join-WorkspacePath (Join-Path "repos" "cloned"))) -or (Test-Path -LiteralPath (Join-WorkspacePath (Join-Path "repos" "archived")))) {
    $failures.Add("Forbidden repo subdirectory exists")
}

if ($failures.Count -eq 0) {
    Write-Host "Status: OK"
    Write-Host "Files: $($files.Count)"
    Write-Host "Directories: $($dirs.Count)"
    exit 0
}

Write-Host "Status: FAILED"
foreach ($failure in $failures) {
    Write-Host "- $failure"
}
exit 1
