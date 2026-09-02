const fileInp = document.getElementById('file-Taker');
const fileList = document.getElementById('file-list');
const dropArea = document.getElementById('warp');

fileInp.addEventListener('change',uploadImage)

function uploadImage(){
    fileList.innerHTML='';

    const files = fileInp.files;

    // if (files.length == 0){
    //     fileList.innerHTML='<li>no file selected</li>';
    //     return;
    // }

    for (let i = 0; i < files.length; i++) {
        const li = document.createElement('li');
        li.textContent = `${files[i].name} (${(files[i].size / 1024).toFixed(1)} KB)`;
        fileList.appendChild(li);
    }
};

dropArea.addEventListener("drop",(e)=>{
    e.preventDefault();
    fileInp.files = e.dataTransfer.files;
    uploadImage();

});
dropArea.addEventListener("dragover",(e)=>{
    e.preventDefault();
});