function validateSignup(formID){
    let numFields = document.forms[formID].length;
    for (let i = 0; i < numFields; i++){
        let field = document.forms[formID][i].value;
        if (field == ""){
            alert("Missing fields in " + formID + " form. Please fill in all fields in this form before submitting.");
            return false;
        }
    }
}