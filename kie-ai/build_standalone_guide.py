from pathlib import Path
import base64

ROOT = Path.cwd()
TEMPLATE = ROOT / 'work' / 'guide-template.html'
VIDEO = ROOT / 'input-video' / 'Kie_AI_Video_Pipeline_True_Pavel.mp4'
MUSIC = ROOT / 'work' / 'hardcoding_ai_ambient.mp3'
POSTER = ROOT / 'work' / 'poster.jpg'
OUT = ROOT / 'dist' / 'Hardcoding_PRO_Kie_AI_Video_Guide_FINAL.html'

html = TEMPLATE.read_text(encoding='utf-8')
video_b64 = base64.b64encode(VIDEO.read_bytes()).decode('ascii')
music_b64 = base64.b64encode(MUSIC.read_bytes()).decode('ascii')
poster_b64 = base64.b64encode(POSTER.read_bytes()).decode('ascii')

extra_css = r'''
.video-hub{background:#0f0e0c;color:white;border-radius:28px;padding:18px;margin:14px 0;box-shadow:var(--shadow);border:1px solid #2a251e;overflow:hidden}.video-hub h2{color:white;margin-bottom:8px}.video-hub .sub{color:#cfc7bc;margin:0 0 16px}.video-shell{background:#000;border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,.14);box-shadow:0 18px 45px rgba(0,0,0,.28)}.video-shell video{display:block;width:100%;height:auto;aspect-ratio:16/9;background:#000}.media-bar{display:grid;grid-template-columns:1fr;gap:10px;margin-top:12px}.music-box{background:#1a1713;border:1px solid #383129;border-radius:16px;padding:13px}.music-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.music-btn{appearance:none;border:1px solid #5a4b3d;background:#ff7a1a;color:#1b1109;border-radius:12px;padding:10px 13px;font-weight:850;cursor:pointer;touch-action:manipulation}.music-btn.secondary{background:#24201a;color:#fff}.music-box audio{width:100%;margin-top:10px;height:34px}.volume{display:flex;gap:9px;align-items:center;color:#d6cec2;font-size:12px}.volume input{width:110px}.chapter-grid{display:grid;grid-template-columns:1fr;gap:8px;margin-top:14px}.chapter{appearance:none;text-align:left;width:100%;border:1px solid #d9ccba;background:#fffdf8;color:#211b14;border-radius:14px;padding:11px 12px;cursor:pointer;display:flex;gap:10px;align-items:flex-start;touch-action:manipulation}.chapter:hover,.chapter.active{border-color:#ff7a1a;box-shadow:0 0 0 2px rgba(255,122,26,.12)}.chapter .ct{font:800 11px/1.2 var(--mono);color:#a34d0f;min-width:44px}.chapter .ttl{font-size:13px;font-weight:760;line-height:1.25}.quick-start{display:grid;grid-template-columns:1fr;gap:8px;margin-top:12px}.quick-start .q{background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px;color:#17140f}.quick-start .q b{color:#9b4b13}.video-note{background:#201b16;border:1px solid #4a3d31;border-radius:14px;padding:12px 13px;color:#d8d0c4;margin-top:12px;font-size:13px}.progress-wrap{height:5px;background:#2b261f;border-radius:999px;overflow:hidden;margin:10px 0 0}.progress-bar{height:100%;width:0;background:#ff7a1a}.hero .watch-now{display:inline-flex;margin-top:18px;text-decoration:none;background:#ff7a1a;color:#1c1008;padding:11px 15px;border-radius:12px;font-weight:900;position:relative;z-index:2}.player-kpis{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:12px}.player-kpis .pk{background:#191612;border:1px solid #352e26;border-radius:13px;padding:10px}.pk b{display:block;color:#ffb376;font:900 18px/1 var(--mono)}.pk span{font-size:11px;color:#bbb1a4}@media(min-width:720px){.media-bar{grid-template-columns:1.2fr .8fr}.chapter-grid{grid-template-columns:repeat(2,1fr)}.quick-start{grid-template-columns:repeat(3,1fr)}.player-kpis{grid-template-columns:repeat(4,1fr)}}
'''
html = html.replace('</style>', extra_css + '\n</style>', 1)
html = html.replace('Hardcoding PRO · офлайн-гайд · урок 17.09.2026', 'Hardcoding PRO · видео + практический гайд · 17.09.2026', 1)
html = html.replace('<span class="badge"><strong>Источник:</strong> запись урока + актуальные docs</span>', '<span class="badge"><strong>Видео:</strong> 8:00 · Full HD</span>\n    <span class="badge"><strong>Музыка:</strong> встроена в HTML</span>', 1)
hero_close = html.find('</section>')
if hero_close != -1:
    html = html[:hero_close] + '<a class="watch-now" href="#video">▶ Смотреть 8-минутный урок</a>\n' + html[hero_close:]

chapters = [
('00:00','Что сегодня строим',0),('00:20','Вся система за 20 секунд',20),('00:40','API, MCP и Skill - это разное',40),('01:00','Pipeline и Workflow простыми словами',60),
('01:20','Подключаем агента к машине',80),('01:40','Один раз изучаем окружение',100),('02:00','Главное правило урока: research once',120),('02:20','Даём агенту официальный контекст',140),
('02:40','API key не отправляем в чат',160),('03:00','Сначала дешёвый smoke test',180),('03:20','Не пишем интеграцию с нуля',200),('03:40','Готовые репозитории и skills',220),
('04:00','Codex, Claude Code и Hermes',240),('04:20','Не говорим просто «сделай видео»',260),('04:40','Фиксируем identity персонажа',280),('05:00','Исследуем character consistency',300),
('05:20','Строим storyboard из 9 кадров',320),('05:40','Пишем 10 секунд действия',340),('06:00','Проверяем актуальную видеомодель',360),('06:20','Один раз изучаем MiniMax H3',380),
('06:40','Сценарий превращаем в production prompt',400),('07:00','Запускаем task и делаем polling',420),('07:20','ИИ сам проверяет результат',440),('07:40','Сохраняем процесс как reusable skill',460),
]
chapter_html='\n'.join([f'<button class="chapter" data-time="{sec}"><span class="ct">{ts}</span><span class="ttl">{title}</span></button>' for ts,title,sec in chapters])

media_section = f'''
<section class="video-hub" id="video">
  <div class="eyebrow">ВИДЕО УРОК · 8 МИНУТ · ВСТРОЕН В ФАЙЛ</div>
  <h2>Сначала посмотри урок. Потом проходи гайд по шагам.</h2>
  <p class="sub">Видео и музыка физически находятся внутри этого HTML. Никаких внешних ссылок для воспроизведения не нужно.</p>
  <div class="video-shell">
    <video id="lessonVideo" controls playsinline preload="metadata" poster="data:image/jpeg;base64,{poster_b64}">
      <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
      Ваш браузер не поддерживает встроенное видео.
    </video>
  </div>
  <div class="progress-wrap"><div class="progress-bar" id="lessonProgress"></div></div>
  <div class="player-kpis">
    <div class="pk"><b>8:00</b><span>длина урока</span></div>
    <div class="pk"><b>24</b><span>смысловых блока</span></div>
    <div class="pk"><b>1080p</b><span>разрешение</span></div>
    <div class="pk"><b>1 файл</b><span>видео + гайд + музыка</span></div>
  </div>
  <div class="media-bar">
    <div class="music-box">
      <b>🎵 Фоновая музыка</b>
      <p class="tiny" style="color:#cfc7bc;margin:6px 0 10px">Оригинальный спокойный AI-ambient. По умолчанию выключен, потому что браузеры блокируют autoplay. Нажми кнопку, если хочешь фон во время чтения.</p>
      <div class="music-row">
        <button class="music-btn" id="musicToggle" type="button">▶ Включить музыку</button>
        <button class="music-btn secondary" id="musicStop" type="button">■ Стоп</button>
        <label class="volume">Громкость <input id="musicVolume" type="range" min="0" max="1" step="0.01" value="0.14"></label>
      </div>
      <audio id="guideMusic" controls loop preload="auto" src="data:audio/mpeg;base64,{music_b64}"></audio>
    </div>
    <div class="music-box">
      <b>Как проходить этот материал</b>
      <div class="quick-start">
        <div class="q"><b>1. Посмотри</b><br><span class="tiny">8 минут целиком, чтобы увидеть систему.</span></div>
        <div class="q"><b>2. Делай</b><br><span class="tiny">Иди по секциям ниже и запускай промпты.</span></div>
        <div class="q"><b>3. Проверяй</b><br><span class="tiny">Не верь слову «готово», требуй фактический output.</span></div>
      </div>
    </div>
  </div>
  <div class="video-note"><b>Важно:</b> в видео показан конкретный execution bridge. Если у тебя другой способ дать агенту доступ к компьютеру или VPS, принцип не меняется: агент должен уметь сам работать с реальным окружением, проверять результат и сохранять рабочий контекст.</div>
</section>

<section class="section" id="chapters">
  <h2>Таймкоды урока</h2>
  <p class="lead">Нажми на нужный блок, видео выше сразу перемотается на этот момент.</p>
  <div class="chapter-grid">{chapter_html}</div>
</section>
'''
first_close = html.find('</section>')
html = html[:first_close+10] + '\n' + media_section + html[first_close+10:]
html = html.replace('Remote Desktop Commander связывает ChatGPT с Mac, Windows или VPS.', 'Execution bridge связывает AI-агента с Mac, Windows или VPS. В записи урока в качестве примера используется Remote Desktop Commander.', 1)
html = html.replace('<span>Remote Desktop Commander подключён к вашему ПК или VPS.</span>', '<span>Execution bridge подключён к вашему ПК или VPS и агент реально умеет выполнять команды.</span>', 1)
html = html.replace('<div class="fixed-cta"><a href="#checklist">✅ <span>К финальному чек-листу</span> — проверить, что всё реально работает</a></div>', '<div class="fixed-cta"><a href="#video">▶ <span>Вернуться к видео</span> · 8 минут</a></div>')

extra_js = r'''
<script>
(function(){
  const v=document.getElementById('lessonVideo');
  const p=document.getElementById('lessonProgress');
  const music=document.getElementById('guideMusic');
  const toggle=document.getElementById('musicToggle');
  const stop=document.getElementById('musicStop');
  const volume=document.getElementById('musicVolume');
  const chapters=[...document.querySelectorAll('.chapter[data-time]')];
  if(music && volume){music.volume=parseFloat(volume.value)||0.14; volume.addEventListener('input',()=>music.volume=parseFloat(volume.value)||0);}
  if(toggle && music){toggle.addEventListener('click',async()=>{try{if(music.paused){await music.play();toggle.textContent='❚❚ Пауза музыки'}else{music.pause();toggle.textContent='▶ Включить музыку'}}catch(e){}})}
  if(stop && music){stop.addEventListener('click',()=>{music.pause();music.currentTime=0;if(toggle)toggle.textContent='▶ Включить музыку'})}
  if(v){
    v.addEventListener('timeupdate',()=>{if(p&&v.duration)p.style.width=((v.currentTime/v.duration)*100)+'%'; const t=v.currentTime; let active=null; chapters.forEach(c=>{if(t>=Number(c.dataset.time))active=c;c.classList.remove('active')}); if(active)active.classList.add('active')});
    v.addEventListener('play',()=>{if(music&&!music.paused)music.volume=Math.min(parseFloat(volume?.value||0.14),0.07)});
    v.addEventListener('pause',()=>{if(music&&!music.paused)music.volume=parseFloat(volume?.value||0.14)});
  }
  chapters.forEach(btn=>btn.addEventListener('click',()=>{if(!v)return; v.currentTime=Number(btn.dataset.time)||0; v.scrollIntoView({behavior:'smooth',block:'center'}); v.play().catch(()=>{});}));
})();
</script>
'''
html = html.replace('</body>', extra_js + '\n</body>')
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding='utf-8')
print(f'BUILT {OUT} bytes={OUT.stat().st_size}')
