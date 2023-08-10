function deletePara() {
    const pSpec = document.getElementsByClassName('product-spec')[0];
    pSpec.remove();

    const divItem = document.getElementsByClassName('product-information')[0];
    divItem.lastElementChild.previousElementSibling.previousElementSibling.remove();

    const productDet = document.getElementsByClassName('price')[0];
    productDet.previousElementSibling.classList.add('more-information');

    const hideFormUl = document.getElementsByTagName('ul')[0];
    hideFormUl.classList.add('hide-form-ul');
}

deletePara()