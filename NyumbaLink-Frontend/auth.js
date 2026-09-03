document.querySelectorAll('.toggle-password').forEach(button=>{
  button.addEventListener('click',()=>{
    const input=document.getElementById(button.dataset.target);
    const visible=input.type==='text';
    input.type=visible?'password':'text';
    button.textContent=visible?'Show':'Hide';
  });
});

document.querySelectorAll('.auth-form').forEach(form=>{
  form.addEventListener('submit',e=>{
    e.preventDefault();
    const success=form.querySelector('.success');
    if(success){success.classList.add('show');success.textContent=form.dataset.message||'Your details have been submitted successfully.';}
  });
});
