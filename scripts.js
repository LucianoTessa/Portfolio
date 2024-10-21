function smoothScroll(target) {
    const targetElement = document.querySelector(target);
    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - 150;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, 1000);
        window.scrollTo(0, run);
        if (timeElapsed < 1000) requestAnimationFrame(animation);
    }

    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
}

document.querySelector('h1 a[href^="#"]').addEventListener("click", function (e) {
    e.preventDefault();
    smoothScroll(this.getAttribute('href'));
});
document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        smoothScroll(this.getAttribute('href'));
    });
});

window.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const darkModeToggle = document.getElementById('darkModeToggle');
    const lightModeToggle = document.getElementById('lightModeToggle');

    if (body.classList.contains('dark')) {
        darkModeToggle.style.display = 'none';
        lightModeToggle.style.display = 'inline-block';
    } else {
        lightModeToggle.style.display = 'none';
        darkModeToggle.style.display = 'inline-block';
    }

    darkModeToggle.addEventListener('click', () => {
        body.classList.add('dark');
        darkModeToggle.style.display = 'none';
        lightModeToggle.style.display = 'inline-block';
    });

    lightModeToggle.addEventListener('click', () => {
        body.classList.remove('dark');
        lightModeToggle.style.display = 'none';
        darkModeToggle.style.display = 'inline-block';
    });
});