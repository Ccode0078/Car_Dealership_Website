document.addEventListener('DOMContentLoaded', () => {
    const imgs = document.querySelectorAll('.img-select a');
    const imgBtns = [...imgs];
    let imgId = 1;

    // console.log(imgBtns)
    imgBtns.forEach((imgItem) => {
        // console.log(imgItem)
        imgItem.addEventListener('click', (event) => {
            event.preventDefault();
            imgId = imgItem.dataset.id;
            // console.log(imgId)
            slideImage();
            return true
        });
    });

    function slideImage() {
        const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;
        // console.log(displayWidth)
        console.log(imgId)
        document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId) * displayWidth}px)`;
    }

    window.addEventListener('resize', slideImage);
    return true
});
