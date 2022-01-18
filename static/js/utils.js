// Some utils functions

export function getButtons(buttons_list) {
  // new list for the buttons
  let new_buttons_list = [];

  buttons_list.forEach(button => {
    const current = document.querySelector(`.${button}`);
    new_buttons_list.push(current);

  });

  return new_buttons_list

}

export function clearComment() {
  const element = document.getElementById('comentary');
  element.value = '';

}
