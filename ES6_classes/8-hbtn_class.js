export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;  // Assure-toi que c'est bien _location avec underscore
  }
  
  valueOf() {
    return this._size;
  }
  
  toString() {
    return this._location;  // Assure-toi que c'est bien _location avec underscore
  }
}
