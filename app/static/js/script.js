window.addEventListener("DOMContentLoaded", () => {
    $('.slider').slick({
        dots: true,
        infinite: false,
        speed: 300,
        arrows:false,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
              arrows:false,
              infinite: true,
              dots: true
            }
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              arrows:false
            }
          },
          {
            breakpoint: 450,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows:false
            }
          }
        ]
      });

      $('.slider2').slick({
        dots: true,
        infinite: false,
        responsive: [
          {
            breakpoint: 575,
            settings: {
              arrows:false
            }
          }
        ]
      }); 
      
      const links = document.querySelectorAll(".header_nav__link");

      links.forEach((link) => {
        link.addEventListener("click", e => {
          links.forEach(lk => {
            lk.classList.remove("active-link");
          });
          link.classList.add("active-link");
        });
      });

      
      const helpButton = document.querySelector(".price_help-button");
      const helpText = document.querySelector(".price_help");

      helpText.addEventListener("mouseover", (e) => {
        helpText.style = "display: block";
        helpText.style.opacity = 1;
      });
      helpText.addEventListener("mouseout", (e) => {
        helpText.style.opacity = 0;
        helpText.style = "display: none";
      });
      
      helpButton.addEventListener("mouseover", (e) => {
        helpText.classList.add("active-help");
        setTimeout( function() {
          helpText.style.opacity = 1;
        }, 100);
      });
      helpButton.addEventListener("mouseout", (e) => {
        
        setTimeout(() => {
          helpText.classList.remove("active-help");
        }, 500);
      });
      


      const priceButton = document.querySelector('.price_button');
      const telephon = document.querySelector('.price_telephon');

      priceButton.addEventListener('mouseover', e => {
        telephon.classList.add('active-telephon');
      });
      priceButton.addEventListener('mouseout', e => {
        telephon.classList.remove('active-telephon');
      });

      AOS.init({
        // Global settings:
        disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
        startEvent: 'DOMContentLoaded', // name of the event dispatched on the document, that AOS should initialize on
        initClassName: 'aos-init', // class applied after initialization
        animatedClassName: 'aos-animate', // class applied on animation
        useClassNames: false, // if true, will add content of `data-aos` as classes on scroll
        disableMutationObserver: false, // disables automatic mutations' detections (advanced)
        debounceDelay: 50, // the delay on debounce used while resizing window (advanced)
        throttleDelay: 99, // the delay on throttle used while scrolling the page (advanced)
        
      
        // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
        offset: 200, // offset (in px) from the original trigger point
        delay: 0, // values from 0 to 3000, with step 50ms
        duration: 1200, // values from 0 to 3000, with step 50ms
        easing: 'ease', // default easing for AOS animations
        once: true, // whether animation should happen only once - while scrolling down
        mirror: false, // whether elements should animate out while scrolling past them
        anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
      
      });
});