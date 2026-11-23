/* Browser-only device adapters. No provider secrets or authentication tokens live here. */
window.asmo = {
 locate(done) {
  if(!navigator.geolocation){done('', 'unavailable');return;}
  let settled=false;
  const complete=(address,error)=>{if(settled)return;settled=true;clearTimeout(deadline);done(address,error);};
  const deadline=setTimeout(()=>complete('', 'unavailable'),25000);
  navigator.geolocation.getCurrentPosition(position => {
   const {latitude,longitude}=position.coords;
   complete('https://maps.google.com/?q='+latitude.toFixed(6)+','+longitude.toFixed(6),'');
  }, error => complete('',error.code===1?'denied':'unavailable'), {enableHighAccuracy:true,timeout:20000,maximumAge:0});
 },
 pickPhoto(done) {
  const input = document.createElement('input'); input.type='file';input.accept='image/*';
  input.oncancel=()=>done('');
  input.onchange=()=>{
   const file=input.files?.[0];if(!file){done('');return;}
   const url=URL.createObjectURL(file),image=new Image();
   image.onerror=()=>{URL.revokeObjectURL(url);alert('Could not open this image. Please choose a JPEG or PNG.');done('');};
   image.onload=()=>{
    const factor=Math.min(1,1280/Math.max(image.width,image.height)),canvas=document.createElement('canvas');
    canvas.width=Math.max(1,Math.round(image.width*factor));canvas.height=Math.max(1,Math.round(image.height*factor));
    const context=canvas.getContext('2d');context.fillStyle='#fff';context.fillRect(0,0,canvas.width,canvas.height);context.drawImage(image,0,0,canvas.width,canvas.height);
    const data=canvas.toDataURL('image/jpeg',0.8).split(',')[1];URL.revokeObjectURL(url);
    if(data.length>Math.ceil(2*1024*1024*4/3)){alert('Image is too large. Please choose a smaller image.');done('');}else done(data);
   };image.src=url;
  };input.click();
 },
 qrPng(payload) {
  const qr=qrcode(0,'M');qr.addData(payload);qr.make();const modules=qr.getModuleCount(),scale=10,margin=4,canvas=document.createElement('canvas');
  canvas.width=canvas.height=(modules+margin*2)*scale;const ctx=canvas.getContext('2d');ctx.fillStyle='#fff';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.fillStyle='#000';
  for(let y=0;y<modules;y++)for(let x=0;x<modules;x++)if(qr.isDark(y,x))ctx.fillRect((x+margin)*scale,(y+margin)*scale,scale,scale);
  return canvas.toDataURL('image/png').split(',')[1];
 },
 scanBottle(done) {
  const dialog=document.createElement('dialog');dialog.innerHTML='<h2>Scan bottle QR / సీసా QR</h2><video autoplay playsinline muted></video><p class="status">Point the camera at an Asmo Fresh bottle label.</p><input aria-label="Bottle QR value" placeholder="Or paste asmo:bottle:…"><div class="controls"><button class="manual">Use pasted code</button><button class="cancel secondary">Cancel / రద్దు</button></div>';
  document.body.append(dialog);dialog.showModal();const video=dialog.querySelector('video'),canvas=document.createElement('canvas'),ctx=canvas.getContext('2d',{willReadFrequently:true});let stream,finished=false,frame;
  const finish=value=>{if(finished)return;finished=true;cancelAnimationFrame(frame);stream?.getTracks().forEach(t=>t.stop());dialog.close();dialog.remove();done(value||'');};
  dialog.querySelector('.manual').onclick=()=>finish(dialog.querySelector('input').value.trim());dialog.querySelector('.cancel').onclick=()=>finish('');dialog.addEventListener('cancel',e=>{e.preventDefault();finish('');});
  const scan=()=>{if(finished)return;if(video.readyState>=2&&video.videoWidth){const factor=Math.min(1,960/video.videoWidth);canvas.width=Math.round(video.videoWidth*factor);canvas.height=Math.round(video.videoHeight*factor);ctx.drawImage(video,0,0,canvas.width,canvas.height);const image=ctx.getImageData(0,0,canvas.width,canvas.height),code=jsQR(image.data,image.width,image.height,{inversionAttempts:'dontInvert'});if(code){finish(code.data);return;}}frame=requestAnimationFrame(scan);};
  if(navigator.mediaDevices?.getUserMedia)navigator.mediaDevices.getUserMedia({video:{facingMode:{ideal:'environment'}}}).then(result=>{if(finished){result.getTracks().forEach(t=>t.stop());return;}stream=result;video.srcObject=stream;video.play().catch(()=>{});scan();}).catch(()=>{dialog.querySelector('.status').textContent='Camera unavailable or permission denied. Paste the bottle QR value instead.';});
  else dialog.querySelector('.status').textContent='Camera unavailable. Paste the bottle QR value instead.';
 },
 download(blob,name){const url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);},
 shareText(text){if(navigator.share)navigator.share({title:'Asmo Fresh report',text}).catch(error=>{if(error.name!=='AbortError')this.download(new Blob([text],{type:'text/plain;charset=utf-8'}),'asmo-report.txt');});else this.download(new Blob([text],{type:'text/plain;charset=utf-8'}),'asmo-report.txt');},
 shareImage(data,title){const bytes=Uint8Array.from(atob(data),c=>c.charCodeAt(0));this.download(new Blob([bytes],{type:'image/png'}),(title.split('·')[0].trim()||'asmo-bottle')+'-qr.png');}
};