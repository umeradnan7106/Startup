// chatbot-service/backend/static/widget.js

(function () {
  const params = new URLSearchParams(location.search);
  const BOT_ID = params.get("bot_id");
  const CHAT_ENDPOINT = "/chatbot";

  function el(id){ return document.getElementById(id); }
  function createMsg(text, who){
    const d = document.createElement('div');
    d.className = 'msg ' + (who === 'user' ? 'user' : 'bot');
    d.innerHTML = `<div>${text}</div>`;
    return d;
  }
  function showEmpty(state){
    el('empty').style.display = state ? 'block' : 'none';
  }
  function typingNode(){
    const wrap = document.createElement('div');
    wrap.className = 'typing';
    wrap.innerHTML = '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
    return wrap;
  }
  function appendMessageNode(node){
    const body = el('chat-body');
    showEmpty(false);
    body.appendChild(node);
    body.scrollTop = body.scrollHeight;
  }

  async function sendMessage(){
    const input = el('input-field');
    const text = (input.value || '').trim();
    if(!text) return;
    if(!BOT_ID){ alert('Missing bot_id'); return; }

    input.value = '';
    appendMessageNode(createMsg(text, 'user'));
    const t = typingNode(); t.id='__typing'; appendMessageNode(t);

    try {
      const res = await fetch(CHAT_ENDPOINT, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message: text, bot_id: BOT_ID })
      });
      const json = await res.json();
      document.getElementById('__typing')?.remove();
      appendMessageNode(createMsg(json.response || 'No response', 'bot'));
    } catch (e) {
      document.getElementById('__typing')?.remove();
      appendMessageNode(createMsg('⚠️ Connection error.', 'bot'));
    }
  }

  document.addEventListener('DOMContentLoaded', function(){
    el('send-btn').addEventListener('click', sendMessage);
    el('input-field').addEventListener('keydown', e => { if(e.key === 'Enter') sendMessage(); });

    el('minimize-btn').addEventListener('click', function(){
      const card = el('chat-card');
      card.classList.toggle('min');
    });

    el('close-btn').addEventListener('click', function(){
      if(window.parent && window.parent !== window){
        window.parent.postMessage({ type:'widget-close' }, '*');
      } else {
        document.body.style.display = 'none';
      }
    });
  });
})();
