// 0-promise.js
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    resolve(); // tu peux aussi laisser vide, juste retourner une Promise
  });
}
