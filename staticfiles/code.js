


const mobil_menu = document.querySelector('.menu')

document.getElementById('icon').addEventListener('click', () => mobil_menu.classList.add('menu-open'))

document.querySelector('.close-icon').addEventListener('click', () => mobil_menu.classList.remove('menu-open'))