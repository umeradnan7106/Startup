// lib/api.ts
export async function sendMessageToBot(message: string) {
  const res = await fetch('http://localhost:8000/chatbot', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) throw new Error('Failed to contact bot');
  return res.json();
}
