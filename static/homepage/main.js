const animItems = document.querySelectorAll(`._anim-items`)
if (animItems.length > 0) {
    window.addEventListener(`scroll`, animOnScroll)

    function animOnScroll() {
        for (let index = 0; index < animItems.length; index++) {
            const animItem = animItems[index]
            const animItemHeight = animItem.offsetHeight
            const animItemOffSet = offset(animItem).top
            const animStart = 4;
            let animItemPoint = window.innerHeight - animItemHeight / animStart
            if (animItemHeight > window.innerHeight) {
                animItemPoint = window.innerHeight - window.innerHeight / animStart
            }
            if ((pageYOffset > animItemOffSet - animItemPoint) && pageYOffset < (animItemOffSet + animItemHeight)) {
                animItem.classList.add(`_active`)
            } else {
                if (!(animItem.classList.contains(`_anim-no-hide`))) {
                    animItem.classList.remove(`_active`)
                }
            }
        }
    }

    function offset(el) {
        const rect = el.getBoundingClientRect()
        let scrollLeft = window.pageXOffset || document.documentElement.scrollLeft
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop
        return {top: rect.top + scrollTop, left: rect.left + scrollLeft}
    }

    setTimeout(() => {
        animOnScroll()
    }, 300)
}

const burgerBtn = document.querySelector('.menu-burger');
const sideBar = document.querySelector('.side-bar');
const clouseBtn = document.querySelector('.clouse-btn');
burgerBtn.addEventListener('click', ()=>{
    sideBar.classList.add('active');
    console.log('click');

});
clouseBtn.addEventListener('click', ()=>{
    sideBar.classList.remove('active');
});


const slides = document.querySelectorAll('.slid'),
      dots = document.querySelectorAll('.dot');

let index = 0;

const activeSlide = n => {
    for(slide of slides){
        slide.classList.remove('active');
    }
    slides[n].classList.add('active');
};

const prCurrentLide = ind =>{
    activeSlide(ind);
    activeDot(ind);
}

const activeDot = n => {
    for(dot of dots){
        dot.classList.remove('active');
    }
    dots[n].classList.add('active');
};

const nextSlide = () => {
    if(index == slides.length - 1){
        index = 0;
        prCurrentLide(index);
    } else{
        index++;
        prCurrentLide(index);
    }
};

const prevSlide = () => {
    if(index == 0){
        index = slides.length - 1
        prCurrentLide(index);
    } else{
        index--;
        prCurrentLide(index);
    }
};

dots.forEach((item, indexDot) => {
    item.addEventListener('click', () =>{
        index = indexDot;
        prCurrentLide(index);
    })
});

setInterval(nextSlide, 7000);

