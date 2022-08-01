
var pizza;


//function for signing up. checks the validation of the password
function SignUp() {
    const password = document.getElementById("password").value;
    const verifyPassword = document.getElementById("verifyPassword").value;

    //password validation: at least one number, one lowercase and one uppercase letter and at least 8 characters
    var valid = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;

    if (valid.test(password) == false) {
        document.getElementById("errorMessage").innerHTML = "The password must contain at least one number, one lowercase and one uppercase letter";
    }
    else if (password !== verifyPassword) {
        document.getElementById("errorMessage").innerHTML = "The passwords does not match";
    }
    else {
        document.getElementById("errorMessage").innerHTML = "";
        window.alert("Sign up successfully");
    }
}



//sign in function
function LogIn() {
    window.alert("Logged in successfully");
}


var count = 0;




function goToOC() {
    const qty = document.getElementById("num_pizza").value;

    if (qty == "") {
        window.alert(`please fill out the wanted quantity`);
    }
    else {
        location.href = "/OrderConfirmation";
    }

}

// When the user clicks -> open the popup


function openPopUp() {
    event.preventDefault(); //to prevent the oage reload
    document.getElementById("overlay").style.display = "block";
    document.getElementById("modal").style.display = "block";
}


function closePopUp() {
    location.href = "/home";
}



// OC page
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear();

if (dd < 10) {
    dd = '0' + dd;
}

if (mm < 10) {
    mm = '0' + mm;
}

today = yyyy + '-' + mm + '-' + dd;


const curPage = window.location.pathname;
if (curPage.includes("sign%20up.html")) {
    document.getElementById("birthdate").setAttribute("max", today); //birthday must be in the past
}
if (curPage.includes("OrderConfirmation.html")) {
    document.getElementById("expDate").setAttribute("min", today); //exp. must be in the future
}



