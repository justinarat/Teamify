function validateSignup(formID){
    let numFields = document.forms[formID].length;
    for (let i = 0; i < numFields; i++){
        let field = document.forms[formID][i].value;
        if (field == ""){
            alert("All fields must be filled out in form");
            return false;
        }
    }
}