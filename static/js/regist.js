// 변수 선언
let attempts = 0;
let index = 0;

async function makerStart(value) {
  const res = await fetch("/createGame", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: new Date(),
      content: value,
    }),
  });
}
