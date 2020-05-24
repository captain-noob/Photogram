submitOK = "true";
function preview_image(event) {
    var reader = new FileReader();
    reader.onload = function(){
            var output = document.getElementById('output_image');
            var bg = document.getElementById('bg');
            var img=document.getElementById('a');
            var fileinp=a.value;
            var ext=/(\.jpg|\.jpeg|\.png)$/i;
            if(!ext.exec(fileinp)){
                alert("you can upload .jpg .png .jpeg images ");
                a.value=="none dude..."
                reader.result=="";
                output.style.display='none';
                bg.style.display='none';
                return false;
            }else
            {
                output.style.display='block';
                bg.style.display='block';
                output.src = reader.result;
            }
        }
    reader.readAsDataURL(event.target.files[0]);
    
}
function onc(){
    var txta=document.getElementById('ab');
    var txt=document.getElementById('ab').value;
    if (txt.length > 60) {
     alert("may have no more than 60 characters");
    submitOK = "false";
    txta.value="";
}else{
    submitOK = "true";
}
}
