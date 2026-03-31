---
name: "dev-browser"
description: "Use when the task requires automating a real browser from the terminal (navigation, form filling, screenshots, data extraction, UI-flow debugging) with `dev-browser`."
---

# Dev Browser

Drive a real browser from the terminal using `dev-browser`, a sandboxed browser automation CLI with persistent page state.
Treat this skill as CLI-first automation. Do not pivot to test-file scaffolding unless the user explicitly asks for it.

## Prerequisite check (required)

Before proposing commands, check whether `dev-browser` is already available:

```bash
command -v dev-browser >/dev/null 2>&1
```

If it is not available, check whether `pnpm` or `npx` is present:

```bash
command -v pnpm >/dev/null 2>&1 || command -v npx >/dev/null 2>&1
```

If neither is available, pause and ask the user to install Node.js plus a package runner before continuing.

## Install or run

Prefer a global install when repeated browser work is likely:

```bash
pnpm add -g dev-browser
dev-browser install
dev-browser --help
```

If the user does not want a global install, run it through the package runner that is already available:

```bash
pnpm dlx dev-browser --help
# or
npx --yes dev-browser --help
```

After installation, run `dev-browser install` once so the browser runtime is ready.

## Core workflow

1. Start `dev-browser` and send it a small JavaScript script through stdin.
2. Reuse named pages with `browser.getPage("name")` so page state persists across runs.
3. Interact with the page, inspect the result, and print only the data you actually need.
4. Save screenshots or temporary files only when they help the task.
5. Re-run with a tighter script instead of growing one giant script.

## Quick start

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("main");
await page.goto("https://example.com");
console.log(await page.title());
EOF
```

Connect to an existing Chrome session:

```bash
dev-browser --connect <<'EOF'
const tabs = await browser.listPages();
console.log(JSON.stringify(tabs, null, 2));
EOF
```

## Recommended patterns

### Fill a form

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("signup");
await page.goto("https://example.com/signup");
await page.getByLabel("Email").fill("user@example.com");
await page.getByLabel("Password").fill("password123");
await page.getByRole("button", { name: "Create account" }).click();
console.log(await page.title());
EOF
```

### Capture a screenshot

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("homepage");
await page.goto("https://example.com");
const screenshot = await page.screenshot({ fullPage: true });
console.log(await saveScreenshot(screenshot, "homepage.png"));
EOF
```

### Extract page data

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("docs");
await page.goto("https://example.com/docs");
const heading = await page.locator("h1").first().textContent();
console.log(JSON.stringify({ heading }, null, 2));
EOF
```

### Request an AI-friendly page snapshot

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("checkout");
await page.goto("https://example.com/checkout");
console.log(JSON.stringify(await page.snapshotForAI(), null, 2));
EOF
```

## Guardrails

- Keep scripts small and purpose-built.
- Use named pages when a flow spans multiple scripts.
- Prefer accessible selectors such as labels, roles, and visible text.
- Remember scripts run in a sandboxed JavaScript runtime, not Node.js.
- Use `dev-browser --help` whenever you need the latest command flags or API details.
- Default to live browser automation, not test-file scaffolding, unless the user explicitly asks for tests.
