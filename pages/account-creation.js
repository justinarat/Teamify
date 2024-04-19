function validateSignup(){
    for (let i = 0; i < 3; i++){
        let field = document.forms["sign-up"][i].value;
        if (field == ""){
            alert("All fields must be filled out");
            return false;
        }
    }
}