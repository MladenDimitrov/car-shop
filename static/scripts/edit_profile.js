function hideUser(){
    const formInfo = document.getElementsByClassName('auth-user')[0];
    const userInfo = formInfo.parentElement;
    userInfo.classList.add('hide-element')
}

hideUser()