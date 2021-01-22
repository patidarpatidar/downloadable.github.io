var token = null
var loading = null
window.onLoad = function(){
console.log("onLoad")
 loading = document.getElementById('loading')
}
function validate(event){
      console.log('Form Submission')
           var error = document.getElementById('message');
           var message = null;
           var form = event.target
           var values = form.elements;
           var name = values.name.value;
           token = values.'csrfmiddlewaretoken'.value;
           var email = values.email.value;

           message = validateForm(form)
           if(message){
                error.innerHTML = message
                error.hidden = false
           }else{
                error.innerHTML = ""
                 error.hidden = true

                 //email
                 sendEmail(email , name ,token)
           }





      event.stopPropagation();
      return false
}

function validateForm(form){
           var values = form.elements;
           var name = values.name.value;
           token = values.csrfmiddlewaretoken.value;
           var message = null;
           var email = values.email.value;
           var password = values.password.value;
           var phone = values.phone.value;
           var repassword = values.repassword.value;

           if(!name.trim()){
              message = "Name Is Required"
           }else if(!email.trim()){
              message = "Email Is Required"
           }else if(!password.trim()){
              message = "Password Is Required"
           }else if(!repassword.trim()){
              message = "Enter Password Again"
           }else if(password.trim() != repassword.trim()){
              message = "Password Not Matched"
           }
           return message;
}

function sendEmail(email , name ,token){
loading.hidden = false
$.ajax({
  method:"POST",
  url: "/send-otp",
  data: { name:name , email:email , 'csrfmiddlewaretoken':token}
})
  .done(function( msg ){
   // alert("Data Saved:" + msg);
   loading.hidden = true
      showOtpInput()
  }).fail(function(err){
     loading.hidden=true
      alert('Cant Send Email')
  })
}

function showOtpInput(){
    var otpInput = document.getElementById('verificationInput')
    var submit = document.getElementById('submitButton')
    var verifyButton = document.getElementById('verifyButton')
    otpInput.hidden = false
    submit.hidden = true
    verifyButton.hidden = false
}

function verifyCode(){
   var codeInput = document.getElementById('code')
   var code = codeInput.value

loading.hidden = false

   $.ajax({
  method:"POST",
  url: "/verify",
  data: { 'code':code , 'csrfmiddlewaretoken':token}
})
  .done(function( msg ){
 loading.hidden = true

  }).fail(function(err){
  loading.hidden = true
      alert('Code is Invaild')
  })

}

function submitForm(){
var form = document.getElementById('form')
var message = validateForm(form)
if(message){

}else{
form.submit()
}
}