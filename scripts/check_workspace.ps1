$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")

$requiredFiles = @(
    "AGENTS.md",
    "README.md",
    "RUNBOOK.md",
    "CURRENT_STATE.md",
    "NEXT_MISSION.md",
    "INGESTION_PROTOCOL.md",
    "THEME_MAP.md",
    "DECISIONS.md",
    "PRODUCTION_CANDIDATES.md",
    "RISK_REGISTER.md",
    "SOURCE_INDEX.md",
    "EXPERIMENT_LOG.md",
    "HANDOFF.md",
    "QUALITY_AUDIT.md",
    "PATCH_PLAN.md"
)

$requiredDirs = @(
    "inbox",
    "themes",
    "themes\_template_theme",
    "sources",
    "repos",
    "repos\cloned",
    "repos\archived",
    "experiments",
    "experiments\runs",
    "templates",
    "skills",
    "skills\source-ingestion",
    "skills\repo-lab-test",
    "skills\transversal-synthesis",
    ".agents\skills",
    ".agents\skills\source-ingestion",
    ".agents\skills\repo-lab-test",
    ".agents\skills\transversal-synthesis",
    "scripts",
    "logs",
    "_archive"
)

$requiredTemplates = @(
    "templates\source-note-template.md",
    "templates\theme-note-template.md",
    "templates\experiment-template.md",
    "templates\production-candidate-template.md",
    "templates\handoff-template.md",
    "templates\ingestion-report-template.md"
)

$requiredSkills = @(
    ".agents\skills\source-ingestion\SKILL.md",
    ".agents\skills\repo-lab-test\SKILL.md",
    ".agents\skills\transversal-synthesis\SKILL.md",
    "skills\source-ingestion\SKILL.md",
    "skills\repo-lab-test\SKILL.md",
    "skills\transversal-synthesis\SKILL.md"
)

$requiredThemeTemplateFiles = @(
    "themes\_template_theme\README.md",
    "themes\_template_theme\sources.md",
    "themes\_template_theme\patterns.md",
    "themes\_template_theme\decisions.md",
    "themes\_template_theme\experiments.md",
    "themes\_template_theme\production_implications.md",
    "themes\_template_theme\cross_links.md"
)

$failures = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]

function Get-WorkspacePath {
    param([string]$RelativePath)
    return Join-Path $root $RelativePath
}

function Test-NonEmptyFile {
    param([string]$RelativePath)

    $path = Get-WorkspacePath -RelativePath $RelativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        return $false
    }

    $content = Get-Content -LiteralPath $path -Raw
    return -not [string]::IsNullOrWhiteSpace($content)
}

function Write-Check {
    param(
        [string]$Status,
        [string]$Item,
        [string]$Detail = ""
    )

    if ([string]::IsNullOrWhiteSpace($Detail)) {
        Write-Host "[$Status] $Item"
    }
    else {
        Write-Host "[$Status] $Item - $Detail"
    }
}

function Check-Files {
    param(
        [string]$Title,
        [string[]]$Items,
        [switch]$RequireNonEmpty
    )

    Write-Host ""
    Write-Host "== $Title =="

    foreach ($item in $Items) {
        $path = Get-WorkspacePath -RelativePath $item
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            Write-Check -Status "MISSING" -Item $item
            $failures.Add("Missing file: $item")
            continue
        }

        if ($RequireNonEmpty -and -not (Test-NonEmptyFile -RelativePath $item)) {
            Write-Check -Status "EMPTY" -Item $item
            $failures.Add("Empty file: $item")
            continue
        }

        $bytes = (Get-Item -LiteralPath $path).Length
        Write-Check -Status "OK" -Item $item -Detail "$bytes bytes"
    }
}

function Check-Directories {
    param(
        [string]$Title,
        [string[]]$Items
    )

    Write-Host ""
    Write-Host "== $Title =="

    foreach ($item in $Items) {
        $path = Get-WorkspacePath -RelativePath $item
        if (Test-Path -LiteralPath $path -PathType Container) {
            Write-Check -Status "OK" -Item $item
        }
        else {
            Write-Check -Status "MISSING" -Item $item
            $failures.Add("Missing directory: $item")
        }
    }
}

function Check-SkillFrontmatter {
    param([string[]]$Items)

    Write-Host ""
    Write-Host "== Skill frontmatter =="

    foreach ($item in $Items) {
        if (-not (Test-NonEmptyFile -RelativePath $item)) {
            Write-Check -Status "INVALID" -Item $item -Detail "missing or empty"
            $failures.Add("Invalid skill file: $item")
            continue
        }

        $content = Get-Content -LiteralPath (Get-WorkspacePath -RelativePath $item) -Raw
        $hasFrontmatter = $content -match "(?s)^---\s*\r?\n(.*?)\r?\n---"
        if (-not $hasFrontmatter) {
            Write-Check -Status "INVALID" -Item $item -Detail "missing YAML frontmatter"
            $failures.Add("Skill missing frontmatter: $item")
            continue
        }

        $frontmatter = $Matches[1]
        $hasName = $frontmatter -match "(?m)^name:\s*.+$"
        $hasDescription = $frontmatter -match "(?m)^description:\s*.+$"

        if ($hasName -and $hasDescription) {
            Write-Check -Status "OK" -Item $item
        }
        else {
            Write-Check -Status "INVALID" -Item $item -Detail "requires name and description"
            $failures.Add("Skill missing name or description: $item")
        }
    }
}

function Check-SkillLocations {
    Write-Host ""
    Write-Host "== Skill location decision =="

    if (Test-Path -LiteralPath (Get-WorkspacePath -RelativePath ".agents\skills") -PathType Container) {
        Write-Check -Status "OK" -Item ".agents\skills" -Detail "active repo skill location"
    }
    else {
        Write-Check -Status "MISSING" -Item ".agents\skills"
        $failures.Add("Missing active skill location: .agents\skills")
    }

    if (Test-Path -LiteralPath (Get-WorkspacePath -RelativePath "skills") -PathType Container) {
        Write-Check -Status "OK" -Item "skills" -Detail "documentary mirror"
    }
    else {
        Write-Check -Status "MISSING" -Item "skills"
        $failures.Add("Missing documentary skill mirror: skills")
    }
}

Write-Host "EGX_Ingestion workspace check"
Write-Host "Root: $root"

Check-Files -Title "Root files" -Items $requiredFiles -RequireNonEmpty
Check-Directories -Title "Directories" -Items $requiredDirs
Check-Files -Title "Templates" -Items $requiredTemplates -RequireNonEmpty
Check-Files -Title "Theme template files" -Items $requiredThemeTemplateFiles -RequireNonEmpty
Check-Files -Title "Skill files" -Items $requiredSkills -RequireNonEmpty
Check-SkillFrontmatter -Items $requiredSkills
Check-SkillLocations

Write-Host ""
Write-Host "== Summary =="
if ($warnings.Count -gt 0) {
    Write-Host "Warnings: $($warnings.Count)"
    foreach ($warning in $warnings) {
        Write-Host "- $warning"
    }
}

if ($failures.Count -eq 0) {
    Write-Host "Status: OK"
    Write-Host "Required files, non-empty content, templates, skills and frontmatter are valid."
    exit 0
}

Write-Host "Status: FAILED"
Write-Host "Failures: $($failures.Count)"
foreach ($failure in $failures) {
    Write-Host "- $failure"
}
exit 1
