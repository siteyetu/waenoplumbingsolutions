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
                    // animItem.classList.remove(`_active`)
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

for ( let i of document.querySelectorAll(".counter-number") ) {

    let numberTop = i.getBoundingClientRect().top,
        start = +i.innerHTML,
        end = +i.dataset.max;
  
    window.addEventListener('scroll', function onScroll() {
      if(window.pageYOffset > numberTop - window.innerHeight / 2) {
        this.removeEventListener('scroll', onScroll);
        let interval = this.setInterval(function() {
          i.innerHTML = ++start + "+";
          if(start == end) {
            clearInterval(interval);
          }
      }, 0.1);
      }
    });
  }

  const burgerBtn = document.querySelector('.menu-burger');
  const sideBar = document.querySelector('.side-bar');
  const clouseBtn = document.querySelector('.clouse-btn');
  burgerBtn.addEventListener('click', ()=>{
      burgerBtn.classList.add('active');
      sideBar.classList.add('active');
      console.log('click');
  });

  clouseBtn.addEventListener('click', () =>{
    sideBar.classList.remove('active');
    burgerBtn.classList.remove('active');
  });
