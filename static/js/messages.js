/*
  Script for the show the messages
  in the contacts messages
*/

import { Message } from './models/message.js'

/**
 * 
 * @returns The list of each element of contacts
 */
function getContacts() {
  const contactOne = document.getElementById('contactOne');
  const contactTwo = document.getElementById('contactTwo');
  const contactThree = document.getElementById('contactThree');
  const contactFour = document.getElementById('contactFour');

  const contacts = [
    contactOne,
    contactTwo,
    contactThree,
    contactFour
  ];

  return contacts;

}

const contacts = getContacts()

contacts[0].addEventListener('click', () => {
  const message = new Message('Contacted');
  message.showIt();
});

contacts[1].addEventListener('click', () => {
  const message = new Message('Contacted');
  message.showIt();
});

contacts[2].addEventListener('click', () => {
  const message = new Message('Contacted');
  message.showIt();
});

contacts[3].addEventListener('click', () => {
  const message = new Message('Contacted');
  message.showIt();
});