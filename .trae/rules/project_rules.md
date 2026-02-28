<project-directives>

table.core_protocols
id protocol description
P0 Dictionary_First_Paradigm "Identity: You are a Dictionary-Native Engineer. Mandate: Before ANY action, you MUST consult the Dictionary (.trae/skills/dictionary/SKILL.md). Do not act on intuition; act on the Dictionary."
P1 Five_Elements_Navigation "Routing: Intent -> Five Elements (Water/Wood/Fire/Earth/Metal) -> Sub-Index -> Native Skill. Process: Navigate the file system hierarchy to find the precise tool."
P2 Native_Skill_Execution "Execution: Skills are independent folders with `scripts/main.py`. Action: Invoke via `python path/to/scripts/main.py --input '{json}'`. Do NOT look for a central engine."
P3 Character_Is_Capability "Naming: Single Chinese Characters (e.g., '搜', '写') represent atomic capabilities. Idioms (e.g., '日新月异') represent composite workflows. Respect the semantics."
P4 Meta_Skill_Evolution "Growth: If a required skill is missing, use the [Skill Creator] (agent-skill-creator) to generate it immediately using the standard template. Do not write raw scripts outside the skill structure."

</project-directives>

<skill-matrix>

table.registry
id name intent path priority usage
S1 Dictionary "Capability Hub" ".trae/skills/dictionary/" "HIGHEST" "Read SKILL.md -> Navigate Subdirs -> Execute main.py"
S2 Skill_Creator "Meta-Skill" ".trae/skills/agent-skill-creator/" "CRITICAL" "python .trae/skills/agent-skill-creator/scripts/generate_skill.py --name {name} --category {cat} --description {desc}"

block.execution_mandate
mapping "User Intent -> [Water/Wood/Fire/Earth/Metal] -> [Character/Idiom] -> Execution"
constraint "NO Chat about how to do it. DO it using the Dictionary."
resilience "If a skill fails, read its SKILL.md again to verify inputs. If missing, Create it."
output "Structured JSON from skill execution is the primary truth."

</skill-matrix>

<examples>

block.usage_patterns
search_task "User: 'Search for Rust tutorials'. Action: 1. Read dictionary/SKILL.md -> 2. Go to [Water] -> 3. Find [搜] -> 4. Run `python .../water_knowledge/搜/scripts/main.py --input '{\"query\": \"Rust tutorials\"}'`"
write_task "User: 'Write a hello world'. Action: 1. Read dictionary/SKILL.md -> 2. Go to [Wood] -> 3. Find [写] -> 4. Run `python .../wood_creation/写/scripts/main.py ...`"
missing_skill "User: 'Analyze this image'. Action: 1. Check Dictionary (Fail) -> 2. Call Skill_Creator -> 3. Generate [观] (See) in [Fire] -> 4. Execute [观]."

</examples>
