// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
  navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));
}

// Process line fill + step lighting on scroll
const track = document.getElementById('processTrack');
if (track) {
  const fill = document.getElementById('processFill');
  const steps = document.querySelectorAll('.step');
  let played = false;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !played) {
        played = true;
        fill.style.width = '100%';
        steps.forEach((s, i) => setTimeout(() => s.classList.add('lit'), 250 + i * 260));
      }
    });
  }, { threshold: 0.5 });
  io.observe(track);
}

// Hero triangle-network canvas (home page only)
const canvas = document.getElementById('hero-canvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let W, H, nodes = [];
  const NODE_COUNT = 30;
  const LINK_DIST = 150;

  function resize() {
    const hero = canvas.parentElement;
    W = canvas.width = hero.offsetWidth;
    H = canvas.height = hero.offsetHeight;
  }

  function initNodes() {
    nodes = [];
    for (let i = 0; i < NODE_COUNT; i++) {
      nodes.push({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25
      });
    }
  }

  function step() {
    ctx.clearRect(0, 0, W, H);
    if (!reduceMotion) {
      nodes.forEach(n => {
        n.x += n.vx; n.y += n.vy;
        if (n.x < 0 || n.x > W) n.vx *= -1;
        if (n.y < 0 || n.y > H) n.vy *= -1;
      });
    }
    const adj = nodes.map(() => new Set());
    const edges = [];
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x, dy = nodes[i].y - nodes[j].y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < LINK_DIST) {
          edges.push([i, j, d]);
          adj[i].add(j); adj[j].add(i);
        }
      }
    }
    ctx.fillStyle = 'rgba(91,124,255,0.05)';
    for (const [i, j] of edges) {
      adj[i].forEach(k => {
        if (k > j && adj[j].has(k)) {
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.lineTo(nodes[k].x, nodes[k].y);
          ctx.closePath();
          ctx.fill();
        }
      });
    }
    edges.forEach(([i, j, d]) => {
      const alpha = 0.35 * (1 - d / LINK_DIST);
      ctx.strokeStyle = `rgba(91,124,255,${alpha})`;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(nodes[i].x, nodes[i].y);
      ctx.lineTo(nodes[j].x, nodes[j].y);
      ctx.stroke();
    });
    nodes.forEach(n => {
      ctx.beginPath();
      ctx.arc(n.x, n.y, 2, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(160,180,255,0.8)';
      ctx.fill();
    });
    if (!reduceMotion) requestAnimationFrame(step);
  }

  function start() {
    resize();
    initNodes();
    step();
  }

  window.addEventListener('resize', () => { resize(); initNodes(); if (reduceMotion) step(); });
  start();
}
