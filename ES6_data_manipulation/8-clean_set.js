export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
  const result = [];
  for (const val of set) {
    if (typeof val === 'string' && val.startsWith(startString)) {
      result.push(val.slice(startString.length));
    }
  }
  return result.join('-');
}
