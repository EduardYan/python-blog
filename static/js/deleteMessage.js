// Script for delete
// the messages

setTimeout(() => {
  try {
    const container = document.querySelector('.container');
    const message = document.querySelector('.message');
    container.removeChild(message);

  } catch(TypeError) {
    // in case not found the element of the message
    console.log('')
  }

}, 2000)