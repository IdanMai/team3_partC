const btn = document.getElementById('btn_update_user');
const form = document.getElementById('update_user_form');

btn.addEventListener('click', () => {

  if (form.style.display === 'none') {
    // 👇️ this SHOWS the form
    form.style.display = 'block';
  } else {
    // 👇️ this HIDES the form
    form.style.display = 'none';
  }
});

//
// const btn = document.getElementById('btn_update_user');
// const form = document.getElementById('update_user_form');
//
// btn.addEventListener('click', () => {
//
//   if (form.style.visibility === 'hidden') {
//     form.style.visibility = 'visible';
//   } else {
//     form.style.visibility = 'hidden';
//   }
// });