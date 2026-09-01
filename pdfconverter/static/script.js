const fileInp = document.getElementById('file-Taker');
const fileList = document.getElementById('file-list');

fileInp.addEventListener('change',()=>{
    fileList.innerHTML='';

    const files = fileInp.files;

    if (files.length == 0){
        fileList.innerHTML='<li>no file selected</li>';
        return;
    }

    for (let i = 0; i < files.length; i++) {
        const li = document.createElement('li');
        li.textContent = `${files[i].name} (${(files[i].size / 1024).toFixed(1)} KB)`;
        fileList.appendChild(li);
    }
});