/* 
 * Some functions for the comment
 */

import utils from './utils.js';

// getting buttons
const buttons = utils.getButtons();

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const comment = utils.getValueComment(button);
    utils.showComment(button, comment); // showing
    utils.clearComment(button); // cleaning the textarea
  });
})