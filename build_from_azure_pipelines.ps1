param(
    [string]$docfx,
    [string]$remote,
    [switch]$debug
)

if ($debug -eq $true) {
    #$git_bin = "C:\Program Files\Git\usr\bin"
    $working_directory = Get-Location | Out-String
    Write-Host "cwd is $working_directory"
    Write-Host "user is $env:USERNAME"

    if (test-path "$home\.ssh\id_rsa.pub") {
        Write-Host "Has public key:"
        Get-Content "$home\.ssh\id_rsa.pub"
    }
    else {
        Write-Host "Doesn't have SSH public key!!"
    }
}


Write-Host "Setting up git remote ssh..."

git config remote.ssh.url
if ($lastexitcode -eq 1) {
    git remote add ssh $remote
}

# Silently abort any in-progress rebase (no-op if there isn’t one)
try
{
    git rebase --abort 2>$null
} catch
{
    # Write-Host "Caught: no rebase was in progress. Moving on..."
}

Write-Host "Getting Latest Changes"
git checkout master
git pull --rebase

Write-Host "Building docfx"
Invoke-Expression "$docfx build"

Write-Host "Upload Changes to Github"
git add -A
$now = [System.DateTime]::Now.ToShortTimeString();
git commit -m "Latest changes from buid bot: $now"
git push ssh master
