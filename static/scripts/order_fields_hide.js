function orderHide() {
    const form = document.getElementsByTagName('form')[0];
    for (let i = 1; i <= 3; i++) {
        form[i].parentElement.classList.add('hide-ps');
    }

    const labelChange = document.getElementById('id_total_price').previousElementSibling;
    labelChange.textContent = 'Total price in ЛВ:';
}

orderHide()