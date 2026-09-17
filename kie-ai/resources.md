# Resources for agents

Перед установкой любого репозитория агент должен сначала провести аудит: свежесть, лицензия, поддерживаемые модели, зависимости, security, качество кода, issues и совместимость с текущей архитектурой.

## Kie.ai

- Official docs: https://docs.kie.ai/
- Kie.ai: https://kie.ai/

## MCP / CLI / agent integration

- felores/kie-cli-mcp: https://github.com/felores/kie-cli-mcp

## Video / storyboard skills для исследования

- 0xadvait/ai-video-skill: https://github.com/0xadvait/ai-video-skill
- aicontentskills/ai-video-storyboard-skill: https://github.com/aicontentskills/ai-video-storyboard-skill
- Lum1104/video-to-skill: https://github.com/Lum1104/video-to-skill
- ConardLi/garden-skills: https://github.com/ConardLi/garden-skills
- datdyn2026/claude-skills-demo: https://github.com/datdyn2026/claude-skills-demo

## Research Once Protocol

Для новой модели или новой задачи агент выполняет:

1. Проверить официальную документацию.
2. Найти 2–5 сильных практических источников/репозиториев.
3. Сравнить подходы.
4. Сделать минимальный тест.
5. Зафиксировать, что реально сработало.
6. Сохранить результат как skill / project knowledge / AGENTS.md / CLAUDE.md / Hermes memory, в зависимости от агента.
7. В следующий раз использовать сохранённый skill и исследовать заново только при изменении версии модели/API или при фактической проблеме.
