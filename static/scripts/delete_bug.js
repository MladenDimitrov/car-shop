function deleteStrange() {
    const registerForm = document.getElementsByClassName('register-form')[0];
    registerForm[3].parentElement.previousElementSibling.remove();
}

deleteStrange()