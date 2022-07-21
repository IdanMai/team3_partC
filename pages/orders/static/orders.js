const calc_btn = document.getElementById('setOrderBtn');
const payemnt_btn = document.getElementById('calc_price_btn');

calc_btn.addEventListener('click', () => {

  if (payemnt_btn.style.display === 'none') {
    // 👇️ this SHOWS the form
    form.style.display = 'block';
  }
});

