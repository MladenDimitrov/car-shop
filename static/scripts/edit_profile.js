function showMoreInfo() {
    const moreInfoBtn = document.getElementsByClassName('show-btn');
    for (const btn of moreInfoBtn) {
        btn.addEventListener('click', ShowInfo)

        function ShowInfo() {
            const moreInfoDiv = btn.parentElement.parentElement;
            const finalMoreInfo = moreInfoDiv.getElementsByClassName('s')[0];
            finalMoreInfo.classList.add('more-info');
            finalMoreInfo.classList.remove('action-hide');
        }
    }
    const hideInfoBtn = document.getElementsByClassName('hide-btn');
    for (const btn of hideInfoBtn) {
        btn.addEventListener('click', HideInfo);

        function HideInfo() {
            const moreInfoDiv = btn.parentElement.parentElement
            const finalMoreInfo = moreInfoDiv.getElementsByClassName('s')[0];
            finalMoreInfo.classList.add('action-hide');
        }
    }
}

showMoreInfo()
