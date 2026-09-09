const buttonConfirm = document.querySelector('#button-confirm');


buttonConfirm.addEventListener('click', function(e){
        const answer = confirm('Подвердите своё действие!');

        if (!answer){
            e.preventDefault();
        }
})