from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nostalgia — por qué nos consume · Mery C.E.</title>
    <meta name="description" content="Un ensayo psicológico sobre la nostalgia, la memoria y la identidad. Por Mery C.E.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=IM+Fell+English:ital@0;1&family=Spectral:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap" rel="stylesheet">

    <style>
        :root {
            --fog-white: #eee9e0;
            --mist: #d9d0c3;
            --ash: #a89e92;
            --dusk: #7a6d62;
            --shadow: #3e342a;
            --deep: #201a14;
            --ground: #140f0a;
            --sepia: #c0a87c;
            --sepia-dim: rgba(192,168,124,0.18);
            --border: rgba(192,168,124,0.12);
            --fog-glow: rgba(200,185,155,0.055);
        }

        *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

        html { scroll-behavior: smooth; }

        body {
            font-family: 'Spectral', serif;
            background-color: var(--ground);
            color: var(--mist);
            overflow-x: hidden;
            cursor: default;
        }

        /* ── GRAIN ── */
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.78' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
            opacity: 0.05;
            pointer-events: none;
            z-index: 9999;
        }

        /* ── FOG LAYERS ── */
        .fog { position:fixed; inset:0; pointer-events:none; z-index:1; }

        .fog-1::before {
            content:''; position:absolute;
            width:1100px; height:600px;
            background: radial-gradient(ellipse, rgba(210,195,165,0.07) 0%, transparent 65%);
            top:-180px; left:-300px;
            border-radius:50%; filter:blur(90px);
            animation: fd1 50s ease-in-out infinite;
        }
        .fog-1::after {
            content:''; position:absolute;
            width:800px; height:500px;
            background: radial-gradient(ellipse, rgba(180,160,130,0.05) 0%, transparent 65%);
            bottom:5%; right:-200px;
            border-radius:50%; filter:blur(80px);
            animation: fd2 65s ease-in-out infinite;
        }
        .fog-2::before {
            content:''; position:absolute;
            width:700px; height:700px;
            background: radial-gradient(ellipse, rgba(215,200,170,0.04) 0%, transparent 65%);
            top:35%; left:25%;
            border-radius:50%; filter:blur(100px);
            animation: fd1 72s ease-in-out infinite 8s reverse;
        }
        .fog-2::after {
            content:''; position:absolute;
            width:900px; height:350px;
            background: radial-gradient(ellipse, rgba(190,170,140,0.05) 0%, transparent 65%);
            bottom:-80px; left:-100px;
            border-radius:50%; filter:blur(70px);
            animation: fd2 55s ease-in-out infinite 3s;
        }
        /* Thin horizon fog strip */
        .fog-horizon {
            position:fixed; bottom:0; left:0; right:0;
            height:220px; pointer-events:none; z-index:1;
            background: linear-gradient(to top, rgba(20,15,10,0.7) 0%, transparent 100%);
        }

        @keyframes fd1 {
            0%   { opacity:0; transform:translate(0,0) scale(1); }
            15%  { opacity:1; }
            50%  { transform:translate(80px,-50px) scale(1.18); opacity:1; }
            85%  { opacity:1; }
            100% { opacity:0; transform:translate(0,0) scale(1); }
        }
        @keyframes fd2 {
            0%   { opacity:0; transform:translate(0,0) scale(1); }
            15%  { opacity:1; }
            50%  { transform:translate(-60px,40px) scale(1.12); opacity:1; }
            85%  { opacity:1; }
            100% { opacity:0; transform:translate(0,0) scale(1); }
        }

        /* ── NAVBAR ── */
        nav {
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 100;
            padding: 22px 48px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(to bottom, rgba(20,15,10,0.92) 0%, transparent 100%);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
        }

        .nav-brand {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1rem;
            font-weight: 300;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--sepia);
            text-decoration: none;
            opacity: 0.85;
        }

        .nav-links {
            display: flex;
            gap: 36px;
            list-style: none;
        }

        .nav-links a {
            font-family: 'Spectral', serif;
            font-size: 0.72rem;
            letter-spacing: 0.32em;
            text-transform: uppercase;
            color: var(--ash);
            text-decoration: none;
            opacity: 0.7;
            transition: opacity 0.3s, color 0.3s;
        }

        .nav-links a:hover { opacity: 1; color: var(--mist); }

        /* ── HERO ── */
        header {
            min-height: 100vh;
            display: grid;
            place-items: center;
            position: relative;
            z-index: 2;
            padding: 120px 30px 80px;
            overflow: hidden;
        }

        header::before {
            content: '';
            position: absolute;
            inset: 0;
            background:
                radial-gradient(ellipse 90% 70% at 50% 35%, rgba(160,135,100,0.07) 0%, transparent 70%),
                radial-gradient(ellipse 50% 40% at 15% 85%, rgba(90,70,50,0.07) 0%, transparent 55%),
                radial-gradient(ellipse 40% 30% at 85% 70%, rgba(100,80,55,0.05) 0%, transparent 55%);
        }

        /* Fog ground at hero bottom */
        header::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 280px;
            background: linear-gradient(to top, var(--ground) 0%, transparent 100%);
            pointer-events: none;
        }

        .hero-inner {
            max-width: 820px;
            text-align: center;
            position: relative;
            animation: heroReveal 2.8s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        .hero-tag {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            font-family: 'Spectral', serif;
            font-size: 0.68rem;
            font-weight: 300;
            letter-spacing: 0.38em;
            text-transform: uppercase;
            color: var(--sepia);
            opacity: 0.65;
            margin-bottom: 44px;
        }

        .hero-tag::before, .hero-tag::after {
            content: '';
            width: 28px;
            height: 1px;
            background: var(--sepia);
            opacity: 0.5;
        }

        .hero h1 {
            font-family: 'Cormorant Garamond', serif;
            font-weight: 300;
            font-size: clamp(2.8rem, 7vw, 5.6rem);
            line-height: 1.09;
            color: var(--fog-white);
            margin-bottom: 40px;
            letter-spacing: -0.015em;
        }

        .hero h1 em {
            font-style: italic;
            color: var(--sepia);
        }

        .hero-divider {
            display: flex;
            align-items: center;
            gap: 18px;
            justify-content: center;
            margin: 0 auto 40px;
        }

        .hero-divider span {
            width: 55px;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(192,168,124,0.45));
        }

        .hero-divider span:last-child {
            background: linear-gradient(90deg, rgba(192,168,124,0.45), transparent);
        }

        .hero-divider-glyph {
            font-family: 'IM Fell English', serif;
            font-size: 0.9rem;
            color: var(--sepia);
            opacity: 0.55;
        }

        .hero-lead {
            font-family: 'Spectral', serif;
            font-size: 1.08rem;
            line-height: 2;
            color: var(--ash);
            font-weight: 300;
            font-style: italic;
            max-width: 620px;
            margin: 0 auto 52px;
        }

        /* ── BLOG META STRIP ── */
        .blog-meta {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 28px;
            flex-wrap: wrap;
            margin-bottom: 52px;
        }

        .meta-item {
            font-family: 'Spectral', serif;
            font-size: 0.7rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--dusk);
        }

        .meta-dot {
            width: 3px; height: 3px;
            border-radius: 50%;
            background: var(--sepia);
            opacity: 0.35;
        }

        .scroll-hint {
            font-family: 'Spectral', serif;
            font-size: 0.68rem;
            letter-spacing: 0.42em;
            text-transform: uppercase;
            color: var(--dusk);
            animation: breathe 3.5s ease-in-out infinite;
            display: block;
        }

        /* ── TABLE OF CONTENTS ── */
        .toc-wrap {
            max-width: 780px;
            margin: 0 auto;
            padding: 0 30px 60px;
            position: relative;
            z-index: 2;
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 1.2s ease, transform 1.2s ease;
        }

        .toc-wrap.visible { opacity:1; transform:translateY(0); }

        .toc {
            border: 1px solid var(--border);
            padding: 38px 44px;
            position: relative;
            background: rgba(20,15,10,0.6);
        }

        .toc::before {
            content: 'Índice';
            position: absolute;
            top: -10px; left: 32px;
            background: var(--ground);
            padding: 0 14px;
            font-family: 'Spectral', serif;
            font-size: 0.67rem;
            letter-spacing: 0.38em;
            text-transform: uppercase;
            color: var(--sepia);
            opacity: 0.75;
        }

        .toc ol {
            list-style: none;
            counter-reset: toc;
        }

        .toc ol li {
            counter-increment: toc;
            display: flex;
            align-items: baseline;
            gap: 14px;
            padding: 10px 0;
            border-bottom: 1px solid rgba(192,168,124,0.07);
        }

        .toc ol li:last-child { border-bottom: none; }

        .toc ol li::before {
            content: counter(toc, upper-roman);
            font-family: 'Cormorant Garamond', serif;
            font-size: 0.72rem;
            letter-spacing: 0.15em;
            color: var(--sepia);
            opacity: 0.6;
            min-width: 26px;
        }

        .toc ol li a {
            font-family: 'Spectral', serif;
            font-size: 0.92rem;
            font-weight: 300;
            color: var(--ash);
            text-decoration: none;
            transition: color 0.3s;
            flex: 1;
        }

        .toc ol li a:hover { color: var(--mist); }

        .toc-dots {
            flex: 1;
            border-bottom: 1px dotted rgba(192,168,124,0.2);
            margin-bottom: 3px;
        }

        /* ── SECTIONS ── */
        main { position: relative; z-index: 2; }

        .chapter {
            max-width: 740px;
            margin: 0 auto;
            padding: 80px 30px;
            opacity: 0;
            transform: translateY(48px);
            transition: opacity 1.3s ease, transform 1.3s ease;
        }

        .chapter.visible { opacity:1; transform:translateY(0); }

        .chapter-number {
            font-family: 'Cormorant Garamond', serif;
            font-size: 0.68rem;
            letter-spacing: 0.42em;
            color: var(--dusk);
            text-transform: uppercase;
            margin-bottom: 22px;
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .chapter-number::after {
            content: '';
            flex: 1;
            max-width: 52px;
            height: 1px;
            background: var(--dusk);
            opacity: 0.35;
        }

        .chapter h2 {
            font-family: 'Cormorant Garamond', serif;
            font-weight: 400;
            font-size: clamp(1.85rem, 3.2vw, 2.7rem);
            line-height: 1.18;
            color: var(--fog-white);
            margin-bottom: 32px;
            letter-spacing: -0.01em;
        }

        .chapter h2 em {
            font-style: italic;
            color: var(--sepia);
        }

        .chapter p {
            font-size: 1.05rem;
            line-height: 2.1;
            color: var(--ash);
            font-weight: 300;
            margin-bottom: 24px;
        }

        .chapter p strong {
            color: var(--mist);
            font-weight: 400;
        }

        /* ── READING MARKER (foggy left border) ── */
        .chapter-anchor {
            display: block;
            position: relative;
            top: -80px;
            visibility: hidden;
        }

        /* ── SEPARATORS ── */
        .sep {
            max-width: 740px;
            margin: 0 auto;
            padding: 0 30px;
            display: flex;
            align-items: center;
            gap: 22px;
            opacity: 0;
            transition: opacity 1.5s ease 0.4s;
        }

        .sep.visible { opacity: 1; }

        .sep-line {
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(192,168,124,0.18), transparent);
        }

        .sep-glyph {
            font-family: 'IM Fell English', serif;
            font-size: 1rem;
            color: var(--dusk);
            opacity: 0.5;
        }

        /* ── PULL QUOTE ── */
        .pullquote {
            margin: 52px 0;
            padding: 36px 44px 36px 42px;
            border-left: 2px solid rgba(192,168,124,0.28);
            background: linear-gradient(135deg, rgba(192,168,124,0.04) 0%, transparent 100%);
            position: relative;
        }

        .pullquote::before {
            content: '\201C';
            font-family: 'Cormorant Garamond', serif;
            font-size: 6rem;
            line-height: 0;
            color: var(--sepia);
            opacity: 0.18;
            position: absolute;
            top: 60px; left: 18px;
        }

        .pullquote p {
            font-family: 'IM Fell English', serif !important;
            font-size: 1.16rem !important;
            line-height: 1.9 !important;
            color: var(--mist) !important;
            font-style: italic;
            padding-left: 22px;
            margin-bottom: 14px !important;
        }

        .pullquote cite {
            font-family: 'Spectral', serif;
            font-size: 0.72rem;
            letter-spacing: 0.22em;
            color: var(--dusk);
            text-transform: uppercase;
            padding-left: 22px;
        }

        /* ── LIST ── */
        .memory-list {
            list-style: none;
            margin: 32px 0;
            padding: 0;
        }

        .memory-list li {
            font-size: 1.02rem;
            line-height: 1.85;
            color: var(--ash);
            font-weight: 300;
            padding: 15px 0 15px 30px;
            border-bottom: 1px solid rgba(192,168,124,0.09);
            position: relative;
        }

        .memory-list li::before {
            content: '—';
            position: absolute;
            left: 0;
            color: var(--sepia);
            opacity: 0.45;
        }

        /* ── FACT BOX ── */
        .fact-box {
            margin: 44px 0;
            padding: 34px 40px;
            border: 1px solid var(--border);
            background: rgba(20,15,10,0.55);
            position: relative;
        }

        .fact-box-label {
            position: absolute;
            top: -10px; left: 28px;
            background: var(--ground);
            padding: 0 12px;
            font-family: 'Spectral', serif;
            font-size: 0.66rem;
            letter-spacing: 0.38em;
            text-transform: uppercase;
            color: var(--sepia);
            opacity: 0.75;
        }

        .fact-box p { margin-bottom: 0 !important; }

        /* ── WORD GRID (new section for Saudade etc.) ── */
        .word-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1px;
            border: 1px solid var(--border);
            margin: 40px 0;
            overflow: hidden;
        }

        .word-card {
            padding: 28px 26px;
            background: rgba(20,15,10,0.5);
            border-right: 1px solid var(--border);
            transition: background 0.4s;
        }

        .word-card:last-child { border-right: none; }
        .word-card:hover { background: rgba(192,168,124,0.04); }

        .word-lang {
            font-family: 'Spectral', serif;
            font-size: 0.62rem;
            letter-spacing: 0.35em;
            text-transform: uppercase;
            color: var(--dusk);
            margin-bottom: 8px;
        }

        .word-term {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.55rem;
            font-weight: 300;
            font-style: italic;
            color: var(--fog-white);
            margin-bottom: 10px;
            letter-spacing: -0.01em;
        }

        .word-def {
            font-family: 'Spectral', serif;
            font-size: 0.88rem;
            line-height: 1.75;
            color: var(--ash);
            font-weight: 300;
        }

        /* ── INTERLUDE ── */
        .interlude {
            background: linear-gradient(180deg, var(--ground) 0%, #0c0907 50%, var(--ground) 100%);
            padding: 110px 30px;
            position: relative;
            overflow: hidden;
        }

        .interlude::before {
            content: '';
            position: absolute;
            inset: 0;
            background:
                radial-gradient(ellipse 70% 60% at 50% 50%, rgba(160,130,85,0.05) 0%, transparent 70%);
        }

        .interlude-inner {
            max-width: 580px;
            margin: 0 auto;
            text-align: center;
            position: relative;
        }

        .interlude-glyph {
            font-family: 'Cormorant Garamond', serif;
            font-size: 4.5rem;
            color: var(--sepia);
            opacity: 0.15;
            display: block;
            margin-bottom: 32px;
            line-height: 1;
        }

        .interlude p {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(1.45rem, 2.8vw, 2.1rem);
            font-style: italic;
            font-weight: 300;
            line-height: 1.72;
            color: rgba(200,185,160,0.72);
        }

        /* ── TIMELINE (new) ── */
        .timeline {
            margin: 44px 0;
            padding: 0;
            list-style: none;
            position: relative;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0; bottom: 0;
            width: 1px;
            background: linear-gradient(to bottom, transparent, rgba(192,168,124,0.25), transparent);
        }

        .timeline-item {
            padding: 0 0 36px 36px;
            position: relative;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -3px; top: 8px;
            width: 7px; height: 7px;
            border-radius: 50%;
            border: 1px solid rgba(192,168,124,0.5);
            background: var(--ground);
        }

        .timeline-year {
            font-family: 'Cormorant Garamond', serif;
            font-size: 0.7rem;
            letter-spacing: 0.3em;
            color: var(--sepia);
            opacity: 0.7;
            margin-bottom: 6px;
            text-transform: uppercase;
        }

        .timeline-text {
            font-size: 0.97rem;
            line-height: 1.85;
            color: var(--ash);
            font-weight: 300;
        }

        /* ── CLOSING ── */
        .closing { padding: 120px 30px 80px; }

        /* ── FOOTER ── */
        footer {
            position: relative;
            z-index: 2;
            border-top: 1px solid var(--border);
        }

        .footer-inner {
            max-width: 740px;
            margin: 0 auto;
            padding: 70px 30px 50px;
        }

        .footer-top {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 40px;
            margin-bottom: 60px;
        }

        .footer-col-title {
            font-family: 'Spectral', serif;
            font-size: 0.65rem;
            letter-spacing: 0.38em;
            text-transform: uppercase;
            color: var(--sepia);
            opacity: 0.6;
            margin-bottom: 18px;
        }

        .footer-col p,
        .footer-col a {
            font-family: 'Spectral', serif;
            font-size: 0.88rem;
            line-height: 1.9;
            color: var(--dusk);
            font-weight: 300;
            text-decoration: none;
            display: block;
        }

        .footer-col a:hover { color: var(--ash); }

        .footer-bottom {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 32px;
            border-top: 1px solid var(--border);
            flex-wrap: wrap;
            gap: 12px;
        }

        .footer-copy {
            font-family: 'Spectral', serif;
            font-size: 0.72rem;
            letter-spacing: 0.2em;
            color: var(--shadow);
            text-transform: uppercase;
        }

        .footer-tags {
            display: flex;
            gap: 18px;
        }

        .footer-tag {
            font-family: 'Spectral', serif;
            font-size: 0.68rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--shadow);
            border: 1px solid rgba(192,168,124,0.12);
            padding: 4px 12px;
        }

        /* ── PROGRESS BAR ── */
        .progress-bar {
            position: fixed;
            top: 0; left: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--sepia), transparent);
            z-index: 200;
            width: 0%;
            transition: width 0.1s linear;
        }

        /* ── ANIMATIONS ── */
        @keyframes heroReveal {
            from { opacity:0; transform:translateY(36px); filter:blur(6px); }
            to   { opacity:1; transform:translateY(0);    filter:blur(0); }
        }

        @keyframes breathe {
            0%,100% { opacity:0.25; }
            50%      { opacity:0.65; }
        }

        /* ── SCROLLBAR ── */
        ::-webkit-scrollbar { width: 3px; }
        ::-webkit-scrollbar-track { background: var(--ground); }
        ::-webkit-scrollbar-thumb { background: rgba(192,168,124,0.25); border-radius: 2px; }

        /* ── RESPONSIVE ── */
        @media (max-width: 640px) {
            nav { padding: 18px 24px; }
            .nav-links { display: none; }
            .footer-top { grid-template-columns: 1fr; gap: 32px; }
            .word-grid { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>

    <div class="progress-bar" id="progress"></div>
    <div class="fog fog-1"></div>
    <div class="fog fog-2"></div>
    <div class="fog-horizon"></div>

    <!-- ── NAVBAR ── -->
    <nav>
        <a href="#" class="nav-brand">Mery C.E.</a>
        <ul class="nav-links">
            <li><a href="#cerebro">El cerebro</a></li>
            <li><a href="#neurologia">Neurología</a></li>
            <li><a href="#emocion">La emoción</a></li>
            <li><a href="#tiempo">Tiempo</a></li>
            <li><a href="#paradoja">Paradoja</a></li>
        </ul>
    </nav>

    <!-- ── HERO ── -->
    <header>
        <div class="hero-inner">
            <p class="hero-tag">Ensayo psicológico</p>
            <h1>Nostalgia:<br>por qué nos <em>consume</em></h1>
            <div class="hero-divider">
                <span></span>
                <span class="hero-divider-glyph">✦</span>
                <span></span>
            </div>
            <p class="hero-lead">
                La nostalgia no es simplemente recordar. Es habitar emocionalmente
                un mundo que ya no existe — una neblina entre quien fuiste
                y quien eres ahora.
            </p>
            <div class="blog-meta">
                <span class="meta-item">Mery C.E.</span>
                <span class="meta-dot"></span>
                <span class="meta-item">2025</span>
                <span class="meta-dot"></span>
                <span class="meta-item">Lectura · 14 min</span>
                <span class="meta-dot"></span>
                <span class="meta-item">Psicología · Memoria</span>
            </div>
            <span class="scroll-hint">↓ &nbsp; descender</span>
        </div>
    </header>

    <!-- ── MAIN ── -->
    <main>

        <!-- ── TABLE OF CONTENTS ── -->
        <div class="toc-wrap" id="toc-wrap">
            <div class="toc">
                <ol>
                    <li>
                        <a href="#cerebro">Lo que ocurre dentro de la mente nostálgica</a>
                        <span class="toc-dots"></span>
                    </li>
                    <li>
                        <a href="#neurologia">Por qué algunos recuerdos duelen físicamente</a>
                        <span class="toc-dots"></span>
                    </li>
                    <li>
                        <a href="#emocion">Una mezcla que el lenguaje apenas puede nombrar</a>
                        <span class="toc-dots"></span>
                    </li>
                    <li>
                        <a href="#tiempo">El mundo que vivimos y el que anhelamos</a>
                        <span class="toc-dots"></span>
                    </li>
                    <li>
                        <a href="#identidad">Quién eres tú sin la memoria de quién fuiste</a>
                        <span class="toc-dots"></span>
                    </li>
                    <li>
                        <a href="#paradoja">La memoria que embellece lo que nunca fue perfecto</a>
                        <span class="toc-dots"></span>
                    </li>
                    <li>
                        <a href="#conclusion">Entonces, ¿por qué nos consume?</a>
                        <span class="toc-dots"></span>
                    </li>
                </ol>
            </div>
        </div>

        <!-- ── CAP I ── -->
        <span class="chapter-anchor" id="cerebro"></span>
        <div class="chapter">
            <div class="chapter-number">I &nbsp;&nbsp; El cerebro emocional</div>
            <h2>Lo que ocurre dentro<br>de la <em>mente nostálgica</em></h2>
            <p>
                Los psicólogos Constantine Sedikides y Tim Wildschut dedicaron décadas a estudiar la nostalgia como fenómeno psicológico formal. Sus investigaciones demostraron que este sentimiento no es un mero capricho sentimental: <strong>cumple una función reguladora dentro del sistema emocional humano</strong>.
            </p>
            <p>
                La nostalgia tiende a emerger con mayor intensidad durante momentos de soledad, incertidumbre o transición. El cerebro la activa como mecanismo de autorregulación: una manera de recuperar estabilidad cuando el presente resulta demasiado incierto o doloroso.
            </p>
            <ul class="memory-list">
                <li>Refuerza la sensación de pertenencia a algo más grande que uno mismo.</li>
                <li>Mantiene una continuidad emocional del "yo" a través del tiempo.</li>
                <li>Reduce temporalmente sentimientos de vacío y aislamiento existencial.</li>
                <li>Activa memorias asociadas con vínculos seguros y afecto genuino.</li>
                <li>Eleva el estado de ánimo en personas que experimentan soledad crónica.</li>
            </ul>
            <p>
                Lo que distingue a la nostalgia de la simple tristeza es su naturaleza mixta: contiene, al mismo tiempo, la calidez del recuerdo y el dolor de la distancia. Los investigadores describen este estado como <strong>agridulce</strong>, y esa dualidad es precisamente lo que lo hace tan difícil de resolver o ignorar.
            </p>
        </div>

        <div class="sep">
            <div class="sep-line"></div>
            <span class="sep-glyph">✦</span>
            <div class="sep-line"></div>
        </div>

        <!-- ── CAP II ── -->
        <span class="chapter-anchor" id="neurologia"></span>
        <div class="chapter">
            <div class="chapter-number">II &nbsp;&nbsp; Neurología</div>
            <h2>Por qué algunos recuerdos<br><em>duelen físicamente</em></h2>
            <p>
                Los estudios de neuroimagen revelan que ciertos estímulos —una canción, un aroma, la textura de un objeto viejo— activan simultáneamente la amígdala, el hipocampo y el córtex prefrontal medial. Estas tres regiones están involucradas en el procesamiento emocional, la memoria autobiográfica y la identidad personal.
            </p>
            <p>
                Cuando convergen, producen algo extraordinario: <strong>la sensación de que un momento pasado vuelve a existir brevemente dentro del cuerpo</strong>. Un vacío en el pecho. Un nudo en la garganta. La certeza momentánea de que algo fue real y ya no está.
            </p>
            <div class="fact-box">
                <span class="fact-box-label">Hallazgo clínico</span>
                <p>
                    Investigaciones de la Universidad de Southampton encontraron que las personas que experimentan nostalgia con frecuencia reportan una mayor sensación de <strong>continuidad personal</strong> y niveles más altos de bienestar psicológico general, siempre que el recuerdo no derive en rumiación crónica.
                </p>
            </div>
            <p>
                Los olores, en particular, tienen una vía directa hacia el hipocampo —sin pasar por el tálamo, a diferencia de la mayoría de los estímulos sensoriales. Esto explica por qué un perfume puede devolverte a un año específico con una precisión casi dolorosa, mientras que una fotografía puede tardar más en activar la misma respuesta emocional.
            </p>
            <p>
                La clave no está en el recuerdo en sí, sino en el significado emocional que el cerebro le asignó en el momento original. Los recuerdos más poderosos son casi siempre los que estuvieron ligados a un sentido de conexión, de amor, o de vitalidad intensa.
            </p>
        </div>

        <!-- ── INTERLUDE ── -->
        <div class="interlude">
            <div class="interlude-inner chapter">
                <span class="interlude-glyph">∿</span>
                <p>
                    "La nostalgia actúa como un puente psicológico entre quiénes fuimos y quiénes somos. No nos lleva hacia atrás — nos revela que existió algo que valió la pena."
                </p>
            </div>
        </div>

        <!-- ── CAP III ── -->
        <span class="chapter-anchor" id="emocion"></span>
        <div class="chapter">
            <div class="chapter-number">III &nbsp;&nbsp; Emoción compleja</div>
            <h2>Una mezcla que el lenguaje<br><em>apenas puede nombrar</em></h2>
            <p>
                En 1688, el médico suizo Johannes Hofer acuñó el término <em>nostalgia</em> a partir del griego <em>nóstos</em> (regreso al hogar) y <em>álgos</em> (dolor). Lo describió originalmente como una enfermedad: soldados suizos que morían de tristeza al estar lejos de los Alpes.
            </p>

            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-year">1688</div>
                    <div class="timeline-text">Johannes Hofer la clasifica como enfermedad clínica, "nostalgia", presente en soldados desplazados.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">S. XIX</div>
                    <div class="timeline-text">La psiquiatría europea la mantiene como diagnóstico. Se asocia con debilidad emocional y desadaptación.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">1970s</div>
                    <div class="timeline-text">Los psicólogos comienzan a reconsiderarla no como patología, sino como mecanismo emocional adaptativo.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2000s</div>
                    <div class="timeline-text">Sedikides y Wildschut la establecen formalmente como constructo psicológico con función regulatoria positiva.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">Hoy</div>
                    <div class="timeline-text">Se estudia en relación con identidad, bienestar, creatividad y respuesta al estrés crónico.</div>
                </div>
            </div>

            <p>
                Hoy sabemos que no es una enfermedad, sino una emoción compleja: una <strong>superposición simultánea de alegría, pérdida, amor, melancolía y deseo</strong>. La mayoría de las palabras para nombrar emociones describen estados simples. La nostalgia es distinta porque contiene contrarios al mismo tiempo.
            </p>

            <div class="word-grid">
                <div class="word-card">
                    <div class="word-lang">Portugués</div>
                    <div class="word-term">Saudade</div>
                    <div class="word-def">Anhelo profundo por algo amado que se ha perdido, con la consciencia de que no volverá.</div>
                </div>
                <div class="word-card">
                    <div class="word-lang">Galés</div>
                    <div class="word-term">Hiraeth</div>
                    <div class="word-def">Añoranza por un hogar al que no se puede volver, o que quizá nunca existió.</div>
                </div>
                <div class="word-card">
                    <div class="word-lang">Turco</div>
                    <div class="word-term">Hüzün</div>
                    <div class="word-def">Melancolía colectiva por la belleza de lo que fue y ya no es. Una tristeza compartida y casi estética.</div>
                </div>
                <div class="word-card">
                    <div class="word-lang">Japonés</div>
                    <div class="word-term">Mono no aware</div>
                    <div class="word-def">La conmoción agridulce ante la transitoriedad de las cosas bellas.</div>
                </div>
            </div>

            <div class="pullquote">
                <p>Quizá duele tanto porque no extrañamos el pasado en sí. Extrañamos cómo <em>éramos</em> dentro de él: más jóvenes, más presentes, más vivos ante ciertas cosas.</p>
            </div>
        </div>

        <div class="sep">
            <div class="sep-line"></div>
            <span class="sep-glyph">✦</span>
            <div class="sep-line"></div>
        </div>

        <!-- ── CAP IV ── -->
        <span class="chapter-anchor" id="tiempo"></span>
        <div class="chapter">
            <div class="chapter-number">IV &nbsp;&nbsp; Cultura y tiempo</div>
            <h2>El mundo que vivimos<br>y el que <em>anhelamos</em></h2>
            <p>
                Vivimos en una era de aceleración sin precedentes. Los ciclos tecnológicos, culturales y relacionales se comprimen. Lo que hoy es nuevo, mañana ya es obsoleto. En ese contexto, el pasado comienza a percibirse no como algo inferior o superado, sino como <strong>algo más auténtico, más cálido, menos fragmentado</strong>.
            </p>
            <p>
                Por eso tantas corrientes culturales contemporáneas buscan activamente esa textura del pasado: la fotografía analógica, los vinilos, la estética <em>lo-fi</em>, las películas de grano grueso, los videojuegos retro. No son modas superficiales. Son respuestas emocionales colectivas a un presente que muchas personas experimentan como demasiado efímero para ser aprehendido.
            </p>
            <ul class="memory-list">
                <li>La fotografía analógica recupera la imperfección como forma de presencia.</li>
                <li>Los vinilos obligan a detenerse, a escuchar un álbum completo sin interrupciones.</li>
                <li>La estética <em>lo-fi</em> recrea el sonido de una grabación que el tiempo ha tocado.</li>
                <li>Las cartas escritas a mano devuelven el peso físico a las palabras.</li>
                <li>El cine en 16mm o Super 8 convierte la imperfección técnica en huella emocional.</li>
            </ul>
            <p>
                Esta estética de la nostalgia no es regresión. Es una búsqueda de densidad emocional en un mundo que tiende hacia lo volátil. El ser humano no puede procesar experiencias si estas no tienen tiempo de sedimentar.
            </p>
            <div class="fact-box">
                <span class="fact-box-label">Perspectiva sociológica</span>
                <p>
                    El sociólogo Zygmunt Bauman describió nuestra época como <strong>modernidad líquida</strong>: una condición en que los vínculos, identidades e instituciones pierden solidez permanente. En ese marco, la nostalgia actúa como ancla: devuelve la ilusión de que algo fue sólido, que algo duró.
                </p>
            </div>
        </div>

        <div class="sep">
            <div class="sep-line"></div>
            <span class="sep-glyph">✦</span>
            <div class="sep-line"></div>
        </div>

        <!-- ── CAP V (NUEVO) ── -->
        <span class="chapter-anchor" id="identidad"></span>
        <div class="chapter">
            <div class="chapter-number">V &nbsp;&nbsp; Identidad</div>
            <h2>Quién eres tú sin la memoria<br>de <em>quién fuiste</em></h2>
            <p>
                La nostalgia tiene una dimensión que raramente se discute con claridad: no extrañamos únicamente a personas o lugares. Extrañamos <strong>versiones de nosotros mismos</strong> que habitaron esos lugares y amaron a esas personas.
            </p>
            <p>
                El yo no es una estructura fija. Se construye y reconstruye continuamente a partir de los recuerdos que seleccionamos, las historias que nos contamos sobre el pasado, y la manera en que esas historias dan sentido al presente. En ese proceso, la nostalgia funciona como <strong>un material de construcción de identidad</strong>.
            </p>
            <div class="pullquote">
                <p>Recordar no es recuperar información. Es <em>recrear activamente</em> una versión del pasado que mantiene coherente la narrativa de quién somos.</p>
            </div>
            <p>
                Los psicólogos llaman a esto <em>función de continuidad del yo</em>: la necesidad de percibirse como la misma persona a través del tiempo, a pesar de los cambios inevitables. La nostalgia refuerza esa continuidad al conectar el presente con momentos en que la identidad se sintió sólida, clara, genuina.
            </p>
            <p>
                Cuando esto se rompe —por duelo, migración, trauma o simplemente el paso del tiempo— la nostalgia puede volverse más intensa, casi insoportable. No porque el pasado fuera mejor, sino porque contenía versiones del yo que el presente todavía no ha encontrado cómo reemplazar.
            </p>
            <div class="fact-box">
                <span class="fact-box-label">Investigación reciente</span>
                <p>
                    Estudios publicados en <em>Personality and Social Psychology Bulletin</em> mostraron que inducir nostalgia deliberadamente aumenta el sentido de continuidad del yo, eleva la autoestima y reduce la ansiedad existencial ante la muerte — un hallazgo que sugiere que recordar no es solo mirar atrás, sino <strong>afirmar que uno existe de manera coherente en el tiempo</strong>.
                </p>
            </div>
        </div>

        <!-- ── INTERLUDE 2 ── -->
        <div class="interlude">
            <div class="interlude-inner chapter">
                <span class="interlude-glyph">∿</span>
                <p>
                    "Cada vez que la niebla cubre un paisaje, el paisaje sigue ahí. La memoria funciona de manera similar: lo que no vemos no ha desaparecido — se ha vuelto más difícil de alcanzar."
                </p>
            </div>
        </div>

        <!-- ── CAP VI ── -->
        <span class="chapter-anchor" id="paradoja"></span>
        <div class="chapter">
            <div class="chapter-number">VI &nbsp;&nbsp; La paradoja</div>
            <h2>La memoria que embellece<br>lo que <em>nunca fue perfecto</em></h2>
            <p>
                Existe una paradoja en el corazón de la nostalgia: los recuerdos que más anhelamos raramente corresponden a momentos que en su día fueron perfectos. La memoria funciona como un <strong>filtro que suaviza las aristas y amplifica el brillo emocional</strong>. Los psicólogos llaman a esto el <em>efecto de rosa</em>, o más formalmente, la tendencia al sesgo positivo en la memoria autobiográfica.
            </p>
            <p>
                Recordamos las tardes de verano, no el calor agobiante. Recordamos la música de la adolescencia, no la inseguridad que la acompañaba. Recordamos las conversaciones largas, no los silencios incómodos. El cerebro no archiva momentos: archiva significados.
            </p>
            <div class="fact-box">
                <span class="fact-box-label">Para considerar</span>
                <p>
                    Esto no significa que la nostalgia sea engañosa. Significa que lo que recordamos con más fuerza es aquello que tuvo <strong>un peso emocional genuino</strong>. La distorsión no borra la verdad — la revela: ese momento importó.
                </p>
            </div>
            <p>
                La paradoja se profundiza cuando la nostalgia se vuelve escapismo. Cuando la idealización del pasado no funciona como ancla, sino como evasión del presente. En ese punto, la función reguladora se invierte: en lugar de darnos recursos para continuar, nos detiene en un momento que el tiempo ya clausuró.
            </p>
            <p>
                La diferencia entre nostalgia sana y nostalgia paralizante no está en la intensidad del recuerdo, sino en la dirección a la que apunta: <strong>¿ilumina el presente o lo oscurece?</strong>
            </p>
        </div>

        <!-- ── CAP VII ── -->
        <span class="chapter-anchor" id="conclusion"></span>
        <div class="chapter closing">
            <div class="chapter-number">VII &nbsp;&nbsp; Conclusión</div>
            <h2>Entonces, ¿por qué<br>nos <em>consume</em>?</h2>
            <p>
                Porque nos enfrenta directamente con algo que el ser humano raramente acepta sin resistencia: el tiempo avanza, nada permanece intacto, y ciertas versiones del mundo —y de nosotros mismos— dejan de existir para siempre.
            </p>
            <p>
                La nostalgia nos recuerda quiénes fuimos. Nos devuelve, por un instante, la presencia de personas que ya no están o de versiones nuestras que ya no habitamos. Pero también demuestra algo importante: que existieron experiencias capaces de afectarnos con suficiente profundidad como para que el cerebro las conserve durante años.
            </p>
            <p>
                En ese sentido, la nostalgia no es únicamente una forma de tristeza. Es también <strong>una prueba de que algo fue real</strong>. De que vivimos, amamos y fuimos afectados por el mundo. La niebla que la acompaña no es vacío: es la textura del tiempo que se asienta sobre lo que alguna vez fue luminoso.
            </p>
            <div class="pullquote">
                <p>Quizá la nostalgia duele tanto porque el cerebro humano no olvida fácilmente aquello que alguna vez lo hizo sentirse completamente vivo.</p>
                <cite>— Mery C.E.</cite>
            </div>
        </div>

    </main>

    <!-- ── FOOTER ── -->
    <footer>
        <div class="footer-inner">
            <div class="footer-top">
                <div class="footer-col">
                    <div class="footer-col-title">Sobre este texto</div>
                    <p>Un ensayo psicológico sobre la memoria, la identidad y el tiempo. Escrito desde la niebla entre lo que fue y lo que es.</p>
                </div>
                <div class="footer-col">
                    <div class="footer-col-title">Temas</div>
                    <a href="#">Psicología cognitiva</a>
                    <a href="#">Memoria autobiográfica</a>
                    <a href="#">Identidad y tiempo</a>
                    <a href="#">Neurociencia afectiva</a>
                </div>
                <div class="footer-col">
                    <div class="footer-col-title">Autora</div>
                    <p>Mery C.E.</p>
                    <p>Escritura sobre la experiencia interior.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <span class="footer-copy">© 2025 Mery C.E.</span>
                <div class="footer-tags">
                    <span class="footer-tag">Memoria</span>
                    <span class="footer-tag">Identidad</span>
                    <span class="footer-tag">Tiempo</span>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // ── PROGRESS BAR ──
        const bar = document.getElementById('progress');
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            const total = document.documentElement.scrollHeight - window.innerHeight;
            bar.style.width = (scrolled / total * 100) + '%';
        });

        // ── SCROLL REVEAL ──
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) entry.target.classList.add('visible');
            });
        }, { threshold: 0.08, rootMargin: '0px 0px -50px 0px' });

        document.querySelectorAll('.chapter, .sep, .toc-wrap').forEach(el => observer.observe(el));

        // ── SMOOTH NAV SCROLL ──
        document.querySelectorAll('a[href^="#"]').forEach(a => {
            a.addEventListener('click', e => {
                const target = document.querySelector(a.getAttribute('href'));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)