/*!
* Start Bootstrap - Freelancer v7.0.6 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

// 여러개의 이미지 파일 넣을수 있게 추가하는 코드~!
$(document).ready(function() {
    $('#add-file-input').click(function() {
        var newInput = $('<div class="mb-3">' +
                            '<label for="images" class="form-label">Images</label>' +
                            '<input type="file" class="form-control" name="images[]" accept="image/*">' +
                        '</div>');
        $('#file-inputs').append(newInput);
    });
});

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 72,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});



document.querySelector('.버튼1').addEventListener('click',function(){
    document.querySelector('.all-block').style.transform = 'translate(0vw)';
})
document.querySelector('.버튼2').addEventListener('click',function(){
    document.querySelector('.all-block').style.transform = 'translate(-100vw)';
})

document.querySelector('.버튼3').addEventListener('click',function(){
    document.querySelector('.all-block').style.transform = 'translate(-200vw)';
})

