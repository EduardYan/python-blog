/**
 *  Some utils functions to use
 */


/**
 * 
 * @returns The list of buttons
 */
function getButtons() {

  const buttons = document.querySelectorAll('.comment-button');

  return buttons;

}

/**
 * 
 * @param {HTMLElement} button The html button to clean
 */
function clearComment(button) {
  // getting and cleaning
  const textarea = button.parentElement.parentElement
  textarea.childNodes[9].value = ''

}

/**
 * 
 * @returns The value was get of the textarea
 */
/**
 * 
 * @param {HTMLElement} button The html button for get the value
 * @returns The value of the textarea element of the button
 */
function getValueComment(button) {

  // getting
  const textarea = button.parentElement.parentElement
  const value = textarea.childNodes[9].value

  return value;

}


/**
 * @param {HTMLElement} button The button to get more data
 * @param {string} comment The value of the comment for show
 */
function showComment(button, comment) {

  const textarea = button.parentElement.parentElement;

  // section from the comentaries
  const comentaries = textarea.childNodes[17];

  // date to show
  const date = getDateCurrent()

  const element = document.createElement('div');
  element.innerHTML = `
    <p>${date}</p>
    <p>
      <i class="fa-solid fa-comment"></i>
      ${comment}
    </p>
    <hr>
  `;

  comentaries.append(element);

}

/**
 * 
 * @returns The data current in string with a format
 */
function getDateCurrent() {
  var today = new Date();

  const formated = `On ${today.getDate()}/${today.getMonth()}/${today.getFullYear()} at ${today.getHours()}:${today.getMinutes()}`;

  return formated;

}

export default { showComment, clearComment, getValueComment, getButtons, clearComment };