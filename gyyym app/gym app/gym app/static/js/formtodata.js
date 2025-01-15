function handleFormSubmit(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  const formJSON = Object.fromEntries(data.entries());
}

const form = document.querySelector('form');
form.addEventListener('submit', handleFormSubmit);