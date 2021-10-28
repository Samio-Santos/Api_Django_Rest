function mostraSenha() {
  var senha = document.getElementById("password");
  var iconSenha = document.getElementById("hide");

  if (senha.type === "password") {
    senha.type = "text";
    iconSenha.src = "/static/img/mostrar.png";
  } else {
    senha.type = "password";
    iconSenha.src = "/static/img/escondido.png";
  }
}

// Validador de senha no cadastro

var myInput = document.getElementById("id_new_password1");
var rsenha = document.getElementById("id_new_password2");

var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var repeat_password = document.getElementById("repeat-password");

if (myInput) {
  // Quando o usuário clica no campo de senha, mostra a caixa de mensagem
  // myInput.onfocus = function() {
  //   document.getElementById("Valid-password").style.display = "block";
  // }

  // Quando o usuário clicar fora do campo de senha, oculte a caixa de mensagem
  // myInput.onblur = function() {
  //   document.getElementById("Valid-password").style.display = "none";
  // }

  // Função execulta dentro do CADASTRO.
  // Quando o usuário começa a digitar algo dentro dos campos de senha e repetir senhas

  rsenha.onkeyup = function () {
    if (myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
  };

  myInput.onkeyup = function () {
    // Validar letra minúsculas
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
      letter.classList.remove("invalid");
      letter.classList.add("valid");
    } else {
      letter.classList.remove("valid");
      letter.classList.add("invalid");
    }

    // Valida letras maiúsculas
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
      capital.classList.remove("invalid");
      capital.classList.add("valid");
    } else {
      capital.classList.remove("valid");
      capital.classList.add("invalid");
    }

    // Valida numeros
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
      number.classList.remove("invalid");
      number.classList.add("valid");
    } else {
      number.classList.remove("valid");
      number.classList.add("invalid");
    }

    // Valida o comprimento
    if (myInput.value.length >= 8) {
      length.classList.remove("invalid");
      length.classList.add("valid");
    } else {
      length.classList.remove("valid");
      length.classList.add("invalid");
    }

    // Verica se as senhas são iguais
    if (myInput.value == rsenha.value) {
      repeat_password.classList.remove("invalid");
      repeat_password.classList.add("valid");
    } else {
      repeat_password.classList.remove("valid");
      repeat_password.classList.add("invalid");
    }
    rsenha;
  };
}

// Muda a cor dos inputs de login quando o usuario cometer erros ao logar
if (document.querySelector(".alert-errorinput")) {
  input_username = document.querySelector("#username").style.borderBottom =
    "1px solid red";
  input_password = document.querySelector("#password").style.borderBottom =
    "1px solid red";
}

// Muda a cor dos inputs do REGISTRO quando o usuario cometer erros ao tentar criar uma conta
if (document.querySelector(".alert-error-error")) {
  labels = document
    .querySelectorAll(".erro-label")
    .forEach((p) => (p.style.color = "red"));

  input_nome = document.querySelector("#nome").style.borderBottom =
    "1px solid red";
  input_email = document.querySelector("#email").style.borderBottom =
    "1px solid red";
  input_password = document.querySelector(
    "#id_new_password1"
  ).style.borderBottom = "1px solid red";
  input_ConfirPassword = document.querySelector(
    "#id_new_password2"
  ).style.borderBottom = "1px solid red";
} else if (document.querySelector(".alert-warning-warning")) {
  labels = document.querySelector("#erro-label").style.color = "red";

  input_email = document.querySelector("#email").style.borderBottom =
    "1px solid red";
} else if (document.querySelector(".alert-info-info")) {
  labelSenha = document.querySelector("#senha").style.color = "red";
  labelConfirmSenha = document.querySelector("#senha1").style.color = "red";

  input_password = document.querySelector(
    "#id_new_password1"
  ).style.borderBottom = "1px solid red";
  input_ConfirPassword = document.querySelector(
    "#id_new_password2"
  ).style.borderBottom = "1px solid red";
}

function copyToken() {
  var copyToken = document.getElementById("token");

  /* Select the text field */
  copyToken.select();
  copyToken.setSelectionRange(0, 99999); /* For mobile devices */

  navigator.clipboard.writeText(copyToken.value);
}

function mostrToken() {
  var token = document.getElementById("token");
  var icontoken = document.getElementById("show-hide");
  
  if (token.type === "password") {
    token.style.color = "yellow"
    token.type = "text";
    icontoken.src = "/static/img/mostrar.png";
    
    
  } else {
    token.style.color = "white"
    token.type = "password";
    icontoken.src = "/static/img/escondido.png";


  }
}
