/* 
 * Some functions for the comment
 *
 * 
*/

import { clearComment, getButtons } from './utils.js'


/**
 * 
 * @returns The value was get of the textarea
 */
function getValueComment() {
  const value = document.getElementById('comentary').value;
  return value;

}


/**
 * 
 * @param {string} comment The value of the comment for show
 */
function showComment(comment) {
  // getting elements for add the value
  const view = document.querySelector('.commentaries');
  const element = document.createElement('div');
  const parraf = document.createElement('p');
  const hr = document.createElement('hr');

  parraf.innerText = comment; // concatenation
  element.append(parraf)

  view.append(element, hr); // adding
  
}

// list of buttons
let buttons_list = [

  'buttons-view-1',
  'buttons-view-2',
  'buttons-view-3',
  'buttons-view-4'

];


// getting buttons
buttons_list = getButtons(buttons_list);
console.log(buttons_list)

buttons_list.forEach((button) => {
  button.addEventListener('click', () => {
    const comment = getValueComment(button);
    showComment(comment);
    clearComment;  // cleaning the textarea
  });

})
