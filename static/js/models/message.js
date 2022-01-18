/**
 * Have the class
 * for have a model of a message
 */

export class Message {
  constructor(value) {
    this.value = value;

  }

  /**
   * Show the value of the message
   */
  showIt() {
    alert(this.value)
  }

}