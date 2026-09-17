# Kie.ai AI Video Pipeline — HyperFrames lesson

Учебная композиция по уроку Hardcoding PRO от 17 сентября 2026.

## Что внутри

- `lesson.html` — HyperFrames-композиция 1920×1080, 480 секунд, 24 главы.
- `storyboard.md` — карта сцен и таймингов.
- `narration.md` — текст диктора по сценам.
- `resources.md` — официальные ссылки и репозитории для аудита агентами.

## Цель урока

Подключить Kie.ai как media/tool layer к Codex, Claude Code и Hermes и собрать первое AI-видео через повторяемый workflow:

`reference → identity → research → N=9 storyboard → script → model research → production prompt → generation → QA → saved skill`

## Главный принцип

Каждую сложную тему агент исследует один раз, проверяет на практике и сохраняет как knowledge/skill. В следующий раз workflow начинается уже с накопленного знания, а не с нуля.

## Composition

- ID: `kie-ai-video-pipeline`
- Duration: `480`
- Width: `1920`
- Height: `1080`

## Безопасность

API keys не должны попадать в чат, URL/query string или логи. Для секретов использовать одноразовый bridge / локальную форму / существующий Secret Bridge.
