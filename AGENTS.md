# Agent instructions
## Workspace organization safeguards

- Treat this directory as one independent Git checkout. A shared origin does not make another local checkout disposable.
- Before consolidating, moving, renaming, archiving, or deleting any checkout, inspect its branch, upstream, worktree status, and untracked files; get explicit approval before destructive changes.
- Preserve pre-existing edits and untracked `_arsiv/` content. Never use `git clean`, reset, or broad deletion to tidy the workspace.
- Stage and commit only the files intended for the current change; do not include unrelated pre-existing changes.
- When working in the local `C:\Users\pc\github` workspace, consult its `PROJECT-ORGANIZATION.md` inventory and refresh status before relying on it.
