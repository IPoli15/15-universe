document.addEventListener('DOMContentLoaded', () => {
    const adminIcon = document.querySelector('.icono');
    const menuAdmin = document.querySelector('.menu-admin');

    adminIcon.addEventListener('click', () => {
        menuAdmin.classList.toggle('active');
    });

    document.addEventListener('click', (e) => {
        if (!menuAdmin.contains(e.target)) {
            menuAdmin.classList.remove('active');
        }
    });
});
