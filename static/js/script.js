if(document.querySelector('.messages') || document.querySelector('.errors')){
    let classMessages = document.querySelector('.messages');
    let classErrors = document.querySelector('.errors');

    setTimeout(function(){
        classMessages.style.display = 'none';
    }, 5000)

    setTimeout(function(){
        classErrors.style.display = 'none';
    }, 5000)
}