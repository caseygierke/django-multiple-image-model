Dropzone.autoDiscover=false;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'upload/',
    maxFiles:100,
    maxFilesize:2,
    acceptedFiles:'.jpg',
    // autoProcessQueue:false,
})