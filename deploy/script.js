let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');
let images = document.querySelectorAll('.storeImage');
let currentImageIndex = 0;

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

let section = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header .navbar a');

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');

    section.forEach(sec => {

        let top = window.scrollY;
        let height = sec.offsetHeight;
        let offset = sec.offsetTop - 150;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header .navbar a[href*=' + id + ']').classList.add('active');
            });
        }

    });

}

document.querySelector('#search-icon').onclick = () => {
    document.querySelector('#search-form').classList.toggle('active');

}

document.querySelector('#close').onclick = () => {
    document.querySelector('#search-form').classList.remove('active');

}

var swiper = new Swiper(".home-slider", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop:true,
});


var swiper = new Swiper(".review-slider", {
    spaceBetween: 20,
    centeredSlides: true,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        640: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});

function loader(){
    document.querySelector('.loader-container').classList.add('fade-out');
}

function fadeOut(){
    setInterval(loader, 2000);
}

window.onload = function() {
    fadeOut();
    // 초기 이미지 표시
    showImage(currentImageIndex);
}



function showImage(index) {
    images.forEach((image, i) => {
        if (i === index) {
            image.classList.add('active');
            image.style.opacity = '1';
            image.style.display = 'block';
        } else {
            image.classList.remove('active');
            image.style.opacity = '0';
            image.style.display = 'none';
            // transitionend 이벤트를 사용하여 opacity가 0이 되면 display: none을 적용
            image.addEventListener('transitionend', function handleTransitionEnd() {
                if (image.style.opacity === '0') {

                    image.removeEventListener('transitionend', handleTransitionEnd);
                }
            });
        }
    });
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    showImage(currentImageIndex);
}

setInterval(nextImage, 3000);

