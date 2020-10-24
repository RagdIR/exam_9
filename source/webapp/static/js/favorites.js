async function addFav(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        const counter = addBtn.parentElement.getElementsByClassName('counter');
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

    addBtn.classList.add('hidden');
    const delBtn = addBtn.parentElement.getElementsByClassName('del');
    unaddBtn.classList.remove('hidden');
}

async function delFav(event) {
    event.preventDefault();
    let delBtn = event.target;
    let url = delBtn.href;

    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
        const counter = delBtn.parentElement.getElementsByClassName('counter')[0];
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

    delBtn.classList.add('hidden');
    const addBtn = delBtn.parentElement.getElementsByClassName('del')[0];
    delBtn.classList.remove('hidden');
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('add');
    const delButtons = document.getElementsByClassName('del');

    for (let btn of addButtons) {btn.onclick = addFav}
    for (let btn of delButtons) {btn.onclick = delFav}
});